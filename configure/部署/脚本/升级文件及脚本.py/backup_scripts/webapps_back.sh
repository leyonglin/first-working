#!/bin/bash
#此脚本用于备份tomcat的webapps
#Nginx app所在目录
webapps_PATH=/opt/webapps
#获取昨天的日期
TODAY=$(date +%Y%m%d)
#获取7天前
AGO=$(date +%Y%m%d --date="-7 day")
#备份目录
bak_dir=/opt/backup/webapps_bak/
#备份目录
 cd $bak_dir
 tar -zcf webapps.${TODAY}.tar.gz $webapps_PATH
#保留7天
[ -f $bak_dir/webapps.${AGO}.tar.gz ] &&  rm -rf $bak_dir/webapps.${AGO}.tar.gz
