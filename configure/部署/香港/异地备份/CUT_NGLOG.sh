#!/bin/bash
#此脚本用于自动分割Nginx的日志，包括access.log和error.log
#每天00:00执行此脚本 将前一天的access.log重命名为access-xxxx-xx-xx.log格式，并重新打开日志文件
#Nginx日志文件所在目录
LOG_PATH=/opt/logs/nginx/
#获取昨天的日期
YESTERDAY=$(date +%Y%m%d --date="-1 day")
#获取7天前
AGO=$(date +%Y%m%d --date="-7 day")
#日志备份目录
bak_dir=/backup/log_bak/nginx/
#备份日志项目列表，切记，多个日志文件之间用空格隔开
#分割日志
cd $bak_dir
cp ${LOG_PATH}web_access.log ${bak_dir}web_access-${YESTERDAY}.log
cp ${LOG_PATH}web_error.log ${bak_dir}web_error-${YESTERDAY}.log
echo > ${LOG_PATH}web_access.log &&  chown swadmin.swadmin ${LOG_PATH}web_access.log
echo > ${LOG_PATH}web_error.log  &&  chown swadmin.swadmin ${LOG_PATH}web_error.log 
#保留7天
[ -f ${bak_dir}web_access-${AGO}.log ] && rm -f ${bak_dir}web_access-${AGO}.log
[ -f ${bak_dir}web_error-${AGO}.log ] && rm -f ${bak_dir}web_error-${AGO}.log
