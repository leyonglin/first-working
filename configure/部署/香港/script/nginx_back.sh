#!/bin/bash
#此脚本用于备份nginx的app
#每天03:00执行此脚本 将前一天的access.log重命名为access-xxxx-xx-xx.log格式，并重新打开日志文件
#Nginx app所在目录
NGX_PATH=/opt/apps/nginx
#获取昨天的日期
TODAY=$(date +%Y%m%d)
#获取7天前
AGO=$(date +%Y%m%d --date="-7 day")
#备份目录
bak_dir=/backup/apps_bak/
#备份目录
cd $bak_dir
tar -zcf nginx_dir.${TODAY}.tar.gz  $NGX_PATH 
#保留7天
cd $bak_dir   && [ -f nginx_dir.${AGO}.tar.gz ] && rm -f nginx_dir.${AGO}.tar.gz
