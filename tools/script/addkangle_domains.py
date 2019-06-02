#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys
import re
import random
import commands
import requests
import json
import paramiko
from urllib import urlencode
import base64

# 获得服务器上所有域名的列表
oppass_ssl = b'eXlKczRjdlpyRXlaSTFBWEM4NzRISWwyMm94MDZWOTRXYnVSR1JubzE3YkFQYTlES1ZlVG1BU1lCdmVxcEwyTUR6YkJrUlhBNFBzS2FrT0JzUXI1R3JnYmF1enN0ZzlWTVk0NFo1OXdZWU5NSGNUajJpVFl3czhGU3FNN2RQSlE='
oppass = base64.b64decode(oppass_ssl).decode('utf-8')
names=commands.getoutput('egrep server_name /opt/apps/nginx/conf/vhosts/* -R |awk -F"server_name" "{print \$2}"|awk -F";" "{print \$1}"').split(' ')
all_name=list(map(lambda x:x, [ i.strip('\n') for i in names if '_' not in i and i != '']))
adminnames=commands.getoutput('egrep server_name `find /opt/apps/nginx/conf/vhosts/ -name "*admin*" -o -name "*cms*" -o -name "*agent*"`|awk -F "(server_name +|;)" "{print \$2}"').split()
# 选择操作
while True:
    print("\033[36m \t\t\t+---------------------------------------+\t\t\t \033[0m")
    print("\033[36m \t\t\t|      请选择您要做的操作               |\t\t\t \033[0m")
    print("\033[36m \t\t\t+---------------------------------------+\t\t\t \033[0m")
    print("\033[36m \t\t\t| (1) 添加web普通域名   	        |\t\t\t \033[0m")
    print("\033[36m \t\t\t| (2) 添加web证书域名                   |\t\t\t \033[0m")
    print("\033[36m \t\t\t| (6) 添加服务器所有域名到海啸cdn       |\t\t\t \033[0m")
    #print("\033[36m \t\t\t| (3) 添加<admin后台域名                |\t\t\t \033[0m")
    #print("\033[36m \t\t\t| (4) 添加<cms后台域名>                 |\t\t\t \033[0m")
    #print("\033[36m \t\t\t| (5) 添加<agent后台域名>               |\t\t\t \033[0m")
    print("\033[36m \t\t\t+---------------------------------------+\t\t\t \033[0m")
    which_do = input("\033[36m \t\t\t： \033[0m")
    if which_do in [1, 2, 3, 4, 5, 6]:
        break
    else:
        print("\033[31m \t\t\t请选择正确的类型 \033[0m")
        continue

def interative(InterativeRole,InterativeConfirm):
    '''配置交互式输入参数'''
    while True:
        InterativeRole = InterativeRole
        InterativeConfirm = InterativeConfirm
        GetInfo = raw_input('\n%s ' % (InterativeRole))
        confir = raw_input('%s：\033[35m%s\033[0m\n \t\t\t确认无误请输入yes/y，错误请输入no:  ' % ( InterativeConfirm, GetInfo))
        if confir == 'yes' or confir == 'y':
            break
        else:
            continue
    return GetInfo

#def get_model_file(file_list, need):
#    '''找出添加非证书域名的文件，或者要添加证书域名的源文件（用来拷贝新的https文件）'''
#    for i in file_list:
#        f = open(i,'r')
#        f.readline()
#        for line in f:
#            ## 包含指定的字符串，且不是default文件
#            if need in line.strip() and i.endswith('.conf') and 'default_server.conf' not in i and 'tgapp' not in i:
#                return i

def add_name(new_name,web_file):
    '''将新域名（new_name)添加到server文件（web_file）中'''
    fopen = open(web_file,'r')
    w_str = ""
    for line in fopen:
            if re.search('server_name',line):
                    line=re.sub(';',' %s;'%(new_name),line)
                    w_str+=line
            else:
                    w_str+=line
    wopen = open(web_file,'w')
    wopen.write(w_str)
    fopen.close()
    wopen.close()
    print '\033[32m \t\t\t【%s】新增添加域名: \033[0m\033[33m%s\033[0m' %(web_file,new_name)

