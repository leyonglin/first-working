#!/bin/bash
# author star
# release version v1.34

#######################global variable parameters#################################
#http auth
current_dir=`pwd`
version=v1.34
http_user="downloader"
http_password="bytVi_iFD__foXZl2PpkpdH3iWgm0dcf"
#define white ip list for firewall
office_ip=113.61.35.0/24
analysis_hk=119.28.63.97
analysis_kr=103.68.110.32
jenkins_kr_masterip=154.223.1.160  #2018-12-28
jenkins_kr_secondip=154.223.1.160  #2018-12-28
jenkins2_kr_masterip=103.116.132.35 #2018-12-28
jenkins2_kr_secondip=103.116.132.36  #2018-12-28
jenkins3_kr_masterip=103.113.9.80
jenkins3_kr_secondip=14.192.67.101
jenkins4_kr_masterip=103.116.132.96  #2018-12-28
jenkins4_kr_secondip=103.116.132.96  #2018-12-28
jenkins5_kr=103.116.133.106 #2019-03-06
jenkins6_kr=103.116.133.100 #2019-03-06
jenkins7_kr=103.86.87.142 #2019-03-06
jenkins8_kr=103.116.132.96 #2019-03-06

jenkins1_hk=103.35.118.19
jenkins2_hk=103.23.46.151
jenkins3_hk=103.15.105.103 #2019-03-06
jenkins4_hk=103.15.106.69 #2019-03-06

zabbix_kr_server_slave=103.86.87.140
zabbix_kr_server_master=103.86.85.91
zabbix_hk_proxy=103.229.146.31
zabbix_kr_proxy=154.223.1.29
downloadserver_hk=hkdownload.zhushuqt.com:8443/download
downloadserver_kr=krdownload.zhushuqt.com:8443/download
#zabbix_server=103.86.85.239

#define default ip address and user list
#default_ip=`ip -4 a| egrep -o "([0-9]{1,3}.){3}[0-9]{1,3}" | head -2 | tail -1`
multi_default_ip=`hostname -I`
default_ip=`hostname -I | awk '{print $1}'`
default_user_list='swadmin ybadmin mtadmin blog'

###############################function overview##################################
#common_list_sys_info
#common_optimize_kernel
#common_check_net_adapter
#common_set_sudo_su_alias
#common_disable_selinux
#common_hiden_sys_issue
#common_set_sshd_service
#common_set_ntp_crontab
#common_add_user
#common_print_success

#add_web_name
#add_web_analysis_ip
#add_web_slave_ip
#add_web_master_ip
#add_web_master_slave_ip
#add_db_master_slave_ip
#add_db_slave_ip
#add_db_master_ip
#add_db_slave_master_ip
#add_web_db_master_slave_ip
#add_web_db_slave_master_ip
#add_test_web_ip
#add_webapps_env_parameters
#add_db_env_parameters
#add_web_db_env_parameters


#create_webapps_directory
#create_db_master_directory
#create_db_slave_directory

#get_webapps_scripts
#get_db_scripts

#set_web_master_firewall
#set_web_slave_firewall
#set_db_master_firewall
#set_db_slave_firewall
#set_web_rsync
#set_web_sersync
#set_web_master_crontab
#set_web_slave_crontab
#set_mysql_master_crontab

#install_web_basic_package
#install_db_basic_package
#install_geoip_nginx
#install_tomcat
#install_rsync
#install_sersync
#install_master_mysql
#install_slave_mysql
#install_master_redis
#install_slave_redis

#install_db_master_zabbix
#install_db_slave_zabbix
#install_web_master_zabbix
#install_web_slave_zabbix
#install_web_db_master_zabbix
#install_web_db_slave_zabbix
#run_scan_file_as_daemon
#grant_mysql_master_privileges
#init_db_trigger
#grant_mysql_slave_replication




##############################define function start###############################
common_list_sys_info () {
    dmidecode | egrep -i 'manufacturer|product|vendor|system'
    sleep 0.1
    lscpu
    sleep 0.1
    hostnamectl
    sleep 0.1
    ip -4 a
    sleep 0.1
    timedatectl 
    sleep 0.1
    df -hT
    read -p 'make sure your system time and disk partition are correctly. save the system information? default path save to /root/system.info. [y/n]  ' info
    if [ "$info" == 'y' ] || [ "$info" == 'Y' ];then
        lscpu >> /root/system.info
        df -hT >> /root/system.info
        hostnamectl >> /root/system.info
        ip -4 a >> /root/system.info
        dmidecode | egrep -i 'manufacturer|product|vendor|system' >> /root/system.info
    fi
}

common_optimize_kernel () {
    echo -e "\033[36m \t\t\t 优化系统内核  \t\t\t  \033[0m"
    grep 'keepalive_time = 12000' /etc/sysctl.conf
    if [ $? -ne 0 ];then
        sed -i "/^[^#]/d" /etc/sysctl.conf
        echo 'fs.file-max = 65535
net.ipv4.ip_forward = 1
net.ipv4.tcp_fin_timeout = 600
net.ipv4.tcp_max_syn_backlog = 10240 
net.ipv4.tcp_keepalive_time = 12000
net.ipv4.tcp_synack_retries = 3
net.ipv4.tcp_syn_retries = 3
net.ipv4.tcp_max_orphans = 8192
net.ipv4.tcp_max_tw_buckets = 2000 
net.ipv4.tcp_window_scaling = 0
net.ipv4.tcp_sack = 0
net.ipv4.tcp_timestamps = 0
net.ipv4.tcp_syncookies = 1 
net.ipv4.tcp_tw_reuse = 1 
net.ipv4.tcp_tw_recycle = 1 
net.ipv4.ip_local_port_range = 1024 65000
net.ipv4.icmp_echo_ignore_all = 1
net.core.somaxconn= 1024
vm.overcommit_memory=1
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.icmp_echo_ignore_all = 1
net.ipv4.ip_default_ttl = 128
net.ipv4.conf.all.accept_redirects = 0' >> /etc/sysctl.conf 
    fi
    sysctl -p 
    sleep 1

    grep '* soft nproc 65535' /etc/security/limits.conf
    if [ $? -ne 0 ];then
        echo '* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535' >> /etc/security/limits.conf
    fi
    rc_local=`grep /var/lock/subsys/local /etc/rc.local`
    [ -z "$rc_local" ] &&  sed -i '$atouch /var/lock/subsys/local' /etc/rc.local
    sleep 1
}

common_check_net_adapter () {
    for net in `ls /etc/sysconfig/network-scripts/ifcfg*`
    do
        sed -i '/ONBOOT/s/no/yes/' $net
    done
    grep   "ONBOOT" /etc/sysconfig/network-scripts/ifcfg* 
    sleep 1
}

common_set_sudo_su_alias () {
    echo '#########NGINX###############
swadmin ALL=NOPASSWD:/opt/apps/nginx/sbin/nginx' > /etc/sudoers.d/swadmin
    chmod 600 /etc/sudoers.d/swadmin
    echo '######别名##########
Cmnd_Alias SCRIPTS_COMMAND = /usr/bin/yum, /usr/bin/mv, /usr/bin/firewall-cmd, /usr/bin/tar, /usr/bin/zip, /usr/bin/unzip, /usr/bin/gunzip, /usr/bin/wget, /usr/bin/bash /opt/scripts/*, /bin/bash /opt/*, /usr/bin/mkdir /opt/*, /usr/bin/touch /opt/*,/usr/bin/rm -r /opt/*,/usr/bin/rm  /opt/*
######备份脚本#######
ybadmin ALL=(ALL)NOPASSWD:SCRIPTS_COMMAND' > /etc/sudoers.d/ybadmin
    chmod 600 /etc/sudoers.d/ybadmin
    grep 'alias su="su -"' /etc/bashrc &> /dev/null
    if [ $? -ne 0 ];then
        echo -e "\033[36m \t\t\t set su and alias  \t\t\t  \033[0m"
        sed -i '2a alias su="su -"' /etc/bashrc
    fi
}

common_disable_selinux () {
    sed -i '/^SELINUX=/s/.*/SELINUX=disabled/' /etc/selinux/config
    setenforce 0
}

common_hiden_sys_issue () {
    mv /etc/issue /etc/system.bak
    mv /etc/issue.net /etc/system.netbak
}

common_set_sshd_service () {
    grep 'PermitRootLogin no' /etc/ssh/sshd_config &> /dev/null
    if [ $? -ne 0 ];then
        sed -i '38a PermitRootLogin no ' /etc/ssh/sshd_config
        sed -i '38a UseDNS no ' /etc/ssh/sshd_config
        sed -i '38a MaxAuthTries 3' /etc/ssh/sshd_config
    fi
    systemctl restart sshd
}

