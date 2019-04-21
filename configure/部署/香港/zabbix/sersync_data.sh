#!/bin/bash
ADMIN_DATA_SERSYNC_DIR=`tree /opt/webapps/admin_7001/data/ | grep directories | awk '{print $1}'`
ADMIN_DATA_SERSYNC_FILE=`tree /opt/webapps/admin_7001/data/ | grep directories | awk '{print $3}'`
WEB_DATA_SERSYNC_DIR=`tree /opt/webapps/web_8001/data/ | grep directories | awk '{print $1}'`
WEB_DATA_SERSYNC_FILE=`tree /opt/webapps/web_8001/data/ | grep directories | awk '{print $3}'`
#echo $ADMIN_DATA_SERSYNC_DIR $ADMIN_DATA_SERSYNC_FILE $WEB_DATA_SERSYNC_DIR $WEB_DATA_SERSYNC_FILE
if [ $ADMIN_DATA_SERSYNC_DIR -eq $WEB_DATA_SERSYNC_DIR ] && [ $ADMIN_DATA_SERSYNC_FILE -eq $WEB_DATA_SERSYNC_FILE ];then
	echo 1
else
	echo 0
fi
