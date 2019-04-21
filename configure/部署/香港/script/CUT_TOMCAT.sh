#!/bin/bash
#此脚本用于自动分割tomcat.out
#每天00:00执行此脚本 将前一天的catalina.out复制为昨天的日志并将今天的清空,并删除7天前的日志
#tomcat日志
LOG_PATH="tomcat_7001  tomcat_7002  tomcat_7003  tomcat_8001 tomcat_8002 tomcat_8003  tomcat_9001  tomcat_9002"
#获取昨天的日期
YESTERDAY=$(date "+%Y-%m-%d" --date="-1 day")
#获取7天前
AGO=$(date "+%Y-%m-%d" --date="-7 day")
#获取日志路径
bac_dir=/backup/log_bak/tomcat/
#分割日志
for CUT_PATH in $LOG_PATH
do
    cd /opt/logs/tomcat/${CUT_PATH} && cp catalina.out ${bac_dir}catalina_${CUT_PATH}.${YESTERDAY}.out
    cd /opt/logs/tomcat/${CUT_PATH} && echo > catalina.out && chown swadmin.swadmin catalina.out
    #保留7天
    cd ${bac_dir} && rm -f *.${AGO}.*
    [ -f ${bac_dir}/*.${AGO}.* ] && rm  -f ${bac_dir}/*.${AGO}.*
done
