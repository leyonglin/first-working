#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os
import sys
import commands


######## base env
### path
scripts_path=os.path.split(os.path.realpath(__file__))[0]
ngx_conf='/opt/apps/nginx/conf/nginx.conf'
rsync_nginx_conf='/opt/apps/nginx/conf'
token=commands.getoutput("egrep 'vhosts/([a-Z]|[0-9])' %s  |egrep -v tgapp |awk -F'/' '{print $2}'"%(ngx_conf))
front_back_path='/opt/backup'                                  # backup directory of web
db_backup_path='/backup/data_back'                               # backup directory of db
webapss_version_path='/opt/backup/webapps_version_record'
http_default_file='/opt/apps/nginx/conf/vhosts/http_default_server.conf'
https_default_file='/opt/apps/nginx/conf/vhosts/https_default_server.conf'
tomcat_install_path='/opt/apps/tomcat'			       # tom家目录
rsync_log_path='/opt/apps/rsync/logs/'
rsync_pass_file='/opt/scripts/.rsyncd.passwd'
rsync_secret_file='/opt/apps/rsync/etc/rsyncd.secret'
rsync_conf='/opt/apps/rsync/etc/rsyncd.conf'
rsync_pass='WIxii20OhL1qM5q93MeASh4sSrdzCzfGrxWXtoXRLvq9s7cFFQMJtUdgiPIHPB4R'
web_log_path='/opt/logs/'                                      
ybweb_need_write_path=[
'/opt/webapps/admin_7001/data/',
'/opt/webapps/admin_7001/temp',
'/opt/webapps/cms_9001/views/',
'/opt/webapps/web_8001/data/',
'/opt/webapps/web_8001/views/',
'/opt/webapps/cms_9001/WEB-INF/classes/template',
'/opt/webapps/live_work_9002/temp',
#'/opt/webapps/admin_7001/exportData'
]
data_dir='/opt/data/'
webapps_dir='/opt/webapps/'
ngx_cache_dir='/opt/apps/nginx/tmp'
### upload directory 
upload_path='/opt/src/upload'
db_upload_path='/opt/src/db_upload'
code_rollback='code_rollback'
cront_file=['ybop']                               ## only for ybop
dataviews_back_dir='/opt/backup/data_views_nginx' ## data views and nginx connf backup
### service init scripts
web_init_service=['nginx', 'rsyncd', 'sersync_data', 'sersync_nginx', 'sersync_views', 'tomcat_7001', 'tomcat_7002', 'tomcat_7003', 'tomcat_8001', 'tomcat_8002', 'tomcat_8003', 'tomcat_9001', 'tomcat_9002']
db_init_service=['mysqld', 'redis']
### users
# infos of all users
all_user_infos={
	'super_user': {'name': 'swadmin', 'pass': 'Passw0rd!**yiboswadmin'},
	'java_user': {'name': 'blog'},
	'op_user':{'name': 'ybop', 'pass': 'Passw0rdop'}, 
	'deploy_user':{'name': 'ybdeploy', 'pass': 'Passw0rddeploy'},
	'web_user':{'name': 'ybweb', 'pass': ''},         # no login authority
	'db_user':{'name': 'ybdb', 'pass': ''},           # no login authority
}
ngx_dir_user = all_user_infos['super_user']['name']
super_user = all_user_infos['super_user']['name']
super_user_pass = all_user_infos['super_user']['pass']
op_user = all_user_infos['op_user']['name']
deploy_user = all_user_infos['deploy_user']['name']
web_process_user = all_user_infos['web_user']['name']
db_process_user = all_user_infos['db_user']['name']
can_su_user_list = [all_user_infos['super_user']['name']]
# members of dataviews group, which own the authority of ybweb_need_write_path 
webgroups='dataviews'
webgroups_menmbers=[all_user_infos['web_user']['name'], all_user_infos['deploy_user']['name'], all_user_infos['super_user']['name']]
# menbers of ybdb group, which own the authority of rx of data_16303
dbgroups=all_user_infos['db_user']['name']
dbgroups_menmbers=[ all_user_infos['op_user']['name'], all_user_infos['java_user']['name'], all_user_infos['super_user']['name'] ]
### nginx's cache setting
ngx_conf_modify=['client_body_temp_path', 'proxy_temp_path', 'fastcgi_temp_path', 'uwsgi_temp_path', 'scgi_temp_path', 'user %s'%(web_process_user)]
### modify token of template of sudo files
os.system('sed -i \'s#virtest#%s#g\' %s/sudo_file/*'%(token, scripts_path))
### reserveed ports
save_ports='80,443,1873,16303,17693,7001,17005,7009,8443,8080,7002,17006,7010,7003,17007,7011,8001,18005,8009,8002,8006,8010,8003,18007,8011,9001,19005,9009,9002,9035,9012'
### prohibit authority of no-root user for installing
jin_install=['/usr/bin/rpm', '/usr/bin/make']
### deploy backup path
web_backup_path='/opt/backup'
### deploy get authority of rsync
need_rsync_file_auth = ['/opt/scripts/.rsyncd.passwd', '/opt/apps/rsync/etc/*', '/opt/apps/rsync/logs/*']
### template file of ybop's bashrc, which set alias of operation
ybop_barsh='other_templat_file/ybop_bashrc'
### home path of all tomcat applications
all_tom_root_path=[
'/opt/apps/tomcat/tomcat_7001',
'/opt/apps/tomcat/tomcat_7002',
'/opt/apps/tomcat/tomcat_7003',
'/opt/apps/tomcat/tomcat_8001',
'/opt/apps/tomcat/tomcat_8003',
'/opt/apps/tomcat/tomcat_9001',
'/opt/apps/tomcat/tomcat_9002'
]
### autority of tomcat specified path, which ybweb need
open_tomcat_chrdir = ['temp', 'work']
### get structure of site
while True:
    print("\033[36m \t\t\t+---------------------------------------+\t\t\t \033[0m")
    print("\033[36m \t\t\t|      请选择您要升级的站点架构类型     |\t\t\t \033[0m")
    print("\033[36m \t\t\t+---------------------------------------+\t\t\t \033[0m")
    print("\033[36m \t\t\t| (1) 升级主站主库-两台                 |\t\t\t \033[0m")
    print("\033[36m \t\t\t| (2) 升级备站备库-两台                 |\t\t\t \033[0m")
    print("\033[36m \t\t\t| (3) 升级主站-四台                     |\t\t\t \033[0m")
    print("\033[36m \t\t\t| (4) 升级备站-四台                     |\t\t\t \033[0m")
    print("\033[36m \t\t\t| (5) 升级主库-四台                     |\t\t\t \033[0m")
    print("\033[36m \t\t\t| (6) 升级备库-四台                     |\t\t\t \033[0m")
    print("\033[36m \t\t\t+---------------------------------------+\t\t\t \033[0m")
    chose = raw_input("\033[36m \t\t\t： \033[0m")
    if chose in ['1', '3']:
        while True:
            back_site_ip  = raw_input("\033[36m \t\t\t请输入web备站的IP： \033[0m").strip()
            confirm_backsite_ip = raw_input("\033[36m \t\t\tweb备站的IP为 %s 请确认（yes/no)   \033[0m"%(back_site_ip))
            if confirm_backsite_ip in ['yes', 'YES', 'y', 'Y', 'Yes']:
                break
            else:
                continue
        ## set back_site_ip of ybop'cron
        os.system('sed -i \'s#{{back_site_ip}}#%s#g\' %s/cront_file/*'%(back_site_ip, scripts_path))
        break
    if chose in ['2', '4', '5', '6']:
        break
    else:
        print("\033[31m \t\t\t请选择正确的类型 \033[0m")
        continue

