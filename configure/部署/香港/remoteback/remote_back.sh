#!/bin/bash
# # -_- ! 

. /etc/profile

token_var=`cat /usr/local/.tocken_var`
echo `hostname -I` |sed 's/\ /#/g' -  >/tmp/ipaddr.txt
ipaddr=`cat /tmp/ipaddr.txt`
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

dir_len=`find /backup/data_back/full/   -mindepth 1 -maxdepth 1 -type d  -mtime -2|wc -l`
if [ ${dir_len} -eq 0 ];then
	Subject="本地备份为空"
	Body="备份异常:${ipaddr}"
	SendToDingding_error $Subject $Body
	exit 2
fi

send_dir=`find /backup/data_back/full/   -mindepth 1 -maxdepth 1 -type d  -mtime -2`
for dir in ${send_dir}
do
	rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port 1873   ${dir}  rsync@krdataback.zhushuqt.com::${token_var}_mysql &>/dev/null
done