common_set_ntp_crontab () {
    timedatectl set-timezone Asia/Shanghai
	systemctl restart rsyslog
	systemctl restart crond
echo '#rdate /minute
*/5 * * * *    /bin/rdate -s time.nist.gov  >>/var/log/rdate.log 2>&1' > /var/spool/cron/root
    chmod 600 /var/spool/cron/root
}

common_add_user () {
    while true;do
        read -p "默认要添加的用户列表为:$default_user_list 确定吗(y/n)" user_list_yn
        case $user_list_yn in
            y|Y)
            userlist=$default_user_list
            break;;
            n|N)
                while true;do
                    read -p "请输入要添加的用户名,以空格隔开,例如:swadmin ybadmin。用户列表：" user_list
                    read -p "用户列表为 $user_list 确定吗(y/n)" user_list_yn
                    case $user_list_yn in
                        y|Y)
                        userlist=$user_list
                        break;;
                        n|N)
                        continue;;
                    esac
                done
            break;;
        esac
    done
    echo -e "\033[36m \t\t\t 添加用户并配置密码  \t\t\t  \033[0m"
    for user in $userlist;do
        id $user &> /dev/null
        if [ $? -ne 0 ];then
            useradd $user &>/dev/null
        fi
    done
}
webuser_password () {
    echo 'Passw0rd'|passwd --stdin blog &>/dev/null
    echo 'Passw0rd!**yiboweb'|passwd --stdin swadmin &>/dev/null
    echo 'yibo3edcMJU&*!*2018web'|passwd --stdin root &>/dev/null
    echo 'Passw0rd!**yibomt' | passwd --stdin mtadmin  &>/dev/null
	echo 'Passw0rd!**yibowebadmin' | passwd --stdin ybadmin &>/dev/null
}
dbuser_password () {
    echo 'Passw0rdBlog'|passwd --stdin blog &>/dev/null
    echo 'Passw0rd!**yibodb'|passwd --stdin swadmin &>/dev/null
    echo 'yibo3edcMJU&*!*2018db'|passwd --stdin root &>/dev/null
    echo 'Passw0rd!**yibomt' | passwd --stdin mtadmin &>/dev/null
	echo 'Passw0rd!**yibodbadmin' | passwd --stdin ybadmin &>/dev/null
}
add_web_name () {
    while true; do
        read -p "请输入您要部署站的令牌码:" web_name
        read -p "即将部署的站的令牌码为：$web_name 确定吗(y/n)" web_name_yn
        case $web_name_yn in
            y|Y)
            break;;
            n|N)
            continue;;
        esac
    done
    webname=$web_name
}

add_web_analysis_ip () {
    while true; do
        read -p "您部署的主机是韩国还是香港？韩国请选1，香港请选2。(1/2): " location
        case $location in
            1)
                read -p "您选择的主机是韩国主机确定吗(y/n)" kr_yn
                case $kr_yn in
                    y|Y)
                    analysis=monday.javagamecollect6.com
                    downloadserver=$downloadserver_kr
					remote_backserver="kr"
                    break;;
                    n|N)
                    continue;;
                esac;;
            2)
            read -p "您选择的主机是香港主机确定吗(y/n)" hk_yn
            case $hk_yn in
                    y|Y)
                    analysis=sunday.javagamecollect5.com
                    downloadserver=$downloadserver_hk
					remote_backserver="hk"
                    break;;
                    n|N)
                    continue;;
            esac;;
        esac
    done
}

add_web_slave_ip () {
# add master/slave sync web ip address, run in master web server.    
    
    echo "检测到您的当前的IP地址为:$multi_default_ip " 

    while true; do
        read -p "请输入备站所有IP地址:" web_slave_ip
        read -p "备站IP地址为:$web_slave_ip 确定吗(y/n)" web_slave_ip_yn
        case $web_slave_ip_yn in
            y|Y)
            webslaveip=$web_slave_ip
            break;;
            n|N)
            continue;;
        esac
    done
}

add_web_master_slave_ip () {
# add web master/slave  ip address, run in db server. 
   echo "检测到您当前的IP地址为:$multi_default_ip " 
    while true; do
        read -p "请输入主站所有IP地址:" web_master_ip
		read -p "请输入备站所有IP地址:" web_slave_ip
        read -p "主站IP地址为: $web_master_ip 备站IP地址为: $web_slave_ip 确定吗(y/n)" web_master_slave_ip_yn
		case $web_master_slave_ip_yn in
            y|Y)
			webmasterip=$web_master_ip
            webslaveip=$web_slave_ip
            break;;
            n|N)
            continue;;
        esac
    done
}


add_web_master_ip () {
# add slave/master sync web ip address, run in slave web server    

    echo "检测到您当前的IP地址为:$multi_default_ip "

    while true; do
        read -p "请输入主站所有IP地址:" web_master_ip
        read -p "主站IP地址为:$web_master_ip 确定吗(y/n)" web_master_ip_yn
        case $web_master_ip_yn in
            y|Y)
            webmasterip=$web_master_ip
            break;;
            n|N)
            continue;;
        esac
    done
}

add_db_master_slave_ip () {
# add master/slave sync db ip address, run in master database server    

    while true;do
        read -p "请输入主库所有IP地址:" db_master_ip
        read -p "主库IP地址为:$db_master_ip 确定吗(y/n)" db_master_ip_yn
        case $db_master_ip_yn in
        y|Y)
        dbmasterip=$db_master_ip
        break;;
        n|N)
        continue;;
        esac
    done

    while true; do
        read -p "请输入备库所有IP地址:" db_slave_ip
        read -p "备库IP地址为:$db_slave_ip 确定吗(y/n)" db_slave_ip_yn
        case $db_slave_ip_yn in
            y|Y)
            dbslaveip=$db_slave_ip
            break;;
            n|N)
            continue;;
        esac
    done
}

add_db_master_ip () {
# add master db ip address, run in slave database server    

    while true;do
        read -p "请输入主库所有IP地址:" db_master_ip
        read -p "主库IP地址为:$db_master_ip 确定吗(y/n)" db_master_ip_yn
        case $db_master_ip_yn in
        y|Y)
        dbmasterip=$db_master_ip
        break;;
        n|N)
        continue;;
        esac
    done
}
add_db_slave_ip () {
# add slave db ip address, run in master database server    

    while true;do
        read -p "请输入从库所有IP地址:" db_slave_ip
        read -p "从库IP地址为:$db_slave_ip 确定吗(y/n)" db_slave_ip_yn
        case $db_slave_ip_yn in
        y|Y)
        dbslaveip=$db_slave_ip
        break;;
        n|N)
        continue;;
        esac
    done
}
add_db_slave_master_ip () {
# add master/slave sync db ip address, run in slave database server
    while true; do
        read -p "检测到您的备库IP地址为:$multi_default_ip 确定吗(y/n)" default_db_slave_ip_yn
        case $default_db_slave_ip_yn in
            y|Y)
            dbslaveip=$muilti_default_ip
            break;;
            n|N)
                while true;do
                    read -p "请输入备库所有IP地址:" db_slave_ip
                    read -p "备库IP地址为:$db_slave_ip 确定吗(y/n)" db_slave_ip_yn
                    case $db_slave_ip_yn in
                        y|Y)
                        dbslaveip=$db_slave_ip
                        break;;
                        n|N)
                        continue;;
                    esac
                done
            break;;
        esac
    done

    while true; do
        read -p "请输入主库所有IP地址:" db_master_ip
        read -p "主库IP地址为:$db_slave_ip 确定吗(y/n)" db_master_ip_yn
        case $db_master_ip_yn in
            y|Y)
            dbmasterip=$db_master_ip
            break;;
            n|N)
            continue;;
        esac
    done
}

add_web_db_master_slave_ip () {
    while true; do
        read -p "检测到您的主站/主库IP地址为:$multi_default_ip 确定吗(y/n)" default_web_db_master_ip_yn
        case $default_web_db_master_ip_yn in
            y|Y)
            webdbmasterip=$multi_default_ip
            break;;
            n|N)
                while true;do
                    read -p "请输入主站/主库所有IP地址:" web_db_master_ip
                    read -p "主站/主库IP地址为:$web_db_master_ip 确定吗(y/n)" web_db_master_ip_yn
                    case $web_db_master_ip_yn in
                        y|Y)
                        webdbmasterip=$web_db_master_ip
                        break;;
                        n|N)
                        continue;;
                    esac
                done
            break;;
        esac
    done

    while true; do
        read -p "请输入备站/备库所有IP地址:" web_db_slave_ip
        read -p "备站/备库IP地址为:$web_db_slave_ip 确定吗(y/n)" web_db_slave_ip_yn
        case $web_db_slave_ip_yn in
            y|Y)
            webdbslaveip=$web_db_slave_ip
            break;;
            n|N)
            continue;;
        esac
    done