def create_user_group():
    ## create common user for op -- ybop
    op_user_name=all_user_infos['op_user']['name']
    op_user_pass=all_user_infos['op_user']['pass']
    user_check = commands.getoutput('id %s'%(op_user_name))
    if 'no such user' in user_check:
        os.system('useradd %s'%(op_user_name))
    else:
        print('\033[31m%s exists\033[0m'%(op_user_name))
    os.system("echo %s |passwd --stdin %s"%(op_user_pass, op_user_name))
    if chose in ['1', '2',  '3', '4']:
        # web user -- no login  
        web_user_name=all_user_infos['web_user']['name']
        web_user_pass=all_user_infos['web_user']['pass']
        user_check = commands.getoutput('id %s'%(web_user_name))
        if 'no such user' in user_check:
            os.system('useradd -M -s /sbin/nologin %s'%(web_user_name))
        else:
            print('\033[31m%s exists\033[0m'%(web_user_name))
        # deploy user -- ssh connecting user of jenkins
        deploy_user_name=all_user_infos['deploy_user']['name']
        deploy_user_pass=all_user_infos['deploy_user']['pass']
        user_check = commands.getoutput('id %s'%(deploy_user_name))
        if 'no such user' in user_check:
            os.system('useradd %s'%(deploy_user_name))
        else:
            print('\033[31m%s exists\033[0m'%(deploy_user_name))
        os.system("echo %s |passwd --stdin %s"%(deploy_user_pass, deploy_user_name))
        # create webgroups group and add menbers
        os.system('groupadd %s'%(webgroups))
        for i in webgroups_menmbers:
            os.system('/sbin/usermod -a -G %s %s'%(webgroups, i))
    if chose in ['1', '2', '5', '6']:
        # db user -- no login  
        db_user_name=all_user_infos['db_user']['name']
        db_user_pass=all_user_infos['db_user']['pass']
        user_check = commands.getoutput('id %s'%(db_user_name))
        if 'no such user' in user_check:
            os.system('useradd -M -s /sbin/nologin %s'%(db_user_name))
        else:
            print('\033[31m%s exists\033[0m'%(db_user_name))
        # add menbers of ybdb group
        for i in dbgroups_menmbers:
            os.system('/sbin/usermod -a -G %s %s'%(dbgroups, i))        

