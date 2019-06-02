#!/bin/sh
#on xtrabackup 2.4.9
# 第一次执行它的时候它会检查是否有完全备份,否则先创建一个全库备份
# 当你再次运行它的时候，它会根据脚本中的设定来基于之前的全备或差量备份进行差量备份
##################
INNOBACKUPEX_PATH=innobackupex  #INNOBACKUPEX的命令
INNOBACKUPEXFULL=/usr/bin/$INNOBACKUPEX_PATH  #INNOBACKUPEX的命令路径
#mysql目标服务器以及用户名和密码
MYSQL_CMD=" --user=root --password=9tN6GFGK60Jk8BNkBJM611GwA66uDFeG -S /opt/data/data_16303/mysql.sock"  
TMPLOG="/tmp/innobackupex.$$.log"
MY_CNF=/opt/conf/my_16303.cnf #mysql的配置文件
MYSQL=/opt/apps/mysql/bin/mysql
BACKUP_DIR=/backup/data_back/xtrabackup # 备份的主目录
FULLBACKUP_DIR=$BACKUP_DIR/full # 全库备份的目录
INCRBACKUP_DIR=$BACKUP_DIR/incre # 差量备份的目录
#FULLBACKUP_INTERVAL=604800  # 全库备份的间隔周期，时间：秒
FULLBACKUP_INTERVAL=604800 # 全库备份的间隔周期，时间：秒
KEEP_FULLBACKUP=2 # 至少保留几个全库备份
XTRABACKUPLOG_DIR=/backup/data_back/xtrabackuplog
logfiledate=backup.`date +%Y%m%d%H%M`.txt
#开始时间
STARTED_TIME=`date +%s`
#############################################################################
# 显示错误并退出
#############################################################################
error()
{
    echo -e "\033[5;31m \t\t\t $1 \t\t\t  \033[0m" 1>&2
    exit 1
}
  
#新建全备和差异备份的目录
mkdir -p $FULLBACKUP_DIR
mkdir -p $INCRBACKUP_DIR
mkdir -p $XTRABACKUPLOG_DIR
# 检查执行环境
if [ ! -x $INNOBACKUPEXFULL ]; then
  error "$INNOBACKUPEXFULL未安装或未链接到/usr/bin."
fi
  
if [ ! -d $BACKUP_DIR ]; then
  error "备份目标文件夹:$BACKUP_DIR不存在."
fi
  
mysql_status=`netstat -nl | awk 'NR>2{if ($4 ~ /.*:16303/) {print "Yes";exit 0}}'`
if [ "$mysql_status" != "Yes" ];then
    error "MySQL 没有启动运行."
fi
  
if ! `echo 'exit' | $MYSQL -s $MYSQL_CMD` ; then
 error "提供的数据库用户名或密码不正确!"
fi
  
# 备份的头部信息
echo "----------------------------"
echo
echo "$0: MySQL备份脚本"
echo "开始于: `date +%F' '%T' '%w`"
echo "开始于: `date +%F' '%T' '%w`" >>$XTRABACKUPLOG_DIR/$logfiledate
echo
  
#查找最新的完全备份
LATEST_FULL_BACKUP=`find $FULLBACKUP_DIR -mindepth 1 -maxdepth 1 -type d -printf "%P\n" | sort -nr | head -1`
  