# redefine web and databse master/slave ip address    
    webmasterip=$webdbmasterip
    webslaveip=$webdbslaveip
    dbmasterip=$webdbmasterip
    dbslaveip=$webdbslaveip
}

add_web_db_slave_master_ip () {
    while true; do
        read -p "检测到您的备站/备库IP地址为:$multi_default_ip 确定吗(y/n)" default_web_db_slave_ip_yn
        case $default_web_db_slave_ip_yn in
            y|Y)
            webdbslaveip=$multi_default_ip
            break;;
            n|N)
                while true;do
                    read -p "请输入备站/备库所有IP地址:" web_db_slave_ip
                    read -p "备站/备库IP地址为:$web_db_slave_ip 确定吗(y/n)" web_db_slave_ip_yn
                    case $web_db_slave_ip in
                        y|Y)
                        webdbslaveip=$web_db_slave_ip
                        break;;
                        n|N)
                        continue;;
                    esac
                done
            break;;
        esac
    done

    while true; do
        read -p "请输入主站/主库所有IP地址:" web_db_master_ip
        read -p "主站/主库IP地址为:$web_db_master_ip 确定吗(y/n)" web_db_master_ip_yn
        case $web_db_master_ip_yn in
            y|Y)
            webdbmasterip=$web_db_master_ip
            break;;
            n|N)
            continue;;
        esac
    done
# redefine web and databse master/slave ip address    
    webmasterip=$webdbmasterip
    webslaveip=$webdbslaveip
    dbmasterip=$webdbmasterip
    dbslaveip=$webdbslaveip
}

add_test_web_ip () {
#add test website  ip address 
    while true; do
        read -p "测试站IP地址:" test_web_ip
        read -p "测试站IP地址为:$test_web_ip 确定吗(y/n)" test_web_ip_yn
        case $test_web_ip_yn in
            y|Y)
            break;;
            n|N)
            continue;;
        esac
    done
    testwebip=$test_web_ip
}



install_web_basic_package () {
    echo -e "\033[36m \t\t\t install web dependency package  \t\t\t  \033[0m"
    yum -y install wget rdate vim lsof nc tree psmisc net-tools gcc gcc-c++ zip unzip pcre pcre-devel rsync w3m mtr
	yum -y install zlib zlib-devel openssl openssl-devel telnet GeoIP-devel expect screen sysstat epel-release tcping fio
}

install_db_basic_package () {
    echo -e "\033[36m \t\t\t install database dependency package  \t\t\t  \033[0m"
	yum -y install  http://www.percona.com/downloads/percona-release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm
	yum -y install percona-xtrabackup-24 qpress
    yum -y install wget rdate vim nc lsof tree psmisc net-tools gcc gcc-c++ zip unzip pcre pcre-devel zlib zlib-devel openssl openssl-devel php php-mysql
	yum -y install wget telnet lua-devel rsync libevent libevent-devel libmount-devel libmount-devel libtool perl-devel libaio expect screen sysstat epel-release fio mtr
}

set_web_master_firewall () {
# 设置ssh direct白规则(公司网段IP）
    firewall-cmd --permanent --direct --add-rule ipv4 filter INPUT 0 -s $office_ip  -p tcp --dport 22  -j ACCEPT && systemctl restart firewalld
# add ipset whitelist
    systemctl restart firewalld && systemctl enable firewalld
    firewall-cmd --permanent --new-ipset=web_whitelist --type=hash:ip
    firewall-cmd --permanent --new-ipset=rsync_whitelist --type=hash:ip
    firewall-cmd --permanent --new-ipset=ssh_whitelist --type=hash:ip
    firewall-cmd --permanent --new-ipset=db_whitelist --type=hash:ip
    firewall-cmd --permanent --new-ipset=blacklist --type=hash:ip
    firewall-cmd --permanent --new-ipset=8002_whitelist --type=hash:ip
    firewall-cmd --permanent --new-ipset=zabbix_whitelist --type=hash:ip
    systemctl restart firewalld
# add ip to web and ssh whitelist 
    firewall-cmd --permanent --ipset=web_whitelist --add-entry="$office_ip"
    firewall-cmd --permanent --ipset=web_whitelist --add-entry="$analysis_hk"
    firewall-cmd --permanent --ipset=web_whitelist --add-entry="$analysis_kr"
    firewall-cmd --permanent --ipset=db_whitelist --add-entry="$office_ip"
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$office_ip"
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins1_hk"
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins2_hk"
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins3_hk"
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins4_hk"
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins3_kr_masterip"
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins3_kr_secondip"
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins_kr_masterip" #2018-12-28
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins_kr_secondip" #2018-12-28
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins2_kr_masterip" #2018-12-28
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins2_kr_secondip" #2018-12-28
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins4_kr_masterip" #2018-12-28
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins4_kr_secondip" #2018-12-28
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins5_kr" 
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins6_kr" 
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins7_kr" 
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins8_kr" 
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$testwebip"
    firewall-cmd --permanent --ipset=8002_whitelist --add-entry="$testwebip"
    firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_kr_server_slave"
    firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_kr_server_master"
    firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_hk_proxy"
	firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_kr_proxy"

    for i in $webslaveip ;do 
        firewall-cmd --permanent --ipset=web_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=rsync_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=db_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=8002_whitelist --add-entry="$i"
    done
    for i in $dbmasterip;do 
        firewall-cmd --permanent --ipset=db_whitelist --add-entry="$i"
    done
    for i in $dbslaveip;do 
        firewall-cmd --permanent --ipset=db_whitelist --add-entry="$i"
    done
#添加pulic.xml
    cd /etc/firewalld/zones
    mv public.xml{,.bak}
    wget  --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E5%85%B6%E4%BB%96/web_public.xml -O public.xml
    chmod 644 public.xml  && systemctl restart firewalld
}

set_web_slave_firewall () {
# 设置ssh direct白规则(公司网段IP）
    firewall-cmd --permanent --direct --add-rule ipv4 filter INPUT 0 -s $office_ip  -p tcp --dport 22  -j ACCEPT && systemctl restart firewalld
# add ipset whitelist
    systemctl restart firewalld && systemctl enable firewalld
    firewall-cmd --permanent --new-ipset=web_whitelist --type=hash:ip
    firewall-cmd --permanent --new-ipset=rsync_whitelist --type=hash:ip
    firewall-cmd --permanent --new-ipset=ssh_whitelist --type=hash:ip
    firewall-cmd --permanent --new-ipset=db_whitelist --type=hash:ip
    firewall-cmd --permanent --new-ipset=blacklist --type=hash:ip
	firewall-cmd --permanent --new-ipset=8002_whitelist --type=hash:ip
	firewall-cmd --permanent --new-ipset=zabbix_whitelist --type=hash:ip
    systemctl restart firewalld
# add ip to web and ssh whitelist 
    firewall-cmd --permanent --ipset=web_whitelist --add-entry="$office_ip" 
    firewall-cmd --permanent --ipset=web_whitelist --add-entry="$analysis_hk" 
    firewall-cmd --permanent --ipset=web_whitelist --add-entry="$analysis_kr" 
    firewall-cmd --permanent --ipset=db_whitelist --add-entry="$office_ip"
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$office_ip"
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins1_hk"
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins2_hk"
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins3_hk"
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins4_hk"
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins3_kr_masterip"
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins3_kr_secondip"
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins_kr_masterip" #2018-12-28
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins_kr_secondip" #2018-12-28
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins2_kr_masterip" #2018-12-28
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins2_kr_secondip" #2018-12-28
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins4_kr_masterip" #2018-12-28
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$jenkins4_kr_secondip" #2018-12-28
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$testwebip"
    firewall-cmd --permanent --ipset=8002_whitelist --add-entry="$testwebip"
    firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_kr_server_slave"
    firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_kr_server_master"
    firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_hk_proxy"
    firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_kr_proxy"	
    for i in $webmasterip;do 
        firewall-cmd --permanent --ipset=web_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=rsync_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=db_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=8002_whitelist --add-entry="$i"
    done
    for i in $dbmasterip;do
        firewall-cmd --permanent --ipset=db_whitelist --add-entry="$i"
    done
    for i in $dbslaveip;do
        firewall-cmd --permanent --ipset=db_whitelist --add-entry="$i"
    done
#添加pulic.xml
    cd /etc/firewalld/zones
    mv public.xml{,.bak}
    wget  --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E5%85%B6%E4%BB%96/web_public.xml -O public.xml
    chmod 644 public.xml  && systemctl restart firewalld
}

