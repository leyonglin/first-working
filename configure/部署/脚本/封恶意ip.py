#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os,sys,commands,time,datetime, requests, json

# env
dingding_api="https://oapi.dingtalk.com/robot/send?access_token=3281ef8bc7b0bd4ca0e270facbad39befdf2a56d56c600c909c75a8abfa091e3"
filter_str='v/user/login'
now_time=time.strftime('%Y-%m-%d %H:%M',time.localtime())
check_minutes=30
before_time=(datetime.datetime.now()-datetime.timedelta(minutes=check_minutes)).strftime("%H:%M")
log_path="/opt/logs/tomcat/tomcat_8001/catalina.out"
limit_counts=10
site_token=commands.getoutput('egrep "^Hostname" /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf | cut -d "-" -f 2')
site_ip=commands.getoutput('hostname -I').split()[0]
deny_log='/opt/src/upload/denyIps.log'
cdn_ips_files='/opt/scripts/cdn_nodeip'
cdn_nodeips=commands.getoutput('cat %s'%(cdn_ips_files)).split('\n')
cdn_nodeips=list(map(lambda x:x, [i.strip() for i in cdn_nodeips]))
#already_blackips=commands.getoutput("firewall-cmd --direct --get-all-rules |egrep \"DROP|REJECT\" |awk '{print $6}'").split('\n')
already_blackips=commands.getoutput("firewall-cmd --info-ipset=blacklist |egrep entries|awk -F ':' '{print $2}'").split()

def fliter_blackips():
    total = 10
    while total > 0:
        # 获得指定时间前的日志的行数的num
        line_num=commands.getoutput("egrep -n ^%s %s |head -1 |awk -F':' '{print $1}'"%(before_time,log_path)).split('\n')[0]
        if line_num and 'grep' not in line_num:
            break
        else:
            time.sleep(1)
    try:
    except ValueError:
        print('什么都没有')
        exit()
    black_ips=list(map(lambda x:x, [ i for i in get_infos if i not in already_blackips + cdn_nodeips  ]))
    return black_ips

def firewall_deny(blackip):
    #os.system('iptables -I INPUT -s %s -j DROP'%(blackip))
    #os.system("firewall-cmd --permanent --direct --add-rule ipv4 filter INPUT 0 -s %s -p tcp --dport 80 -j  DROP"%(blackip))
    #os.system("firewall-cmd --permanent --direct --add-rule ipv4 filter INPUT 0 -s %s -p tcp --dport 443 -j  DROP"%(blackip))
    os.system("firewall-cmd --permanent  --ipset=blacklist --add-entry=%s" %(blackip))

def send_to_dingding(text):
    url = dingding_api
    HEADERS = {"Content-Type":"application/json;charse^t=utf-8"}
    String_textMsg = {"msgtype":"text", "text": {"content": text}}
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    print(res.text)

def main():
    blackips=fliter_blackips()
    print(blackips)
    if blackips and blackips[0] != '':
        ## 写入封锁日志
        os.system('echo %s %s-%s: firewalld封掉%s分钟内刷登录接口次数超过%s次的IP %s >> %s'%(now_time, site_token, site_ip, check_minutes, limit_counts,blackips,deny_log))
        for i in blackips:
            firewall_deny(i)
        os.system("firewall-cmd --reload")
        ## 钉钉报警
        send_to_dingding('%s 【%s-%s】: %s分钟内刷验证码次数超过%s次的IP. 累计封%d 个 \n%s'%(now_time, site_token, site_ip, check_minutes, limit_counts, len(already_blackips + blackips), blackips))

if __name__ == "__main__":
    main()