def sudo_auth():
    os.system('cp %s/sudo_file/mtadmin /etc/sudoers.d/'%(scripts_path))
    if chose in ['1', '2', '3', '4']:
        os.system('cp %s/sudo_file/ybdeploy /etc/sudoers.d/'%(scripts_path))
        os.system('cp %s/sudo_file/ybop /etc/sudoers.d/ybop'%(scripts_path))
    if chose in ['5', '6']:
        os.system('cp %s/sudo_file/db_ybop /etc/sudoers.d/ybop'%(scripts_path))
    ## delete sudo config of swadmin && ybadmin
    for i in ['swadmin', 'ybadmin']:
        if os.path.exists('/etc/sudoers.d/%s'%(i)):
            os.system('rm -f /etc/sudoers.d/%s'%(i))
    ## chmod 0440 
    os.system('chmod 0440 /etc/sudoers.d/*')
    ## check config
    sudo_check = commands.getoutput('visudo -c')
    if 'error' in sudo_check:
        print('\n\033[31msudo配置有问题,请检查!!!\033[0m\n')
        sys.exit()

def common_set():
    # ports reserved
    ports_check = commands.getoutput('egrep net.ipv4.ip_local_reserved_ports /etc/sysctl.conf')
    if not ports_check:
        os.system("sed -i '$anet.ipv4.ip_local_reserved_ports=%s' /etc/sysctl.conf"%(save_ports))
        os.system('sysctl -p')
    # su authority
    for i in can_su_user_list:
        os.system('/sbin/usermod -a -G wheel %s'%(i))
    check_swadmin_su = commands.getoutput('id %s |egrep wheel'%(can_su_user_list[0]))
    if check_swadmin_su:
        os.system('cp -a /etc/pam.d/su{,.default}')
        os.system("sed -i '/required/s#.*#auth           required        pam_wheel.so use_uid#g' /etc/pam.d/su")
        os.system('cp -a /etc/login.defs{,.default}')
        su_wheel_check=commands.getoutput('egrep "SU_WHEEL_ONLY" /etc/login.defs')
        if not su_wheel_check:
            os.system("sed -i '$aSU_WHEEL_ONLY yes' /etc/login.defs")


