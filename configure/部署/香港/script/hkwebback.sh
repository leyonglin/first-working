#!/bin/bash
##  *_*  This is backup of data views nginx/conf to remote backserver ! *_*
. /etc/profile
echo `hostname -I` |sed 's/\ /#/g' -  >/tmp/ipaddr.txt
ipaddr=`cat /tmp/ipaddr.txt`
backup_dir="/opt/backup/data_views_nginx/"
backup_log="/opt/backup/data_views_nginx/logs"
token=`find /opt/apps/nginx/conf/vhosts/  -mindepth 1 -maxdepth 1 -type d -printf "%P\n"  |sort -n |egrep -v '*.bak|*.back|tgapp*'|head -1`
#error
error()
{
    echo -e "\033[5;31m \t\t\t $1 \t\t\t  \033[0m" 1>&2
    exit 1
}
#钉钉接口
function SendToDingding_error(){ 
    Dingding_Url="https://oapi.dingtalk.com/robot/send?access_token=233d949181a02c7f64879520c6f95a99d69d02ee645a303b5f64ffe942fb4052" 
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

#判断备份目录
#if [ ! -x rsync ]; then
which rsync &>/dev/null
if [ $?  != 0 ]; then
  error "rsync 未安装."
  Subject="data_views_nginx异地备份失败"
  Body="${ipaddr} rsync 未安装"
  SendToDingding_error $Subject $Body
fi

if [ ! -d ${backup_dir} ];then 
    mkdir -p ${backup_dir}
fi	
if [ ! -d ${backup_log} ];then 
    mkdir -p ${backup_log}
fi

Rsync=`which rsync`
cd /opt/webapps && tar -caPf ${backup_dir}/data_views_nginx_`date +%Y%m%d%H%M`.tar.gz admin_7001/data/ cms_9001/views/  -C /opt/apps/nginx/ conf --exclude "Geo*" 
$Rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port 1873   /opt/backup/data_views_nginx/ rsync@hkdataback.zhushuqt.com::${token}_data_views_nginx >>/dev/null 2>&1
if [ $? -ne 0 ];then
    echo -e "`date +'%Y%m%d_%H:%M:%S'` 备份data_views_nginx发生错误,具体看日志" >> ${backup_log}/backlog_`date +%Y%m%d%H%M`.log
    Subject="data_views_nginx异地备份失败" 
    Body="${ipaddr}_data_views_nginx异地备份失败,请参考日志:${backup_log}"
    SendToDingding_error $Subject $Body
    exit 1
fi

#删除过期备份
keep_bak=`find  ${backup_dir} -mindepth 1 -maxdepth 1 -type f  |wc -l`
if [ $keep_bak -lt 1 ];then 
    Subject="data_views_nginx本地备份${keep_bak}份" 
    Body="${ipaddr}_data_views_nginx本地备份份数异常."
    SendToDingding_error $Subject $Body
    exit 0
elif [ $keep_bak -gt 5 ];then
    Subject="data_views_nginx本地备份${keep_bak}份" 
    Body="${ipaddr}_data_views_nginx本地备份份数异常."
    SendToDingding_error $Subject $Body
    cd ${backup_dir} && find  ${backup_dir} -mindepth 1 -maxdepth 2  -mtime +2 -type f |xargs  rm -f
    exit 0
else
    cd ${backup_dir} && find  ${backup_dir} -mindepth 1 -maxdepth 2  -mtime +2 -type f |xargs  rm -f
fi
