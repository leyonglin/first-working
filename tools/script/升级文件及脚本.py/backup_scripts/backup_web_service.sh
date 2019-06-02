#!/bin/bash

## ENV
NGINX_PATH="/opt/apps/nginx"
NGINX_LOG_PATH="/opt/logs/nginx"
TOMCAT_LOG_PAHT="/opt/logs/tomcat"
WEB_BACKUP_PATH="/opt/backup"
SAVE_CUTLOG_PATH="${WEB_BACKUP_PATH}/log_bak"
CUTLOG_SAVE_DAYS='4'
WEBAPPS_SAVE_DAYS='7'
YESTERDAY=$(date +%Y%m%d --date="-1 day")
TODAY=$(date +%Y%m%d)

CUT_LOG(){
        ## delete cut logs for more than specified days
        if [ -d ${SAVE_CUTLOG_PATH} ];then
        	find ${SAVE_CUTLOG_PATH} -type f -mtime +${CUTLOG_SAVE_DAYS} | xargs rm -f 
        fi
	## cut logs of nginx
        cd ${SAVE_CUTLOG_PATH}/nginx
	cp ${NGINX_LOG_PATH}/web_access.log ${SAVE_CUTLOG_PATH}/nginx/web_access-${YESTERDAY}.log
	cp ${NGINX_LOG_PATH}/web_error.log ${SAVE_CUTLOG_PATH}/nginx/web_error-${YESTERDAY}.log
        echo > ${NGINX_LOG_PATH}/web_access.log
        echo > ${NGINX_LOG_PATH}/web_error.log
	## cut logs of tomcat
        for i in tomcat_7001  tomcat_7002  tomcat_7003  tomcat_8001 tomcat_8002 tomcat_8003  tomcat_9001  tomcat_9002
	do
	  if [ -d ${TOMCAT_LOG_PAHT}/$i ];then
		cp ${TOMCAT_LOG_PAHT}/${i}/catalina.out ${SAVE_CUTLOG_PATH}/tomcat/catalina_${i}.${YESTERDAY}.out
		echo > ${TOMCAT_LOG_PAHT}/${i}/catalina.out
          fi
        done
	## chown to swadmin
        chown -R swadmin:swadmin ${SAVE_CUTLOG_PATH}
	## give authority to ybop
        find ${SAVE_CUTLOG_PATH} -type d |xargs setfacl -m u:ybop:rwx 
        find ${SAVE_CUTLOG_PATH} -type f |xargs setfacl -m u:ybop:rw 
        ## delete logs of overs 5 days
        find /opt/logs/ -type f -mtime +5  |egrep -v  pid |xargs rm -f


}

WEBAPPS_BACKUP(){
   	## delete backup webapps for more than specified days
        if [ -d ${WEB_BACKUP_PATH}/webapps_bak ];then
        	find ${WEB_BACKUP_PATH}/webapps_bak -type f -mtime +${WEBAPPS_SAVE_DAYS} | xargs rm -f
        fi
        ## backup
        cd ${WEB_BACKUP_PATH}/webapps_bak
        tar -zcf webapps.${TODAY}.tar.gz -C /opt/  webapps
	## chown to ybdeploy
        chown -R ybdeploy:ybdeploy ${WEB_BACKUP_PATH}/webapps_bak
	### give authority to ybop
	#setfacl -m u:ybop:rwx ${WEB_BACKUP_PATH}/webapps_bak
	#setfacl -m u:ybop:rw ${WEB_BACKUP_PATH}/webapps_bak/*

}

GEOIP_UPDATA(){
	su swadmin -c"cd /opt/apps/nginx/conf && wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz && gunzip -f GeoLiteCity.dat.gz && wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz && gunzip -f GeoIP.dat.gz"
}

## CUT LOGS
CUT_LOG
sleep 5
## backup webapps
WEBAPPS_BACKUP
sleep 5
## update geoip
GEOIP_UPDATA