def modify_nginx():
    if chose in ['1', '2', '3', '4']:
        # modify configurations of nginx
        os.system('su %s -c "sed -i \"s/error_log/#error_log/g\" %s\"'%(ngx_dir_user,http_default_file))
        os.system('su %s -c "sed -i \"s/error_log/#error_log/g\" %s\"'%(ngx_dir_user,https_default_file))
        # delete old temp directories
        os.system('cd /opt/apps/nginx/ && rm -rf client_body_temp fastcgi_temp proxy_temp scgi_temp uwsgi_temp')
        # set nginx cache path, which need to give writing authority to ybweb
        if not os.path.exists(ngx_cache_dir):
            os.system('mkdir -p %s'%(ngx_cache_dir))
        os.system('chown -R %s:%s %s'%(web_process_user, web_process_user, ngx_cache_dir))
        with open(ngx_conf, 'r') as f:
            ngx_context=f.read()
        os.system("su %s -c 'cp %s %s_backup'"%(ngx_dir_user, ngx_conf, ngx_conf))
        for line in ngx_context.split('\\n'):
            for new_line in ngx_conf_modify:
                if new_line not in line:
                    if 'user' in new_line:
                        # specify work process user
                        os.system('sed -i "1auser %s;" %s'%(web_process_user, ngx_conf))
                    else:
                        set_path='%s/%s'%(ngx_cache_dir, new_line.replace('_path', ''))
                        os.system('sed -i \"/charset/a\    %s  %s;\" %s'%(new_line, set_path, ngx_conf))
def add_domains_script():
    if chose in ['1', '2', '3', '4']:
        os.system('cp %s/start_service_file/add_domains.py /opt/scripts/'%(scripts_path))
        os.system('chown %s.%s /opt/scripts/add_domains.py'%(super_user, super_user))

def modify_rsync():
    if chose in ['1', '2', '3', '4']:
        ## modify configure of rsync
        # set uid and gid of rsync
        os.system("sed -r -i '/(uid|gid)/d' %s"%(rsync_conf))
        os.system('sed -i "1iuid = root\\ngid = root" %s'%(rsync_conf))
        # give  pass and secret files to root  
        os.system("chown root.root %s %s"%(rsync_pass_file, rsync_secret_file))
        # update pass
        os.system('echo %s > %s'%(rsync_pass, rsync_pass_file))
        os.system('echo "rsync:%s" > %s'%(rsync_pass, rsync_secret_file))


