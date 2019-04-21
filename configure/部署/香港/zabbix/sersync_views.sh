#!/bin/bash
VIEWS_DATA_SERSYNC_DIR=`tree /opt/webapps/cms_9001/views/ | grep directories | awk '{print $1}'`
VIEWS_DATA_SERSYNC_FILE=`tree /opt/webapps/cms_9001/views/ | grep directories | awk '{print $3}'`
WEB_DATA_SERSYNC_DIR=`tree /opt/webapps/web_8001/views/ | grep directories | awk '{print $1}'`
WEB_DATA_SERSYNC_FILE=`tree /opt/webapps/web_8001/views/ | grep directories | awk '{print $3}'`
#echo $VIEWS_DATA_SERSYNC_DIR $VIEWS_DATA_SERSYNC_FILE $WEB_DATA_SERSYNC_DIR $WEB_DATA_SERSYNC_FILE
if [ $VIEWS_DATA_SERSYNC_DIR -eq $WEB_DATA_SERSYNC_DIR ] && [ $VIEWS_DATA_SERSYNC_FILE -eq $WEB_DATA_SERSYNC_FILE ];then
	echo 1
else
	echo 0
fi