set_db_master_firewall () {
# 设置ssh direct白规则(公司网段IP）
    firewall-cmd --permanent --direct --add-rule ipv4 filter INPUT 0 -s $office_ip  -p tcp --dport 22  -j ACCEPT && systemctl restart firewalld
# add ipset whitelist
    systemctl restart firewalld && systemctl enable firewalld
        firewall-cmd --permanent --new-ipset=db_whitelist --type=hash:ip
        firewall-cmd --permanent --new-ipset=ssh_whitelist --type=hash:ip
        firewall-cmd --permanent --new-ipset=zabbix_whitelist --type=hash:ip
    systemctl restart firewalld
# add ip to web and ssh whitelist 
    firewall-cmd --permanent --ipset=db_whitelist --add-entry="$office_ip" 
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$office_ip"  
	firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$testwebip"
	firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_kr_server_slave"
	firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_kr_server_master"
    firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_hk_proxy"
	firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_kr_proxy"
    for i in $webmasterip;do 
        firewall-cmd --permanent --ipset=db_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$i"
    done
    for i in $webslaveip;do 
        firewall-cmd --permanent --ipset=db_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$i"
    done
    for i in $dbslaveip;do
        firewall-cmd --permanent --ipset=db_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$i"
    done
# 设置public.xml 
    cd /etc/firewalld/zones
    mv public.xml{,.bak}
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E5%85%B6%E4%BB%96/db_public.xml -O public.xml
    chmod 644 public.xml  && systemctl restart firewalld
}

set_db_slave_firewall () {
# 设置ssh direct白规则(公司网段IP）
    firewall-cmd --permanent --direct --add-rule ipv4 filter INPUT 0 -s $office_ip  -p tcp --dport 22  -j ACCEPT && systemctl restart firewalld
# add ipset whitelist
    systemctl restart firewalld && systemctl enable firewalld
    firewall-cmd --permanent --new-ipset=db_whitelist --type=hash:ip
    firewall-cmd --permanent --new-ipset=ssh_whitelist --type=hash:ip
    firewall-cmd --permanent --new-ipset=zabbix_whitelist --type=hash:ip
    systemctl restart firewalld
# add ip to web and ssh whitelist 
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$office_ip" 
    firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$testwebip"
    firewall-cmd --permanent --ipset=db_whitelist --add-entry="$office_ip"
    firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_kr_server_slave"
    firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_kr_server_master"
    firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_hk_proxy"
	firewall-cmd --permanent --ipset=zabbix_whitelist --add-entry="$zabbix_kr_proxy"
    for i in $webmasterip;do
        firewall-cmd --permanent --ipset=db_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$i"
    done
    for i in $webslaveip;do
        firewall-cmd --permanent --ipset=db_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$i"
    done
    for i in $dbmasterip;do
        firewall-cmd --permanent --ipset=db_whitelist --add-entry="$i"
        firewall-cmd --permanent --ipset=ssh_whitelist --add-entry="$i"
    done
# 设置public.xml 
    cd /etc/firewalld/zones
    mv public.xml{,.bak}
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E5%85%B6%E4%BB%96/db_public.xml -O public.xml
    chmod 644 public.xml  && systemctl restart firewalld
}

add_webapps_env_parameters () {
    grep 'HISTTIMEFORMAT="%F %T"' /etc/profile  &> /dev/null
    if [ $? -ne 0 ];then
        echo '################################
HISTSIZE=1000
export TMOUT=600
export HISTTIMEFORMAT="%F %T"
#######JDK环境变量########################
export JAVA_HOME=/opt/apps/jdk
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar
export PATH=$PATH:$JAVA_HOME/bin:$JAVA_HOME/jre/bin
#########rsync环境变量########
export PATH=$PATH:/opt/apps/rsync/bin/'>> /etc/profile
    fi
}

add_db_env_parameters () {
    grep 'HISTTIMEFORMAT="%F %T"' /etc/profile  &> /dev/null
    if [ $? -ne 0 ];then
        echo '################################ 
HISTSIZE=1000
export TMOUT=600
export HISTTIMEFORMAT="%F %T"
#######mysql&&redis环境变量##########
export PATH=$PATH:/opt/apps/mysql/bin/
export PATH=$PATH:/opt/apps/redis/bin/'>> /etc/profile
    fi
}

add_web_db_env_parameters () {
    grep 'HISTTIMEFORMAT="%F %T"' /etc/profile  &> /dev/null
    if [ $? -ne 0 ];then
        echo '################################
HISTSIZE=1000
export TMOUT=600
export HISTTIMEFORMAT="%F %T"
#######JDK环境变量########################
export JAVA_HOME=/opt/apps/jdk
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar
export PATH=$PATH:$JAVA_HOME/bin:$JAVA_HOME/jre/bin
#########rsync环境变量########
export PATH=$PATH:/opt/apps/rsync/bin/
#######mysql&&redis环境变量##########
export PATH=$PATH:/opt/apps/mysql/bin/
export PATH=$PATH:/opt/apps/redis/bin/'>> /etc/profile
    fi
}