def modify_files_authority():
    # remove authority of some tools, su as npm , make
    # save superuser'authority of jin_install
    for i in jin_install:
        os.system('chmod o-x %s'%(i))
        os.system('setfacl -m u:%s:x %s'%(super_user,i)) 

    if chose in ['1', '2', '3', '4', '5', '6']:
        # create upload directory
        if not os.path.exists('%s'%(upload_path)):
            os.system('mkdir %s'%(upload_path))
        os.system('chown -R %s:%s %s'%(super_user, super_user, upload_path))
        os.system('setfacl -R  -m u:%s:rwx %s'%(op_user, upload_path))
        os.system('chmod -R g+s %s'%(upload_path))
    if chose in ['1', '2', '5', '6']:
        ## web server
        ## create upload directory for db
        if not os.path.exists(db_upload_path):
            os.system('mkdir %s'%(db_upload_path))
        os.system('chown -R %s:%s %s'%(db_process_user, db_process_user,db_upload_path))
        os.system('chmod 775 %s'%(db_upload_path))
        os.system('chmod g+s %s'%(db_upload_path))
        # mysql & redis 
        os.system('chown -R %s:%s %s'%(db_process_user, db_process_user, data_dir))
        # ybdb get authority of scripts for backup mysql
        sql_backup_scripts='/opt/scripts/mysqlback.sh'
        if os.path.exists(sql_backup_scripts):
            os.system('chown ybdb.ybdb %s'%(sql_backup_scripts))
            os.system('chmod 644 %s'%(sql_backup_scripts))
        # give authority of mysql backup to ybdb
        if not os.path.exists(db_backup_path):
            os.system('mkdir -p %s'%(db_backup_path))
        os.system('chown -R %s.%s %s'%(db_process_user, db_process_user, db_backup_path))

    if chose in ['1', '2', '3', '4']:
        ## db server
        ## create data views nginx conf backup diretory 
        if not os.path.exists(dataviews_back_dir):
            os.system('mkdir -p %s'%(dataviews_back_dir))
        os.system('chown -R %s:%s %s'%(deploy_user, super_user, dataviews_back_dir))
        os.system('chmod g+s %s'%(dataviews_back_dir))
        ## create webapps version records
        if not os.path.exists(webapss_version_path):
            os.system('mkdir %s'%(webapss_version_path))
        ## mv old code to /opt/backup/webapps_version_record
        os.system('chown -R %s:%s %s'%(deploy_user,deploy_user,webapss_version_path))
        os.system('mv /opt/backup/*.zip %s'%(webapss_version_path))
        os.system('setfacl -m u:%s:rw %s/*'%(super_user, webapss_version_path))
        # path of logs of tomcat nginx sersync: u:ybweb,g:ybweb  && ybop Acl d:rwx f:rw 
        os.system('chown -R %s:%s %s'%(web_process_user, web_process_user, web_log_path))
        os.system('find %s -type d |xargs setfacl -m u:%s:rwx'%( web_log_path, op_user))
        old_log_file=commands.getoutput('find %s -type f'%( web_log_path))
        if old_log_file:
            for i in old_log_file.split('\n'):
                os.system('setfacl -m u:%s:rw %s'%(op_user, i))
        os.system('find %s -type f |xargs setfacl -m u:%s:rw'%( web_log_path, op_user))
        # tomcat server.conf  
        os.system('for i in %s/*; do setfacl -R -m u:%s:rx $i/conf/*;done'%(tomcat_install_path, web_process_user))
        ## give authority of webapps directory to deploy user
        os.system('chown -R %s:%s %s'%(deploy_user, deploy_user, webapps_dir))
        ## swadmin get authority of rsync
        for i in need_rsync_file_auth:
             os.system('setfacl -m u:%s:r %s'%(super_user, i))
             os.system('setfacl -m u:%s:r %s'%(deploy_user, i))
        ## copy backup_web_service 
        os.system('cp %s/backup_scripts/backup_web_service.sh /opt/scripts'%(scripts_path))	
        os.system('chown %s:%s /opt/scripts/backup_web_service.sh'%(super_user,super_user))
        os.system('chmod 644 /opt/scripts/backup_web_service.sh')
        # git autority of (hk|kr)webback.sh to ybdeploy
        os.system('chown %s.%s /opt/scripts/*webback.sh'%(deploy_user,deploy_user))
        os.system('chmod 644  /opt/scripts/*webback.sh')
        # ybdeploy get authority of /opt/backup
        os.system('setfacl -m u:%s:rwx %s'%(deploy_user, web_backup_path))
        # ybweb get authority of backup dir of log, nginx_path 
        os.system('chown -R %s.%s %s'%(web_process_user,web_process_user, web_log_path))
        # create directory of ngix backup, logs cutting, webapps backup, and set autority
        if not os.path.exists('%s/log_bak/'%(front_back_path)):
            os.system('mkdir -p %s/log_bak/{tomcat,nginx}'%(front_back_path))
        if not os.path.exists('%s/apps_bak/'%(front_back_path)):
            os.system('mkdir -p %s/apps_bak/'%(front_back_path))
        if not os.path.exists('%s/webapps_bak/'%(front_back_path)):
            os.system('mkdir -p %s/webapps_bak/'%(front_back_path))
        os.system('chown -R %s.%s %s/apps_bak/'%(super_user,super_user,front_back_path))
        os.system('chown -R %s.%s %s/log_bak/'%(web_process_user,web_process_user,front_back_path))
        os.system('chown -R %s.%s %s/webapps_bak/'%(deploy_user,deploy_user,front_back_path))
        # give rw autority of all_tom_root_path to ybweb,
        for i in all_tom_root_path:
            tom_rootdir = i # home path of tomcat
            for one in open_tomcat_chrdir:
                tom_chrdir = one # child path of home path of tomcat
                os.system('setfacl -R -m u:%s:rwx %s/%s'%(web_process_user, tom_rootdir, tom_chrdir))
        # set 644 authority of log path
        os.system('for i in `find %s -type f`;do chmod 644 $i;done'%(web_log_path))