def add_crt(yuan_file, name_list, crt_file, key_file,token):
    '''配置证书域名'''
    ## 建立server文件，从老的htpps_web.conf拷出来
    randomstr = ''.join(random.sample(['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],3))
    new_name = name_list[0]
    #crt_server_file = yuan_file.rstrip('web.conf') + randomstr + '_' + new_name.rstrip('.com').strip('*.') + '.conf'
    crt_server_file = '/opt/apps/nginx/conf/vhosts/%s/https_'%token + randomstr + '_' + new_name.rstrip('.com').strip('*.') + '.conf'
    if not os.path.exists(crt_server_file):
        os.system('cp -p  %s %s' %(yuan_file, crt_server_file))
        os.system("sed -i '/## begin/,/## end/d' %s"%crt_server_file)
    else:
        print('\n\033[31m \t\t\t脚本自动生成的server文件：%s已经存在，请将就目录和相关server文件ssl做更改，再执行脚本\033[0m\n'%(crt_server_file))
        sys.exit()
    ## 建立证书目录,拷贝证书文件: 并将之前文件统一命名为：server.crt server.key 
    key_path = '/opt/apps/nginx/conf/keys'
    new_crt_path = key_path + '/'+ randomstr + '_'  + new_name.rstrip('.com') + '_crt'
    new_name_key_path = new_crt_path.replace('/opt/apps/nginx/conf/keys/','') # eg: /opt/apps/nginx/conf/key/abc_com --> abc_com
    
    if not os.path.exists(new_crt_path):
        os.makedirs('%s'%(new_crt_path))
        os.system('cp -r %s %s/server.crt'%(crt_file, new_crt_path))
        os.system('cp -r %s %s/server.key'%(key_file, new_crt_path))
    else:
        print('\n\033[31m \t\t\t脚本自动生成的证书目录：%s已经存在，请将就目录和相关server文件ssl做更改，再执行脚本\033[0m\n'%(new_crt_path))
        sys.exit()
    ## 修改ssl
    os.system('sed -i "/ssl_certificate /s/.*/    ssl_certificate keys\/%s\/server.crt;/g" %s' %(new_name_key_path, crt_server_file))
    os.system('sed -i "/ssl_certificate_key /s/.*/    ssl_certificate_key keys\/%s\/server.key;/g" %s' %(new_name_key_path, crt_server_file))
    ## 清空新证书https文件的server_name，这样后面加的都是证书域名
    os.system('sed -i "/server_name/s/.*/    server_name  ;/g" %s' %(crt_server_file))
    ## 添加域名:调用前面设置的add_name函数
    for crt_one in name_list:
        add_name(crt_one, crt_server_file)

def check_do():
    print('\n\033[33m配置完毕，nginx -t进行健康检查，请根据下面输出结果自行做相关重启nginx、同步到备站重启nginx等操作\033[0m\n')
    os.system('/opt/apps/nginx/sbin/nginx  -t')
    print ''
###查找小黄所有域名id
def xh_all_id(sss,token,xh_cookie):
    url_id = {}
    token_url = "http://cdn3.01ip.cn/api2/site/index.php/domain/list"
    header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
        }
    data={
            'domain': token,
            'offset': 0,
            'length': 10000,
            'keyword': ''
        }
    sss.cookies.set("authentication", xh_cookie)
    resp1 = json.loads(sss.post(token_url, data=data ,headers=header).text)
    token_domain=resp1['domains']
    for eachdomain in token_domain:
        url_id[eachdomain['domain']]=eachdomain['id']
    return url_id
###查找海啸cdn所有域名id
def haix_all_id(sss,token,haix_cookie):
    sss.cookies.set("authentication", haix_cookie)
    search_token_url='http://cloud.fangddos.cc/api2/site/index.php/domain/search'
    search_token_data = {
        "search": "%s."%token,
	"type": "pre_host",
	"offset": 0,
	"length": 5000
	}
    header={
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
       }
    resp=sss.post(search_token_url,data=search_token_data,headers=header)
    resp_json=json.loads(resp.text)
    resp_status=resp_json['status']
    haix_all_id={}
    #print('\n\033[33m \t\t\t%s\033[0m'%resp_status["message"])
    #    print('\n\033[32m \t\t\t该站点未在海啸cdn上添加任何域名\033[0m')
    if resp_status["message"].encode("UTF-8")=="操作成功":
    #    print('\n\033[31m \t\t\t该站点在海啸cdn上添加了部分域名\033[0m') 
        domains=resp_json["rows"]
        for eachdomain in domains:
            haix_all_id[eachdomain["domain"]]=eachdomain["id"]
    elif resp_status["message"].encode("UTF-8")=="无匹配项":
        haix_all_id={}
    return haix_all_id

def haix_dup_domain(all_name,haix_allold_id):
    haix_need_name=[i for i in all_name]
    haix_already_name=[]
    if haix_allold_id:
        for eachname in all_name:
            if eachname in haix_allold_id:
	        haix_need_name.pop(haix_need_name.index(eachname))
	        haix_already_name.append(eachname)
    return haix_need_name,haix_already_name

def haix_cdn_add(sss,token,haix_need_name,zhuip,all_name,haix_cookie): 
    print("\n\033[31m \t\t\t开始添加海啸cdn。。。。。\033[0m")
    domain_add_url='http://cloud.fangddos.cc/api2/site/index.php/domain' 
    header={
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
    }
    sss.cookies.set("authentication", haix_cookie)
    base_ssl_dir="/opt/apps/nginx/conf/"
    if not haix_need_name:
        print("\n\033[32m \t\t\tcdn不存在需要添加的域名，继续查看是否有需要更新证书的域名\033[0m")
    else:
        for eachname in haix_need_name:
            ###海啸cdn证书域名推送证书密钥
            eachname_all_file=commands.getoutput('grep %s /opt/apps/nginx/conf/vhosts/* -r | grep -v ssl |cut -d ":" -f 1'%eachname).split('\n')
            eachname_conf_num=0
            for eachfile in eachname_all_file:
                if str(eachfile).endswith(".conf"):
                   eachname_conf_num+=1 
            if eachname_conf_num == 1:
               for eachfile in eachname_all_file:
                   if str(eachfile).endswith(".conf"):
                       eachname_conf_file=eachfile
            else:
                print("\n\031[31m \t\t\t有多个配置文件包含此域名：%s,请检查\033[0m"%eachname)
                continue
            domain_add_data={
	    "host": zhuip,
	    "domain": eachname
    	    }
	    ###海啸cdn添加
            sss.post(domain_add_url,data=domain_add_data,headers=header)
    print("\n\033[32m \t\t\t海啸cdn域名已添加，准备添加证书文件\033[0m")
    haix_allnew_id=haix_all_id(sss,token,haix_cookie)
    for eachname in all_name:
        eachname_all_file=commands.getoutput('grep %s /opt/apps/nginx/conf/vhosts/* -r | grep -v ssl |cut -d ":" -f 1'%eachname).split('\n')
        eachname_conf_num=0
        for eachfile in eachname_all_file:
            if str(eachfile).endswith(".conf"):
               eachname_conf_num+=1 
        if eachname_conf_num == 1:
           for eachfile in eachname_all_file:
               if str(eachfile).endswith(".conf"):
                   eachname_conf_file=eachfile
        else:
            print("\n\031[31m \t\t\t有多个配置文件包含此域名：%s,请检查\033[0m"%eachname)
	eachname_crt_confirm=commands.getoutput('egrep "\ +ssl_certificate" %s |grep -v _key|wc -l'%eachname_conf_file)
	if eachname_crt_confirm == "0":
	    print("\n\033[32m \t\t\t%s是普通域名,无需证书操作\033[0m"%eachname)
	    continue
	elif eachname_crt_confirm == "1":
	    print("\n\033[33m \t\t\t%s是证书域名，添加证书\033[0m"%eachname)
	    eachname_crt_location=commands.getoutput('egrep "\ +ssl_certificate" %s |grep -v _key|awk \'{print $2}\' |cut -d ";" -f 1'%eachname_conf_file)
	    eachname_key_location=commands.getoutput('egrep "\ +ssl_certificate" %s |grep _key|awk \'{print $2}\' |cut -d ";" -f 1'%eachname_conf_file)
	    if str(eachname_crt_location).startswith("keys") and str(eachname_key_location).startswith("keys"):
	        eachname_ssl_crt=base_ssl_dir + eachname_crt_location
		eachname_ssl_key=base_ssl_dir + eachname_key_location
	    else:
	        print("\n\033[31m \t\t\t%snginx配置证书密钥不规范，请以keys开头\033[0m"%eachname)
	        continue 
	    eachname_crt=commands.getoutput('cat %s'%eachname_ssl_crt)
	    eachname_key=commands.getoutput('cat %s'%eachname_ssl_key)
	    eachname_id=haix_allnew_id[eachname]
	    eachname_addssl_url='http://cloud.fangddos.cc/api2/site/index.php/domain/public/%s'%eachname_id
	    eachname_addssl_data='force_ssl=1&sslcsr=%s&sslkey=%s&hash=&max_error_count=&error_try_time=&hsts=0&portmap=0'%(eachname_crt,eachname_key)
            sss.put(eachname_addssl_url,data=eachname_addssl_data,headers=header) 
    print("\n\033[32m \t\t\tcdn证书更新完毕\033[0m") 
###查找已添加cdn的域名
def find_dup_url(sss,token,xh_cookie,new_name):
    #print('\n\033[31m \t\t\t开始添加cdn域名\033[0m')
    old_all_id = xh_all_id(sss,token,xh_cookie)
    need_add_url=[i for i in new_name]
    cdn_dup_url=[]
    for each_new_name in new_name:
        if each_new_name in old_all_id:
            need_add_url.pop(need_add_url.index(each_new_name))
            cdn_dup_url.append(each_new_name)
    return need_add_url,cdn_dup_url	    
###开始添加cdn域名
def add_cdn_url(sss,token,xh_cookie,new_name,zhuip,which_do,crt_file,key_file):
    need_add_url=find_dup_url(sss,token,xh_cookie,new_name)[0]
    cdn_dup_url=find_dup_url(sss,token,xh_cookie,new_name)[1]
    sss.cookies.set("authentication", xh_cookie) 
    token_get_url='http://cdn3.01ip.cn/api2/proxy/index.php/vhost/info/%s'%token
    header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
         }
    sss.get(token_get_url,headers=header)
    sss_post_url='http://cdn3.01ip.cn/api2/site/index.php/domain'
    for eachname in need_add_url:
        data={
            'host': zhuip,
	    'domain': eachname
        }
        sss.post(sss_post_url,data=data,headers=header)
    if which_do==1:
        if bool(need_add_url) is True:
            print('\n\033[32m \t\t\t普通域名%s小黄cdn已添加完毕\033[0m\n'%(' ').join(need_add_url))
	else:
	    print('\n\033[32m \t\t\t没有需要添加cdn域名\033[0m\n')
    elif which_do==2:
         new_all_id=xh_all_id(sss,token,xh_cookie)
	 domain_crt=commands.getoutput('cat %s'%crt_file)
	 domain_key=commands.getoutput('cat %s'%key_file)
	 if bool(need_add_url) is True:
	     for eachname in need_add_url:
	         eachname_id=new_all_id[eachname]
	         token_put_url='http://cdn3.01ip.cn/api2/site/index.php/domain/public/%s'%eachname_id
	         #put_data='force_ssl=1&sslcsr=%s&sslkey=%s&hash=&max_error_count=&error_try_time=&hsts=0&portmap=0'%(domain_crt,domain_key)
		 put_data={
		     'force_ssl': 1,
		     'sslcsr': domain_crt,
		     'sslkey': domain_key,
		     'hash': '',
		     'max_error_count': '',
		     'error_try_time': '',
		     'hsts': 0,
		     'portmap': 0
		     }
	         sss.put(token_put_url,data=urlencode(put_data),headers=header)
	     print('\n\033[32m \t\t\t新证书域名%s小黄cdn已添加完毕\033[0m'%(' ').join(need_add_url))
	 if bool(cdn_dup_url) is True:
             for eachname in cdn_dup_url:
                 eachname_id=new_all_id[eachname]
                 token_put_url='http://cdn3.01ip.cn/api2/site/index.php/domain/public/%s'%eachname_id
                 #put_data='force_ssl=1&sslcsr=%s&sslkey=%s&hash=&max_error_count=&error_try_time=&hsts=0&portmap=0'%(domain_crt,domain_key)
		 put_data={
		     'force_ssl': 1,
		     'sslcsr': domain_crt,
		     'sslkey': domain_key,
		     'hash': '',
		     'max_error_count': '',
		     'error_try_time': '',
		     'hsts': 0,
		     'portmap': 0
		     }
                 sss.put(token_put_url,data=urlencode(put_data),headers=header)
             print('\033[32m \t\t\t域名%s小黄cdn证书替换完毕\033[0m\n'%(' ').join(cdn_dup_url))
def nginx_reload():
    print('\n\t\t\t\033[33mnginx准备重载\033[0m')
    ###主站重启
    os.system('echo %s|su ybop -c "sudo /etc/init.d/nginx -t && sudo /etc/init.d/nginx reload"'%oppass)
    print('\n\t\t\t\033[32m主站nginx重载成功\033[0m')
    ####备站重启
    sitessh = paramiko.SSHClient()
    sitessh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    web_back_ip=commands.getoutput('grep remote /opt/apps/sersync/nginx_conf.xml | egrep -o "[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}"').strip('\n').split()
    if web_back_ip:
        for eachip in web_back_ip:
            try:
                print "\n\t\t\t\033[33m备站%snginx准备重载\033[0m"%eachip
                sitessh.connect("%s" % eachip.strip(), port=22, username="ybop", password=oppass)
	        ssh_stdin, ssh_stdout, ssh_stderr = sitessh.exec_command('sudo /etc/init.d/nginx -t && sudo /etc/init.d/nginx reload',timeout=10,get_pty=True)
                doresult = ''.join(ssh_stdout.readlines()).lower()
                print doresult
                print "\n\t\t\t\033[32m备站%snginx重载成功\033[0m"%eachip
	    except:
	        print("\n\t\t\t\033[0;31;0m ERROR: 备站未给主站授权ssh连接权限,请上服务器添加\033[0m")
    sitessh.close()

def main():
    ###小黄cdncookie
    #xh_cookie = "username='expires=1970-01-08T00:00:00.000Z;value=2847815919@qq.com'; PHPSESSID=d4d410c8e2cf141a35ee22e3f7ef5463"
    ###海啸cdncookie
    haix_cookie = "__cfduid=d182d083bfaa2399aaa1fe21ad318741a1547373550; PHPSESSID=819173da52851203e18a8ced06c89900"
    ###requests会话维持
    sss=requests.session()
    login_header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
    }
    xh_user_ssl = b'Mjg0NzgxNTkxOUBxcS5jb20='
    xh_pass_ssl = b'YXdkMTIzYXdkMTIz'
    xh_user = base64.b64decode(xh_user_ssl).decode('utf-8')
    xh_pass = base64.b64decode(xh_pass_ssl).decode('utf-8')
    login_data={
        'vhostname': xh_user,
        'vhostpasswd': xh_pass 
    }
    open_url = "http://cdn3.01ip.cn/"
    login_url = "http://cdn3.01ip.cn/site/?c=session&a=login"
    aaa = sss.get(open_url)
    login_cookie = aaa.cookies.get_dict()['PHPSESSID']
    xh_cookie = "username='expires=1970-01-08T00:00:00.000Z;value=2847815919@qq.com'; PHPSESSID=%s"% login_cookie
    sss.post(login_url, data=login_data, headers=login_header)
    #token=commands.getoutput('find /opt/apps/nginx/conf/vhosts/ -mindepth 1 -maxdepth 1 -type d -printf "%P\n" |sort -n |egrep -v "*.bak|*.back|tgapp*"|head -1')
    token=commands.getoutput('egrep -o web.javawebdata /opt/apps/nginx/conf/vhosts/* -r | cut -d / -f 7')
    site_url="http://cdn3.01ip.cn/api2/proxy/index.php/vhost/info/%s"%token
    sss.get(site_url, headers=login_header)
    if which_do == 6:
        '''添加海啸cdn'''
	#hx_user_ssl = b'MzI2OTcxNDE3NA=='
	#hx_user = base64.b64decode(hx_user_ssl).decode('utf-8')
	#hx_pass_ssl = b'bXozMjY5NzE0MTc0'
	#hx_pass = base64.b64decode(hx_pass_ssl).decode('utf-8')
	haix_allold_id=haix_all_id(sss,token,haix_cookie)
	haix_need_name=haix_dup_domain(all_name,haix_allold_id)[0]
	haix_already_name=haix_dup_domain(all_name,haix_allold_id)[1]
	if haix_already_name:
	    print("\n\033[32m \t\t\t以下域名已存在于海啸cdn中：%s\033[0m"%(' ').join(haix_already_name))
        zhuip=interative("\n\033[33m\t\t\t域名添加完毕，请输入cdn解析记录：\033[0m","\t\t\t您输入的javazhuip为：")
	haix_cdn_add(sss,token,haix_need_name,zhuip,all_name,haix_cookie)
        sys.exit()
    ### 需要配置的新域名
    new_name_set = interative(' \t\t\t请输入你所有绑定的域名（\033[33m多个域名以空格隔开\033[0m）', " \t\t\t您要绑定的域名为：")
    new_name_cn = new_name_set.strip('\n').split( )
    new_name = list(set(new_name_cn))  ## 去掉list中的重复元素
    admin_duplicat_domains=list(map(lambda x:x,[ i for i in new_name for k in adminnames if i.upper() == k or i.lower() == k]))
    alladmindup=(' ').join(admin_duplicat_domains)
    if admin_duplicat_domains:
        print('\n\033[31m \t\t\t%s是后台域名，不做操作，请找客服确认\033[0m\n'%alladmindup)
    for i in admin_duplicat_domains:
        new_name.pop(new_name.index(i))
    if bool(new_name) is False:
        print('\033[31m \t\t\t没有需要添加的域名，请确认\033[0m')
	sys.exit()
    duplicat_domains=list(map(lambda x:x,[ i for i in new_name for k in all_name if i.upper() == k or i.lower() == k]))
    if duplicat_domains:
        print("\033[31m \n\t\t\t提供的域名有如下重复：%s \033[0m"%(' ').join(duplicat_domains))
        for xin_name in duplicat_domains:
            # 删除重复域名
            upper_name = xin_name.upper() 
            lower_name = xin_name.lower()
	    if '*.' in xin_name:
                os.system("sed -i '/server_name/s/ \+\\'%s'//g' /opt/apps/nginx/conf/vhosts/*.conf /opt/apps/nginx/conf/vhosts/*/*.conf"%(xin_name))
                os.system("sed -i '/server_name/s/ \+\\'%s'//g' /opt/apps/nginx/conf/vhosts/*.conf /opt/apps/nginx/conf/vhosts/*/*.conf"%(upper_name))
                os.system("sed -i '/server_name/s/ \+\\'%s'//g' /opt/apps/nginx/conf/vhosts/*.conf /opt/apps/nginx/conf/vhosts/*/*.conf"%(lower_name))
            else:
                os.system("sed -i '/server_name/s/ \+'%s'//g' /opt/apps/nginx/conf/vhosts/*.conf /opt/apps/nginx/conf/vhosts/*/*.conf"%(xin_name))
                os.system("sed -i '/server_name/s/ \+'%s'//g' /opt/apps/nginx/conf/vhosts/*.conf /opt/apps/nginx/conf/vhosts/*/*.conf"%(upper_name))
                os.system("sed -i '/server_name/s/ \+'%s'//g' /opt/apps/nginx/conf/vhosts/*.conf /opt/apps/nginx/conf/vhosts/*/*.conf"%(lower_name))
	        
	print("\033[31m \t\t\t%s已从服务器上删除\033[0m"%(' ').join(duplicat_domains))
    ## 如果重复域名删掉了，server_name 都为空的conf文件也删掉
    empty_server_file = commands.getoutput('egrep "server_name\ *;" /opt/apps/nginx/conf/vhosts/*/*.conf |awk -F":" "{print \$1}"').split('\n')
    if empty_server_file:
        for i in empty_server_file:
            os.system('rm -f %s'%(i))
    ### 针对选择做相关操作：
    if which_do == 1:
        ''''添加前台域名'''
        ## 获取增加域名的配置文件 
        source_file = commands.getoutput('egrep "web.javawebdata5.com" /opt/apps/nginx/conf/vhosts/*/*.conf |awk -F":" "{print \$1}"')
        print '\033[32m \n\t\t\tweb前台域名添加中.....\033[0m'
        for N in new_name:
            add_name(N,source_file)
	#zhuip=raw_input("\n\033[33m\t\t\t前台非证书域名添加完毕，请输入cdn解析记录：\033[0m")
	zhuip=interative("\n\033[33m\t\t\t前台证书域名添加完毕，请输入cdn解析记录：\033[0m","\t\t\t您输入的javazhuip为：")
	crt_file=''
	key_file=''
	add_cdn_url(sss,token,xh_cookie,new_name,zhuip,which_do,crt_file,key_file)
    if which_do == 2:
        '''添加前台证书域名'''
        ## 获取证书文件路径
        crt_file = interative(' \t\t\t请输入证书的crt文件的绝对路径：', ' \t\t\t您输入的crt文件路径为：')
        key_file = interative(' \t\t\t请输入证书的key文件的绝对路径：', ' \t\t\t您输入的key文件路径为：')
        ## 获取证书域名文件的源文件
        crt_source_file = commands.getoutput('egrep "tgapp" /opt/apps/nginx/conf/vhosts/* -r |awk -F":" "{print \$1}"').split('\n')[0]
        ## 配置证书文件
        print '\n\033[32m \t\t\t前台证书域名添加中.....\033[0m'
        add_crt(crt_source_file,new_name, crt_file, key_file, token)
	zhuip=interative("\n\033[33m\t\t\t前台证书域名添加完毕，请输入cdn解析记录：\033[0m","\t\t\t您输入的javazhuip为：")
	#zhuip=raw_input("\n\033[33m\t\t\t前台证书域名添加完毕，请输入cdn解析记录：\033[0m")
	add_cdn_url(sss,token,xh_cookie,new_name,zhuip,which_do,crt_file,key_file)
    if which_do == 3:
        ''''添加admin后台域名'''
        admin_source_file = commands.getoutput('egrep "admin.online8828.com" /opt/apps/nginx/conf/vhosts/*/*.conf |awk -F":" "{print \$1}"')
        print '\n\033[32m \t\t\tadmin后台域名添加中.....\033[0m'
        for A in new_name:
            add_name(A,admin_source_file)
    if which_do == 4:
        ''''添加cms后台域名'''
        cms_source_file = commands.getoutput('egrep "cms.online8828.com" /opt/apps/nginx/conf/vhosts/*/*.conf |awk -F":" "{print \$1}"')
        print '\n\033[32m \t\t\tcms后台域名添加中.....\033[0m'
        for C in new_name:
            add_name(C,cms_source_file)
    if which_do == 5:
        ''''添加agent后台域名'''
        agent_source_file = commands.getoutput('egrep "agent.online8828.com" /opt/apps/nginx/conf/vhosts/*/*.conf |awk -F":" "{print \$1}"')
        print '\n\033[32m \t\t\tagent后台域名添加中.....\033[0m'
        for G in new_name:
            add_name(G,agent_source_file)
    nginx_reload()
if __name__ == '__main__':
    main()