# 查找最近修改的最新备份时间
LATEST_FULL_BACKUP_CREATED_TIME=`stat -c %Y $FULLBACKUP_DIR/$LATEST_FULL_BACKUP`
#如果全备有效进行差量备份否则执行完全备份
if [  "$LATEST_FULL_BACKUP" -a `expr $LATEST_FULL_BACKUP_CREATED_TIME + $FULLBACKUP_INTERVAL + 5` -ge $STARTED_TIME ] ; then
   # 如果最新的全备未过期则以最新的全备文件名命名在差量备份目录下新建目录
   echo -e "完全备份$LATEST_FULL_BACKUP 未过期,将根据 $LATEST_FULL_BACKUP名字作为差量备份基础目录名"
   echo "   "
   NEW_INCRDIR=$INCRBACKUP_DIR/$LATEST_FULL_BACKUP
   mkdir -p $NEW_INCRDIR
   # 查找最新的差量备份是否存在.指定一个备份的路径作为差量备份的基础
   LATEST_INCR_BACKUP=`find $NEW_INCRDIR -mindepth 1 -maxdepth 1 -type d -printf "%P\n"  | sort -nr | head -1`
   INCRBASEDIR=$FULLBACKUP_DIR/$LATEST_FULL_BACKUP
   echo -e "差量备份将以$INCRBASEDIR作为备份基础目录"
   echo "   "
   echo "使用$LATEST_FULL_BACKUP 作为基础本次差量备份的基础目录."
   $INNOBACKUPEXFULL --defaults-file=$MY_CNF --use-memory=16G --compress --compress-threads=32  $MYSQL_CMD --incremental $NEW_INCRDIR --incremental-basedir $INCRBASEDIR > $TMPLOG 2>&1
   #保留一份备份的详细日志
   cat $TMPLOG >$XTRABACKUPLOG_DIR/$logfiledate
   if [ ! -z "`tail -1 $TMPLOG | grep 'innobackupex: completed OK'`" ] ; then
     echo "$INNOBACKUPEX命令执行失败:"; echo
     echo -e "---------- $INNOBACKUPEX_PATH错误 ----------"
     cat $TMPLOG
     rm -f $TMPLOG
     exit 1
   fi
   THISBACKUP=`awk -- "/Backup created in directory/ { split( \\\$0, p, \"'\" ) ; print p[2] }" $TMPLOG`
   rm -f $TMPLOG
   echo -n "数据库成功备份到:$THISBACKUP"
   echo
   # 提示应该保留的备份文件起点
   LATEST_FULL_BACKUP=`find $FULLBACKUP_DIR -mindepth 1 -maxdepth 1 -type d -printf "%P\n" | sort -nr | head -1`
   NEW_INCRDIR=$INCRBACKUP_DIR/$LATEST_FULL_BACKUP
   LATEST_INCR_BACKUP=`find $NEW_INCRDIR -mindepth 1 -maxdepth 1 -type d -printf "%P\n"  | sort -nr | head -1`
   RES_FULL_BACKUP=${FULLBACKUP_DIR}/${LATEST_FULL_BACKUP}
   RES_INCRE_BACKUP=`dirname ${INCRBACKUP_DIR}/${LATEST_FULL_BACKUP}/${LATEST_INCR_BACKUP}`
   echo
   echo -e '\e[31m NOTE:---------------------------------------------------------------------------------.\e[m' #红色
   echo -e "必须保留$KEEP_FULLBACKUP份全备即全备${RES_FULL_BACKUP}和${RES_INCRE_BACKUP}目录中所有差量备份."
   echo -e '\e[31m NOTE:---------------------------------------------------------------------------------.\e[m' #红色
   echo
else
   echo  "*********************************"
   echo -e "正在执行全新的完全备份...请稍等..."
   echo  "*********************************"
   $INNOBACKUPEXFULL --defaults-file=$MY_CNF  --use-memory=16G --compress --compress-threads=32  $MYSQL_CMD $FULLBACKUP_DIR > $TMPLOG 2>&1 
   #保留一份备份的详细日志
   cat $TMPLOG>$XTRABACKUPLOG_DIR/$logfiledate
   if [ ! -z "`tail -1 $TMPLOG | grep 'innobackupex: completed OK!'`" ] ; then
     echo "$INNOBACKUPEX命令执行失败:"; echo
     echo -e "---------- $INNOBACKUPEX_PATH错误 ----------"
     cat $TMPLOG
     rm -f $TMPLOG
     exit 1
   fi
     
   THISBACKUP=`awk -- "/Backup created in directory/ { split( \\\$0, p, \"'\" ) ; print p[2] }" $TMPLOG`
   rm -f $TMPLOG
   echo -n "数据库成功备份到:$THISBACKUP"
   echo
   # 提示应该保留的备份文件起点
   LATEST_FULL_BACKUP=`find $FULLBACKUP_DIR -mindepth 1 -maxdepth 1 -type d -printf "%P\n" | sort -nr | head -1`
   RES_FULL_BACKUP=${FULLBACKUP_DIR}/${LATEST_FULL_BACKUP}
   echo
   echo -e '\e[31m NOTE:---------------------------------------------------------------------------------.\e[m' #红色
   echo -e "无差量备份,必须保留$KEEP_FULLBACKUP份全备即全备${RES_FULL_BACKUP}."
   echo -e '\e[31m NOTE:---------------------------------------------------------------------------------.\e[m' #红色
   echo
fi
#删除过期的全备,差备，日志
echo -e "find expire backup file...........waiting........."
echo -e "寻找过期的全备文件并删除">>$XTRABACKUPLOG_DIR/$logfiledate
EXPIRE_DIR=`find $FULLBACKUP_DIR  -mindepth 1 -maxdepth 1 -mtime +14 -type d -printf "%P\n"`
for file in $EXPIRE_DIR
do
   echo "全备文件 $file 过期删除" >>$XTRABACKUPLOG_DIR/$logfiledate
   cd $FULLBACKUP_DIR && rm $file -rf
   cd $INCRBACKUP_DIR && rm $file -rf
done
find $XTRABACKUPLOG_DIR  -mindepth 1 -maxdepth 1 -name backup.\* -mtime +14 -type f |xargs  rm -f
#完成时间
echo -e "完成于: `date +%F' '%T` \t 星期`date +%w`"
echo -e "完成于: `date +%F' '%T` \t 星期`date +%w`" >>$XTRABACKUPLOG_DIR/$logfiledate