def add_cron():
    ## mv old users'cron ,such as swadmin, ybadmin
    for i in ['swadmin', 'ybadmin']:
        if os.path.exists('/var/spool/cron/%s'%(i)):
            os.system('rm -f /var/spool/cron/%s'%(i))
    ## add new users'cron
    if chose in ['1']:
       os.system('cp %s/cront_file/web_db_master_%s /var/spool/cron/%s'%(scripts_path, op_user,op_user))
    if chose in ['2','4']:
       os.system('cp %s/cront_file/web_slave_%s /var/spool/cron/%s'%(scripts_path, op_user,op_user))
    if chose in ['3']:
       os.system('cp %s/cront_file/web_master_%s /var/spool/cron/%s'%(scripts_path, op_user,op_user))
    if chose in ['5']:
       os.system('cp %s/cront_file/db_master_%s /var/spool/cron/%s'%(scripts_path, op_user,op_user))
    if chose not in ['6']:
        ## flush privileges of ybop crontab
        os.system('chown %s:%s /var/spool/cron/%s'%(op_user,op_user,op_user))
        os.system('chmod 600 /var/spool/cron/%s'%(op_user))

def start_service():
    if chose in ['1','2','3','4']:
        ## copy web service init scripts
        for i in web_init_service:
            os.system('cp %s/start_service_file/%s /etc/init.d/'%(scripts_path, i))
            os.system('chmod 700 /etc/init.d/%s'%(i))
            os.system('setfacl -m u:%s:r /etc/init.d/%s'%(super_user, i))
            os.system('setfacl -m u:%s:r /etc/init.d/%s'%(op_user, i))
        ## copy code rollback script
        os.system('cp %s/start_service_file/%s /etc/init.d/'%(scripts_path, code_rollback))
        os.system('chown %s.%s /etc/init.d/%s'%(deploy_user,deploy_user,code_rollback))
        os.system('chmod 700 /etc/init.d/%s'%(code_rollback))
        os.system('setfacl -m u:%s:r /etc/init.d/%s'%(super_user, code_rollback))
        os.system('setfacl -m u:%s:r /etc/init.d/%s'%(op_user, code_rollback))
    if chose in ['1','2','5','6']:
        ## copy db service init scripts
        for i in db_init_service:
            os.system('cp %s/start_service_file/%s /etc/init.d/'%(scripts_path, i))
            os.system('chmod 700 /etc/init.d/%s'%(i))
            os.system('setfacl -m u:%s:r /etc/init.d/%s'%(super_user, i))
            os.system('setfacl -m u:%s:r /etc/init.d/%s'%(op_user, i))
        
