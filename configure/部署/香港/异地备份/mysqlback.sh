#!/bin/bash
#***************************************************************#
# Create: DBA
#***************************************************************#
echo `hostname -I` |sed 's/\ /#/g' -  >/tmp/ipaddr.txt
ipaddr=`cat /tmp/ipaddr.txt`
backup_time=`date +'%Y%m%d%m'`
backup_base="/backup/data_back"
backup_dir="$backup_base/full"
backup_log="$backup_base/log/xtra_${backup_time}.log"
backup_user='bkpuser'
backup_password='EKju_QoQP4z8EirBMxsCSZSuPFJct8qR'
slave_days=7

#钉钉接口
function SendToDingding_error(){ 
    Dingding_Url="https://oapi.dingtalk.com/robot/send?access_token=d5201a579163dc6045b6da6d8dbc1cdc1d935698050971ceddb5a8956e9507ee"
 
    # 发送钉钉消息
    curl "${Dingding_Url}" -H 'Content-Type: application/json' -d "
    {
        \"actionCard\": {
            \"title\": \"$1\", 
            \"text\": \"$2\", 
            \"hideAvatar\": \"0\", 
            \"btnOrientation\": \"0\", 
            \"btns\": [
                {
                    \"title\": \"$1\", 
                    \"actionURL\": \"\"
                }
            ]
        }, 
        \"msgtype\": \"actionCard\"
    }"
} 

if [ ! -x /usr/bin/innobackupex ];then
	yum -y install  http://www.percona.com/downloads/percona-release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm
	yum -y install percona-xtrabackup-24 qpress
fi
#开始创建目录
if [ ! -d ${backup_dir} ];then 
    mkdir -p ${backup_dir}
fi
if [ ! -d ${backup_base}/log ];then 
    mkdir -p ${backup_base}/log 
fi

start_time=`date +'%Y%m%d_%H:%M:%S'`
#开始备份数据库
echo -e "`date +'%Y-%m-%d %H:%M:%S'` 开始物理备份数据库 ${ipaddr} ..." >> ${backup_log}


/usr/bin/innobackupex --defaults-file=/opt/conf/my_16303.cnf --user=${backup_user} --password=${backup_password} --host='localhost' --socket=/opt/data/data_16303/mysql.sock --use-memory=1G --compress --compress-threads=32 --parallel=3 --slave-info ${backup_dir} 2>>${backup_log}
if [ $? -ne 0 ];then
    echo -e "`date +'%Y%m%d_%H:%M:%S'` 备份数据库发生错误,具体看日志" >> ${backup_log}
    Subject="物理备份xtra备份失败" 
    Body="'${ipaddr}'_物理备份失败,请参考日志:${backup_log}"
    SendToDingding_error $Subject $Body
    exit 1
fi


if [ ! -z "`tail -1 ${backup_log} | grep 'completed OK'`" ]; then
    finish_time=`date +'%Y%m%d_%H:%M:%S'`
    file_size=`du -sm ${backup_dir} |awk '{print $1}'`
    echo -e "${ipaddr}数据库xtrabackup物理备份工作完成!\n 开始时间：${start_time} 结束时间：${finish_time}\n 备份目录${backup_dir}\n 
备份文件大小${file_size} MB" >> ${backup_log}
    #删除以前的备份
    echo -e "`date +'%Y%m%d_%H:%M:%S'` 开始删除${slave_days}天以前的备份" >> ${backup_log}
    for tfile in $(/usr/bin/find ${backup_dir}  -mindepth 1 -maxdepth 1 -mtime +${slave_days})
      do 
         cd ${backup_dir} && rm -rf ${tfile} 2>>${backup_log}
         echo -e "---- delete file :${file} -----" >> ${backup_log}
      done 
    echo -e "`date +'%Y%m%d_%H%M%S'` 删除${slave_days}天以前的备份-完成" >> ${backup_log}
    find $backup_base/log  -mindepth 1 -maxdepth 1  -mtime +${slave_days} -type f |xargs  rm -f
else
    echo -e "`date +'%Y%m%d_%H:%M:%S'` 备份数据库发生错误,具体看日志" >> ${backup_log}
    Subject="物理备份xtra备份失败" 
    Body="${ipaddr}_物理备份失败,请参考日志:${backup_log}"
    SendToDingding_error $Subject $Body

fi



exit