create_webapps_directory () {
    mkdir -p /opt/{apps,logs,scripts,src,backup,webapps}
    cd /opt/apps && mkdir GeoIP
    cd /opt/webapps && mkdir -p admin_7001/data  agent_7003  cms_9001/views  live_work_9002  web_8001/{data,views} anls_api_8002 wechat_8003  work_7002
    cd /opt/logs && mkdir nginx  program  sersync  tomcat
    cd /opt/logs/tomcat && mkdir tomcat_7001  tomcat_7002  tomcat_7003  tomcat_8001 tomcat_8002 tomcat_8003  tomcat_9001  tomcat_9002
    chown -R swadmin:swadmin /opt/*
	mkdir -p /backup/{apps_bak,log_bak,webapps_bak}
	cd /backup/log_bak && mkdir nginx tomcat
}

create_db_master_directory () {
    cd /opt && mkdir -p apps conf data/{data_16303,data_17693} src scripts
    chown -R swadmin:swadmin apps conf data src scripts
}

create_db_slave_directory () {
    cd /opt && mkdir -p apps conf backup  data/{data_16303,data_17693} scripts src 
    chown -R swadmin:swadmin apps conf backup data scripts src
	mkdir -p /backup/data_back
}

get_webapps_scripts () { 
    cd /opt/scripts/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E8%84%9A%E6%9C%AC%E7%9B%B8%E5%85%B3/CUT_NGLOG.sh
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E8%84%9A%E6%9C%AC%E7%9B%B8%E5%85%B3/CUT_TOMCAT.sh
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E8%84%9A%E6%9C%AC%E7%9B%B8%E5%85%B3/GEO_UPDATE.sh
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E8%84%9A%E6%9C%AC%E7%9B%B8%E5%85%B3/nginx_back.sh
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E8%84%9A%E6%9C%AC%E7%9B%B8%E5%85%B3/webapps_back.sh
	if [ $remote_backserver == "kr" ];then
		wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E8%84%9A%E6%9C%AC%E7%9B%B8%E5%85%B3/krwebback.sh
	else
		wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E8%84%9A%E6%9C%AC%E7%9B%B8%E5%85%B3/hkwebback.sh
	fi
    chown -R swadmin:swadmin /opt/*
	su swadmin -c "
	bash /opt/scripts/GEO_UPDATE.sh
	"
}
get_db_scripts () {
    cd /opt/scripts/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E8%84%9A%E6%9C%AC%E7%9B%B8%E5%85%B3/mysqlback.sh
    chown -R swadmin:swadmin /opt/*
}

install_geoip_nginx () {
    su  swadmin -c "
    cd /opt/src/ 
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/GeoIP.tar.gz
    tar -xf GeoIP.tar.gz
    cd GeoIP-1.4.8
    ./configure --prefix=/opt/apps/GeoIP 
    make
    make install 
    "
    ln -s /opt/apps/GeoIP/lib/*  /lib64/
    su  swadmin -c "
    cd /opt/src/ 
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/nginx-1.10.3.tar.gz
    tar -xf nginx-1.10.3.tar.gz 
    cd nginx-1.10.3
    ./configure --prefix=/opt/apps/nginx --with-http_stub_status_module --with-http_ssl_module --with-http_geoip_module --with-http_gzip_static_module --with-ipv6 --with-http_realip_module  --user=swadmin --group=swadmin
    make
    make install
    cd /opt/apps/nginx/conf
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/ip.conf
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/blacklist.conf
    rm -rf nginx.conf
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/GeoIP.dat 
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/GeoLiteCity.dat 
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/nginx.conf
    cp /opt/apps/nginx/conf/nginx.conf /opt/apps/nginx/conf/nginx.conf.default
    sed -i "s/example/$webname/g" nginx.conf
    mkdir -p /opt/apps/nginx/conf/keys/"$webname"_crt
    cd /opt/apps/nginx/conf/keys/"$webname"_crt
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/keys/example_crt/example.crt
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/keys/example_crt/example.key
    mv example.key "$webname".key
    mv example.crt "$webname".crt
    mkdir -p /opt/apps/nginx/conf/vhosts/tgapp
    cd /opt/apps/nginx/conf/vhosts
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/vhosts/admin_default_server.conf
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/vhosts/http_default_server.conf  
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/vhosts/https_default_server.conf
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/vhosts/filter.forbid
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/vhosts/qp.whitelist
    sed -i "s/example/$webname/g" *
    mkdir -p /opt/apps/nginx/conf/vhosts/$webname
    cd /opt/apps/nginx/conf/vhosts/$webname
    # get nginx configuration files
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/vhosts/example/https_web.conf
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/vhosts/example/web.conf 
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/vhosts/example/web_admin.conf 
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/vhosts/example/web_agent.conf 
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/vhosts/example/web_cms.conf 
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/vhosts/example/wechats.conf
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/vhosts/example/work.conf

    sed -i "s/example/$webname/g" * 
    sed -i "s/xxx.xxx.xxx.xxx/$default_ip/" *
    sed -i "s/103.68.110.32/$analysis/g" *
	##
	cd /opt/apps/nginx/conf/vhosts/tgapp
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/https_tgapp12.conf
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/https_tgapp3.conf
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/https_tgapp456.conf
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/https_tgapp789.conf
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/https_tgapp1-5-9.conf
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/https_tgapp8081-3.conf
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/https_tgapp1001-1003.conf
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/https_tgapp2001-3.conf
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/https_tgapp3001-3.conf
	sed -i "s/example/$webname/g"  https_tgapp*.conf
	sed -i "s/xxx.xxx.xxx.xxx/$default_ip/" https_tgapp*.conf
	sed -i "s/103.68.110.32/$analysis/g" https_tgapp*.conf
	mkdir /opt/apps/nginx/conf/keys/{tgapp12,tgapp3,tgapp456,tgapp789,tgapp1-5-9,tgapp8081-3,tgapp1001-1003,tgapp2001-3,tgapp3001-3}	
	cd /opt/apps/nginx/conf/keys/tgapp12/
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp1688-2288/server.crt
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp1688-2288/server.key
	cd /opt/apps/nginx/conf/keys/tgapp3/
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp3588/server.crt
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp3588/server.key
	cd /opt/apps/nginx/conf/keys/tgapp456
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp456/server.crt
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp456/server.key
	cd /opt/apps/nginx/conf/keys/tgapp789
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp789/server.crt
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp789/server.key
    cd /opt/apps/nginx/conf/keys/tgapp1-5-9
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp1234-tgapp5678-tgapp9012/server.crt
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp1234-tgapp5678-tgapp9012/server.key
	cd /opt/apps/nginx/conf/keys/tgapp8081-3
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp8081-3/server.crt
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp8081-3/server.key
	cd /opt/apps/nginx/conf/keys/tgapp1001-1003
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp1001-1003/server.crt
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp1001-1003/server.key
	cd /opt/apps/nginx/conf/keys/tgapp2001-3
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp2001-3/server.crt
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp2001-3/server.key
	cd /opt/apps/nginx/conf/keys/tgapp3001-3
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp3001-3/server.crt
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/nginx/tgapp/tgapp3001-3/server.key		
	"
}

install_tomcat () {
    su  swadmin -c "
    cd /opt/src
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/jdk-8u121.tar.xz
    tar -xf jdk-8u121.tar.xz -C /opt/apps/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/tomcat/tomcat.tar.gz
    tar -xf tomcat.tar.gz -C /opt/apps/
    "
}

install_rsync () {
    su  swadmin -c " 
    mkdir -p /opt/apps/rsync/{etc,logs}
    cd /opt/src/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/rsync/rsync_source.zip
    unzip -q rsync_source.zip -d /opt/apps
    "
}

install_sersync () {
    su swadmin -c "
    cd /opt/apps/ 
    wget  --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/key.cz
    cd /opt/src/
    cd /opt/src
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/rsync/sersync_source.zip
    unzip -q sersync_source.zip -d /opt/apps
    "
}

set_web_rsync () {
    su swadmin -c "
    chmod +x /opt/apps/rsync/bin/rsync
    echo 'rsync:RsYnCpAsWoRd' > /opt/apps/rsync/etc/rsyncd.secret
    chmod 600 /opt/apps/rsync/etc/rsyncd.secret
    echo 'RsYnCpAsWoRd' > /opt/scripts/.rsyncd.passwd
    chmod 600 /opt/scripts/.rsyncd.passwd
    /opt/apps/rsync/bin/rsync --daemon --config=/opt/apps/rsync/etc/rsyncd.conf --no-detach &
    "
}

set_web_sersync () {
    website_slaveip=`echo $webslaveip| awk '{print $1}'`
    cd /opt/apps/sersync
    sed -i '/\<remote ip="127.0.0.1" name="data"\/>/a\            \<remote ip='"\"$website_slaveip\""' name="data"\/>' data.xml   #追加一行
    sed -i '/\<remote ip="127.0.0.1" name="views"\/>/a\             \<remote ip='"\"$website_slaveip\""' name="views"\/>' views.xml
    sed -i "s/103.68.110.225/$website_slaveip/" nginx_conf.xml
    chmod +x sersync2
    su swadmin -c "
    /opt/apps/sersync/sersync2 -r -d -o /opt/apps/sersync/data.xml
    /opt/apps/sersync/sersync2 -r -d -o /opt/apps/sersync/views.xml 
    /opt/apps/sersync/sersync2 -r -d -o /opt/apps/sersync/nginx_conf.xml
    touch /opt/webapps/admin_7001/data/hello
    touch /opt/webapps/cms_9001/views/world
    "
}

install_master_mysql () {
    server_id=`echo $default_ip | cut -d . -f 4`
    if [ `echo ${#server_id}` -eq 1 ];then
        server_id=00$server_id
    elif [ `echo ${#server_id}` -eq 2 ]; then
        server_id=0$server_id
    fi
    su  swadmin -c "
    cd /opt/conf 
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/db/my_16303.cnf
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/db/syncdb-init/syncdb-init.sql -P /opt/src/
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/db/syncdb-init/trigger.sql  -P /opt/src/
    "
    sed -i "s/^server-id = 16303110/server-id = 16303$server_id/g" /opt/conf/my_16303.cnf
    su swadmin -c "
    cd /opt/src
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/mysql-5.7.17-linux-glibc2.5-x86_64.tar.xz
    tar -xf mysql-5.7.17-linux-glibc2.5-x86_64.tar.xz -C /opt/apps/
    cd /opt/apps/
    mv mysql-5.7.17-linux-glibc2.5-x86_64/ mysql
    /opt/apps/mysql/bin/mysqld --defaults-file=/opt/conf/my_16303.cnf --initialize-insecure --user=swadmin
    sleep 3
    /opt/apps/mysql/bin/mysqld --defaults-file=/opt/conf/my_16303.cnf --user=swadmin &
    "
}

install_slave_mysql () {
    server_id=`echo $default_ip | cut -d . -f 4`
    if [ `echo ${#server_id}` -eq 1 ];then
        server_id=00$server_id
    elif [ `echo ${#server_id}` -eq 2 ]; then
        server_id=0$server_id
    fi
    su  swadmin -c "
    cd /opt/conf/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/db/my_slave_16303.cnf
    "
    sed -i "s/^server-id = 16303220/server-id = 16303$server_id/g" /opt/conf/my_slave_16303.cnf
    su swadmin -c "
    cd /opt/src
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/mysql-5.7.17-linux-glibc2.5-x86_64.tar.xz
    tar -xf mysql-5.7.17-linux-glibc2.5-x86_64.tar.xz -C /opt/apps/
    cd /opt/apps/
    mv mysql-5.7.17-linux-glibc2.5-x86_64/ mysql
    /opt/apps/mysql/bin/mysqld --defaults-file=/opt/conf/my_slave_16303.cnf --initialize-insecure --user=swadmin
    sleep 3
    /opt/apps/mysql/bin/mysqld --defaults-file=/opt/conf/my_slave_16303.cnf --user=swadmin &
    "
}

install_master_redis () {
    su swadmin -c "
    cd /opt/conf
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/db/re_17693.conf
    cd /opt/src/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/redis-3.2.9.tar.gz
    tar -xf redis-3.2.9.tar.gz -C /opt/apps/
    cd /opt/apps/
    mv redis-3.2.9/ redis 
    cd redis
    make MALLOC=libc 
    make PREFIX=/opt/apps/redis install
    /opt/apps/redis/src/redis-server  /opt/conf/re_17693.conf &
    "
}

install_slave_redis () {
    database_masterip=`echo $dbmasterip | awk '{print $1}'`
    su swadmin -c "
    cd /opt/src
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/redis-3.2.9.tar.gz
    tar -xf redis-3.2.9.tar.gz -C /opt/apps/
    cd /opt/apps
    mv redis-3.2.9 redis
    cd redis
    make MALLOC=libc 
    make PREFIX=/opt/apps/redis install
    cd /opt/conf/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/db/re_slave_17693.conf 
    sed -i "s/XXX.XXX.XXX.XXX/$database_masterip/" re_slave_17693.conf
    /opt/apps/redis/src/redis-server /opt/conf/re_slave_17693.conf &
    "
}

grant_mysql_master_privileges () {
	while ! ls /opt/data/data_16303/mysql.sock &>/dev/null 
	do 
		echo "wait for mysql-server to up ... ..."
		sleep 1
	done

    for i in $dbslaveip;do
expect << EOF
        spawn /opt/apps/mysql/bin/mysql -uroot -p -S /opt/data/data_16303/mysql.sock -e "    
        grant replication slave on *.* to myrync@'$i' identified by 'MyryncCloud';
        flush privileges;
	    reset master;
        "
        expect "Enter password:" {send "\r"}
        expect eof
EOF
    done
expect << EOF
    spawn /opt/apps/mysql/bin/mysql -uroot -p -S /opt/data/data_16303/mysql.sock -e "
    create database gameplat_analysis;
    create database gameplat_sc_data;
    create database gameplat_cms;
	create user zabbixmonitor@localhost;
    grant process,replication client,select on *.* to zabbixmonitor@localhost;
	grant trigger on gameplat_sc_data.* to 'zabbixmonitor'@'localhost';
    grant all privileges on gameplat_analysis.* TO 'tgadmin'@'113.61.35.%' identified by 'aNaMuxFJY64OK_4q${webname}';
    grant all privileges on gameplat_sc_data.* TO 'tgadmin'@'113.61.35.%';
    grant all privileges on gameplat_cms.* TO 'tgadmin'@'113.61.35.%';
    grant select on gameplat_cms.* TO 'tgblog'@'113.61.35.%'  identified by '3JPBKSt_6kOiF2mD${webname}';
    grant select on gameplat_analysis.* TO 'tgblog'@'113.61.35.%';
    grant select on gameplat_sc_data.* TO 'tgblog'@'113.61.35.%';
    "
    expect "Enter password:" {send "\r"}
    expect eof
EOF

    rand_pass=`echo "${webname}" |md5sum |cut -c 9-24`
    for i in $webmasterip;do
expect << EOF
        spawn /opt/apps/mysql/bin/mysql -uroot -p -S /opt/data/data_16303/mysql.sock -e "    
        grant all privileges on gameplat_analysis.* TO 'gameplat_analysis_dev'@'$i' identified by 'xjVXkB>Q6JpB61r${rand_pass}';
        grant all privileges on gameplat_sc_data.* TO 'gameplat_sc_data_dev'@'$i' identified by 'OeJr)4uRGAuf(BH${rand_pass}';
        grant all privileges on gameplat_cms.* TO 'gameplat_cms_dev'@'$i' identified by '9ckhq<64RZ2YUSR${rand_pass}';
        "
        expect "Enter password:" {send "\r"}
        expect eof
EOF
    done

    for i in $webslaveip;do
expect << EOF
        spawn /opt/apps/mysql/bin/mysql -uroot -p -S /opt/data/data_16303/mysql.sock -e "    
        grant all privileges on gameplat_analysis.* TO 'gameplat_analysis_dev'@'$i' identified by 'xjVXkB>Q6JpB61r${rand_pass}';
        grant all privileges on gameplat_sc_data.* TO 'gameplat_sc_data_dev'@'$i' identified by 'OeJr)4uRGAuf(BH${rand_pass}';
        grant all privileges on gameplat_cms.* TO 'gameplat_cms_dev'@'$i' identified by '9ckhq<64RZ2YUSR${rand_pass}';
        "
        expect "Enter password:" {send "\r"}
        expect eof
EOF
    done

expect << EOF
    spawn /opt/apps/mysql/bin/mysql -uroot -p -S /opt/data/data_16303/mysql.sock -e "    
    set password=password('9tN6GFGK60Jk8BNkBJM611GwA66uDFeG');
    flush privileges;
    "
    expect "Enter password:" {send "\r"}
    expect eof
EOF
}

init_db_trigger (){
echo -e "\033[35m \t\t\t+-------------------正在初始化数据库,耐心等待！--------------------+\t\t\t \033[0m"
/opt/apps/mysql/bin/mysql -uroot -p9tN6GFGK60Jk8BNkBJM611GwA66uDFeG -S /opt/data/data_16303/mysql.sock -A < /opt/src/syncdb-init.sql
/opt/apps/mysql/bin/mysql -uroot -p9tN6GFGK60Jk8BNkBJM611GwA66uDFeG -S /opt/data/data_16303/mysql.sock -A < /opt/src/trigger.sql

}

grant_mysql_slave_replication () {
    database_masterip=`echo $dbmasterip | awk '{print $1}'`
expect << EOF
    spawn /opt/apps/mysql/bin/mysql -uroot -p -S /opt/data/data_16303/mysql.sock -e "
    change master to master_host='$database_masterip', master_port=16303, master_user='myrync', master_password='MyryncCloud', master_log_file='mysql-bin.000001', master_log_pos=154, master_connect_retry=15;
    start slave;
    show slave status\G
    flush privileges;
    "
    expect "Enter password:" {send "\r"}
    expect eof
EOF
}


set_web_master_crontab () {
    website_slaveip=`echo $webslaveip | awk '{print $1}'`
    RanDom=$(($RANDOM%59))
    echo "########5分钟同步本地的views、data
*/5 * * * * /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/webapps/admin_7001/data/ rsync@127.0.0.1::data >>/dev/null 2>&1
*/5 * * * * /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/webapps/admin_7001/data/ rsync@$website_slaveip::data >>/dev/null 2>&1
*/5 * * * * /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/webapps/cms_9001/views/ rsync@127.0.0.1::views >>/dev/null 2>&1
*/5 * * * * /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/webapps/cms_9001/views/ rsync@$website_slaveip::views >>/dev/null 2>&1
*/5 * * * * /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/apps/nginx/conf/ rsync@$website_slaveip::nginx_conf >>/dev/null 2>&1
###########全量同步web
##web_8001
*/30 * * * * /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/webapps/web_8001/ rsync@$website_slaveip::web8001 >>/dev/null 2>&1
##anls_8002
0 6 * * *  /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/webapps/anls_api_8002/ rsync@$website_slaveip::anls8002 >>/dev/null 2>&1
##wechat_8003
0 6 * * * /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/webapps/wechat_8003/ rsync@$website_slaveip::wechat8003 >>/dev/null 2>&1
##admin_7001
*/30 * * * * /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/webapps/admin_7001/ rsync@$website_slaveip::admin7001 >>/dev/null 2>&1
##work_7002
*/30 * * * * /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/webapps/work_7002/ rsync@$website_slaveip::work7002 >>/dev/null 2>&1
##agent_7003
*/30 * * * * /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/webapps/agent_7003/ rsync@$website_slaveip::agent7003 >>/dev/null 2>&1
##cms_9001
*/30 * * * * /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/webapps/cms_9001/ rsync@$website_slaveip::cms9001 >>/dev/null 2>&1
##live_work9002
*/30 * * * * /opt/apps/rsync/bin/rsync -avz --password-file=/opt/scripts/.rsyncd.passwd --port=1873 --delete /opt/webapps/live_work_9002/ rsync@$website_slaveip::live_work9002 >>/dev/null 2>&1" > /var/spool/cron/swadmin

echo "######备份data_views_nginx  
$RanDom 4 * * *   /bin/bash /opt/scripts/*webback.sh" >>/var/spool/cron/swadmin

	
    chown  swadmin:swadmin /var/spool/cron/swadmin
    chmod 600 /var/spool/cron/swadmin
    crontab -l -u  swadmin
    echo '########nginx目录备份
00 03 * * *  sudo /usr/bin/bash /opt/scripts/nginx_back.sh
########日志切割
01 00 * * *  sudo /usr/bin/bash /opt/scripts/CUT_NGLOG.sh
02 00 * * *  sudo /usr/bin/bash /opt/scripts/CUT_TOMCAT.sh
#备份webapps
03 00 * * *  sudo /usr/bin/bash /opt/scripts/webapps_back.sh
#update GeoIP ，官网每个月更新一次
00 00 8 * *  sudo -u swadmin  /usr/bin/bash /opt/scripts/GEO_UPDATE.sh' >/var/spool/cron/ybadmin
    chown ybadmin.ybadmin /var/spool/cron/ybadmin
    chmod 600 /var/spool/cron/ybadmin
    crontab -l -u ybadmin
	sudo -u swadmin  /usr/bin/bash /opt/scripts/GEO_UPDATE.sh
}

install_db_master_zabbix () {
    su mtadmin -c "
    cd /home/mtadmin/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/zabbix-agent-db.zip
    sleep 2
    unzip zabbix-agent-db.zip &&  rm -rf zabbix-agent-db.zip
    sleep 1
	chmod +x /home/mtadmin/apps/zabbix/scripts/*
    chmod +x /home/mtadmin/apps/zabbix/sbin/zabbix_agentd
    sed -i  's#\(Hostname=\).*#\1zabbixclient-"$webname"-master#' /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf
    grep Hostname= /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf
    /home/mtadmin/apps/zabbix/sbin/zabbix_agentd
    "
	echo -e "########zabbix开机自启########\nsu mtadmin -c \"/home/mtadmin/apps/zabbix/sbin/zabbix_agentd\"" >> /etc/rc.local
    chmod +x /etc/rc.local
	chmod +x /etc/rc.d/rc.local
	
}

install_db_slave_zabbix () {
    su mtadmin -c "
    cd /home/mtadmin/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/zabbix-agent-db.zip
    sleep 2
    unzip zabbix-agent-db.zip &&  rm -rf zabbix-agent-db.zip
    sleep 1
	chmod +x /home/mtadmin/apps/zabbix/scripts/*
    chmod +x /home/mtadmin/apps/zabbix/sbin/zabbix_agentd
    sed -i  's#\(Hostname=\).*#\1zabbixclient-"$webname"-slave#' /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf
    grep Hostname= /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf
    /home/mtadmin/apps/zabbix/sbin/zabbix_agentd
    "
	echo -e "########zabbix开机自启########\nsu mtadmin -c \"/home/mtadmin/apps/zabbix/sbin/zabbix_agentd\"" >> /etc/rc.local
    chmod +x /etc/rc.local
	chmod +x /etc/rc.d/rc.local
}

install_web_master_zabbix () {
    su mtadmin -c "
    cd /home/mtadmin/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/zabbix-agent-web.zip
    sleep 2
     unzip zabbix-agent-web.zip &&  rm -rf zabbix-agent-web.zip
    sleep 1
	cd /home/mtadmin/apps/zabbix/scripts/
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E5%85%B6%E4%BB%96/sersync_data.sh
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E5%85%B6%E4%BB%96/sersync_views.sh
	cd /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf.d/
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E5%85%B6%E4%BB%96/sersync.conf
	sleep 1
	chmod +x /home/mtadmin/apps/zabbix/scripts/*
    chmod +x /home/mtadmin/apps/zabbix/sbin/zabbix_agentd
    sed -i  's#\(Hostname=\).*#\1zabbixclient-"$webname"-web#' /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf
    grep Hostname= /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf
     /home/mtadmin/apps/zabbix/sbin/zabbix_agentd
    "
	echo -e "########zabbix开机自启########\nsu mtadmin -c \"/home/mtadmin/apps/zabbix/sbin/zabbix_agentd\"" >> /etc/rc.local
    chmod +x /etc/rc.local
	chmod +x /etc/rc.d/rc.local
}

install_web_slave_zabbix () {
    su mtadmin -c "
    cd /home/mtadmin/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/zabbix-agent-web.zip
    sleep 2
     unzip zabbix-agent-web.zip &&  rm -rf zabbix-agent-web.zip
    sleep 1
	chmod +x /home/mtadmin/apps/zabbix/scripts/*
    chmod +x /home/mtadmin/apps/zabbix/sbin/zabbix_agentd
    sed -i  's#\(Hostname=\).*#\1zabbixclient-"$webname"-web-backup#' /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf
    grep Hostname= /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf
    /home/mtadmin/apps/zabbix/sbin/zabbix_agentd
    "
	echo -e "########zabbix开机自启########\nsu mtadmin -c \"/home/mtadmin/apps/zabbix/sbin/zabbix_agentd\"" >> /etc/rc.local
    chmod +x /etc/rc.local
	chmod +x /etc/rc.d/rc.local
}

install_web_db_master_zabbix () {
    su mtadmin -c "
    cd /home/mtadmin/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/zabbix-agent-web%2Bdb.zip
    sleep 2
    unzip zabbix-agent-web+db.zip &&  rm -rf zabbix-agent-web+db.zip
    sleep 1
	cd /home/mtadmin/apps/zabbix/scripts/
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E5%85%B6%E4%BB%96/sersync_data.sh
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E5%85%B6%E4%BB%96/sersync_views.sh
	cd /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf.d/
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E5%85%B6%E4%BB%96/sersync.conf
	sleep 1
	chmod +x /home/mtadmin/apps/zabbix/scripts/*
    chmod +x /home/mtadmin/apps/zabbix/sbin/zabbix_agentd
    sed -i  's#\(Hostname=\).*#\1zabbixclient-"$webname"-web-master#' /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf
    grep Hostname= /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf
    /home/mtadmin/apps/zabbix/sbin/zabbix_agentd
    "
	echo -e "########zabbix开机自启########\nsu mtadmin -c \"/home/mtadmin/apps/zabbix/sbin/zabbix_agentd\"" >> /etc/rc.local
    chmod +x /etc/rc.local
	chmod +x /etc/rc.d/rc.local
}

run_scan_file_as_daemon (){
	wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E8%84%9A%E6%9C%AC%E7%9B%B8%E5%85%B3/scan_file.py -O /opt/scripts/scan_file.py
	echo -e "########run_scan_file_as_daemon########\npython /opt/scripts/scan_file.py &" >> /etc/rc.local
}

install_web_db_slave_zabbix () {
    su mtadmin -c "
    cd /home/mtadmin/
    wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E9%80%9A%E7%94%A8%E5%8C%85/zabbix-agent-web%2Bdb.zip
    sleep 2
    unzip zabbix-agent-web+db.zip  &&  rm -rf zabbix-agent-web+db.zip
    sleep 1
	chmod +x /home/mtadmin/apps/zabbix/scripts/*
    chmod +x /home/mtadmin/apps/zabbix/sbin/zabbix_agentd
    sed -i  's#\(Hostname=\).*#\1zabbixclient-"$webname"-web-backup-slave#' /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf
    grep Hostname= /home/mtadmin/apps/zabbix/etc/zabbix_agentd.conf
    /home/mtadmin/apps/zabbix/sbin/zabbix_agentd
    "
	echo -e "########zabbix开机自启########\nsu mtadmin -c \"/home/mtadmin/apps/zabbix/sbin/zabbix_agentd\"" >> /etc/rc.local
    chmod +x /etc/rc.local
	chmod +x /etc/rc.d/rc.local
}
set_web_slave_crontab () {
    echo '########nginx目录备份
00 03 * * *  sudo /usr/bin/bash /opt/scripts/nginx_back.sh
########日志切割
01 00 * * *  sudo /usr/bin/bash /opt/scripts/CUT_NGLOG.sh
02 00 * * *  sudo /usr/bin/bash /opt/scripts/CUT_TOMCAT.sh
#备份webapps
03 00 * * *  sudo /usr/bin/bash /opt/scripts/webapps_back.sh
#update GeoIP ，官网每个月更新一次
00 00 8 * *  sudo -u swadmin  /usr/bin/bash /opt/scripts/GEO_UPDATE.sh' >/var/spool/cron/ybadmin
    chown ybadmin.ybadmin /var/spool/cron/ybadmin
    chmod 600 /var/spool/cron/ybadmin
    crontab -l -u ybadmin
}

set_mysql_master_crontab () {
    echo '######备份数据库
5 5 * * * sudo  /bin/bash /opt/scripts/mysqlback.sh
' >>/var/spool/cron/ybadmin
    chown ybadmin.ybadmin /var/spool/cron/ybadmin
    chmod 600 /var/spool/cron/ybadmin
    crontab -l -u ybadmin
}

set_db_remoteback (){
	echo ${webname} >/usr/local/.tocken_var
	if [ $remote_backserver == "kr" ];then
		wget --http-user=${http_user}  --http-password=${http_password} --no-check-certificate   https://$downloadserver/%E7%BA%BF%E4%B8%8A%E7%8E%AF%E5%A2%83/%E7%BA%BF%E4%B8%8A%E5%8C%85%E4%B8%8E%E9%85%8D%E7%BD%AE/%E8%84%9A%E6%9C%AC%E7%9B%B8%E5%85%B3/remote_back.sh -O /opt/scripts/remote_back.sh
		chmod 600 /opt/scripts/remote_back.sh
		echo "WIxii20OhL1qM5q93MeASh4sSrdzCzfGrxWXtoXRLvq9s7cFFQMJtUdgiPIHPB4R" >/opt/scripts/.rsyncd.passwd;setfacl -m u:ybdeploy:r /opt/scripts/.rsyncd.passwd
		(crontab -l|egrep -v  "rsync|db异地备份|remote_back" ;echo -e "# db异地备份\n$(($RANDOM%59)) $(($RANDOM%3+6)) * * *  /usr/bin/bash /opt/scripts/remote_back.sh" ) |crontab
	fi
}

common_print_success () {
    echo -e "\033[36m \t\t\t congratulation you! deploy successfuly! \t\t\t \033[0m"
}
common_delete_itself() {
    cd $current_dir
    self="$current_dir/${0}"
    while [ -f $self ]; do
        rm -rf $self
    done         
}
print_db_passwd() {
    echo -e "\033[32m DB USER gameplat_analysis_dev CONNECTION PASSWORD: \t xjVXkB>Q6JpB61r${rand_pass} \033[0m"
    echo -e "\033[32m DB USER gameplat_sc_data_dev  CONNECTION PASSWORD: \t OeJr)4uRGAuf(BH${rand_pass} \033[0m"
    echo -e "\033[32m DB USER gameplat_cms_dev      CONNECTION PASSWORD: \t 9ckhq<64RZ2YUSR${rand_pass} \033[0m"
}
###############################define function end################################

########################################menua#####################################
while true; do
    echo -e "\033[36m \t\t\t+---------------------------------------+\t\t\t \033[0m"  
    echo -e "\033[36m \t\t\t|      请选择您要部署的站点架构类型     |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t+---------------------------------------+\t\t\t \033[0m"  
    echo -e "\033[36m \t\t\t| (1) 部署主站主库-两台                 |\t\t\t \033[0m"  
    echo -e "\033[36m \t\t\t| (2) 部署备站备库-两台                 |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t| (3) 部署主站-四台                     |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t| (4) 部署备站-四台                     |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t| (5) 部署主库-四台                     |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t| (6) 部署备库-四台                     |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t| (0) 退出菜单                          |\t\t\t \033[0m"  
    echo -e "\033[36m \t\t\t+---------------------------------------+\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t| \033[5m\c"
    echo -e "\033[31m部署完请立即删除本脚本!当前版本:$version \033[0m\c" 
    echo -e "\033[36m|\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t+---------------------------------------+\t\t\t \033[0m" 
    read -p "选择要部署的环境:" choice

    ######################## perform user selection###################################
    case $choice in  
        0)
             exit
        ;;  
        1) #部署主站主库两台
            common_list_sys_info                      #系统信息

            add_web_name                              #令牌码，并复制给webname
            add_web_db_master_slave_ip                #添加ip(授权或添加防火墙)并赋值，webmasterip=$webdbmasterip  webslaveip=$webdbslaveip  dbmasterip=$webdbmasterip  dbslaveip=$webdbslaveip
            add_web_analysis_ip                       #选择对应分析主机analysis=sunday.javagamecollect5.com  downloadserver=$downloadserver_hk  remote_backserver="hk"
            add_web_db_env_parameters                 #设置历史命令，超时时间，jdk路径，命令(bin)路径
            add_test_web_ip                           #测试ip

            common_add_user                           #userlist='swadmin ybadmin mtadmin blog'       
            webuser_password                          #修改密码
            common_optimize_kernel                    #内核及文件数优化
            common_set_sudo_su_alias                  #添加sudo权限及别名
            common_disable_selinux                    #关闭selinux
            common_hiden_sys_issue                    #隐藏版本号
            common_set_sshd_service                   #设置sshd文件，禁止root登陆，且最大失败登陆次数为3
            common_set_ntp_crontab                    #设置时间同步
            install_web_basic_package                ##下载web基础包

            set_web_master_firewall                  ##设置防火墙

            create_webapps_directory                  #自定义创建目录
            create_db_master_directory                #创建数据库目录
            
            install_db_basic_package                 ##下载数据库依赖包
            install_geoip_nginx                       #下载nginx及组件
            install_tomcat                            #下载jdk与tomcat
            install_rsync                             #下载rsync
            install_sersync                           #下载key,cz与sersync软件包
            install_master_mysql                      #下载软件包，配置文件及初始化数据(*.sql)
            install_master_redis                      #下载配置文件及软件包
            grant_mysql_master_privileges             #数据库授权
		    init_db_trigger                           #初始化数据库

            set_web_rsync                             
            set_web_sersync
            set_web_master_crontab
			set_mysql_master_crontab
			set_db_remoteback
            get_webapps_scripts
			get_db_scripts
            install_web_db_master_zabbix 
            run_scan_file_as_daemon                  #起服务
            common_print_success                     #输出成功
            print_db_passwd                          #输出密码
            common_delete_itself                     #杀死自己
        ;;
        2) #部署备站备库两台    
            common_list_sys_info
             
            add_web_name
            add_web_db_slave_master_ip               #ip和主库一样
            add_web_analysis_ip                      
            add_web_db_env_parameters
            add_test_web_ip
             
            common_add_user
            dbuser_password                          #设置密码
            common_optimize_kernel
            common_set_sudo_su_alias
            common_disable_selinux
            common_hiden_sys_issue
            common_set_sshd_service
            common_set_ntp_crontab
            install_web_basic_package
            
            set_web_slave_firewall

            create_webapps_directory
            create_db_slave_directory

            install_db_basic_package
            install_geoip_nginx
            install_tomcat
            install_rsync
            install_sersync
            install_slave_mysql
            install_slave_redis
            grant_mysql_slave_replication

            set_web_rsync
            set_web_slave_crontab
            get_webapps_scripts
            install_web_db_slave_zabbix
            run_scan_file_as_daemon
            common_print_success
            common_delete_itself
        ;;
        3) #部署主站四台master
            common_list_sys_info                     #系统信息

            add_web_name                             #令牌码
            add_web_slave_ip
            add_db_master_slave_ip
            add_web_analysis_ip
            add_webapps_env_parameters
            add_test_web_ip

            common_add_user
            webuser_password
            common_optimize_kernel
            common_set_sudo_su_alias
            common_disable_selinux
            common_hiden_sys_issue
            common_set_sshd_service
            common_set_ntp_crontab
            install_web_basic_package

            set_web_master_firewall

            create_webapps_directory

            install_geoip_nginx
            install_tomcat
            install_rsync
            install_sersync
            set_web_rsync
            set_web_sersync
            set_web_master_crontab
            get_webapps_scripts
            install_web_master_zabbix
            run_scan_file_as_daemon
            common_print_success
            common_delete_itself
        ;;
        4) #部署备站四台slave
            common_list_sys_info

            add_web_name
            add_web_master_ip
            add_db_master_slave_ip
            add_web_analysis_ip
            add_webapps_env_parameters
            add_test_web_ip
            
            common_add_user
            webuser_password
            common_optimize_kernel
            common_set_sudo_su_alias
            common_disable_selinux
            common_hiden_sys_issue
            common_set_sshd_service
            common_set_ntp_crontab
            install_web_basic_package

            set_web_slave_firewall

            create_webapps_directory

            install_geoip_nginx
            install_tomcat
            install_rsync
            install_sersync
            set_web_rsync
            set_web_slave_crontab
            get_webapps_scripts
            install_web_slave_zabbix
            run_scan_file_as_daemon
            common_print_success
            common_delete_itself
        ;;
        5) #部署主库四台
            common_list_sys_info
            add_web_name

            add_web_master_slave_ip
            add_db_slave_ip
            add_web_analysis_ip
            add_db_env_parameters
            add_test_web_ip
            
            common_add_user
            dbuser_password
            common_optimize_kernel
            common_set_sudo_su_alias
            common_disable_selinux
            common_hiden_sys_issue
            common_set_sshd_service
            common_set_ntp_crontab
            install_db_basic_package			

            create_db_master_directory

            set_db_master_firewall

            install_master_mysql
            install_master_redis
            grant_mysql_master_privileges
		    init_db_trigger
			get_db_scripts
			set_mysql_master_crontab
			set_db_remoteback
            install_db_master_zabbix
            common_print_success
            print_db_passwd
            common_delete_itself
        ;;
        6) #部署备库四台
            common_list_sys_info
            add_web_name

            add_web_master_slave_ip
            add_db_master_ip
            add_web_analysis_ip
            add_db_env_parameters
            add_test_web_ip
            
            common_add_user
            dbuser_password
            common_optimize_kernel
            common_set_sudo_su_alias
            common_disable_selinux
            common_hiden_sys_issue
            common_set_sshd_service
            common_set_ntp_crontab   
            install_db_basic_package			

            create_db_slave_directory

            set_db_slave_firewall

            install_slave_mysql
            install_slave_redis

            grant_mysql_slave_replication

            install_db_slave_zabbix
            common_print_success
            common_delete_itself

        ;;
    esac
done