def operate_dir(directory):
    '''do setgid for specified directories'''
    os.system('chmod g+s %s'%(directory))
    fs=os.listdir(directory)
    for f1 in fs:
        tmp_path = os.path.join(directory,f1)
        if os.path.isdir(tmp_path):
            os.system('chmod g+s %s'%(tmp_path))
            operate_dir(tmp_path)

def traverse(f):
    '''set authority, dirctory -- 775 && file -- 664, for specified path and child path'''
    os.system('chmod -R 664 %s'%(f))
    all_dir=commands.getoutput('find %s -type d'%(f)).split('\n')
    for i in all_dir:
        os.system('chmod g+s "%s"'%(i))
        os.system('chmod 775 "%s"'%(i))
    
def main():
    ## create user and group
    create_user_group()
    ### sudo settings
    sudo_auth()
    ## common settings: ports reserverd, su athority only for supper user,
    common_set()
    ## modify nginx'temp path
    modify_nginx()
    ## modify authority of specified files
    modify_files_authority()
    ## add cron
    add_cron()
    ## copy service init scripts 
    start_service()
    ## annotate redis save of db servers
    if chose in ['1','2','5','6']:
         os.system("sed -r -i 's/^ *save/#save/g' /opt/conf/re*.conf")
    ## set alias
    os.system('cp -f %s/%s /home/%s/.bashrc'%(scripts_path, ybop_barsh, op_user))
    os.system('chown %s.%s /home/%s/.bashrc'%(op_user, op_user, op_user))
    ## set directory:775 and file:664 for webapps path
    if chose in ['1','2','3','4']:
        traverse(webapps_dir)
    ## delete ybadmin 
    os.system('userdel -r  ybadmin')
    ## transfer  add doamins scripts 
    add_domains_script()
    # set authority of data and views and its child path
    #  u:ybdeploy g:dataviews
    #  set gid for all dirctories of webapps
    if chose in ['1','2','3','4']:
        for i in ybweb_need_write_path:
            if os.path.exists(i):
                ## put directories into daivews group
                os.system('chown -R %s:dataviews %s'%(deploy_user,i))
                ## set gid 
                operate_dir(i)
            else:
                print('\n\033[31m 目录%s 不存在\033[0m\n'%(i))
        # 传送libaes.so文件
        print('传送libaes.so文件到前后台服务器')
        os.system('cp %s/libaes.so /opt/apps'%(scripts_path))
        os.system('chown swadmin.swadmin /opt/apps/libaes.so')
        os.system('chmod 444 /opt/apps/libaes.so')
        # 启动scan_file.py文件
        scanProcess=commands.getoutput("ps -ef |egrep scan_file.py |egrep -v grep |awk '{print $2}'")
        if not scanProcess:
            os.system('python /opt/scripts/scan_file.py &')
        # 安装pip、request、paramiko
        print('先给前后台服务器安装域名添加脚本所需的模块，请稍后\n')
        os.system('yum -y install epel-release')
        os.system('yum -y install python-pip')
        os.system('pip install --upgrade pip')
        os.system('pip install paramiko')
        os.system('pip install requests')
    # modify rsync
    modify_rsync()
    # delete old backup scritpts
    for i in ['/opt/scripts/CUT_NGLOG.sh', '/opt/scripts/CUT_TOMCAT.sh', '/opt/scripts/GEO_UPDATE.sh', '/opt/scripts/nginx_back.sh', '/opt/scripts/webapps_back.sh']:
        if os.path.exists(i):
            os.system('rm -f %s'%(i))
    # init password of swadmin;
    # 将nginx的conf目录开放给ybop
    os.system('for i in `find /opt/apps/nginx/conf/ -type d`;do chmod g+s $i && setfacl -m u:ybop:rwx $i;done')
    os.system('for i in `find /opt/apps/nginx/conf/ -type f`;do setfacl -m u:ybop:rw $i;done')
    if super_user_pass:
        os.system("echo %s |passwd --stdin %s"%(super_user_pass, super_user))

        

if  __name__ == '__main__':
    main()
        
   
