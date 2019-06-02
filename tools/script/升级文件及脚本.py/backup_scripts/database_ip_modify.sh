#!/bin/bash
# author：evan
# use: 本脚本用于紧急情况下临时修改数据库连接ip
echo -e "\033[31m温馨提示，本脚本会重启tomcat，务必检查是否重复启动！\033[0m"
read -p "输入您所要更换的为新架构(1)还是老架构(2)(1/2)：" STRUCTURE
if [ $STRUCTURE == 2 ]; then
        read -p "输入您所要更换的令牌码：" TOKEN
fi
read -p "输入新的主库IP：" NEW_MASTERIP
read -p "输入新的从库IP：" NEW_SLAVEIP
######################################
ADMIN_NEW="/opt/webapps/admin_7001/WEB-INF/lib"
WORK_NEW="/opt/webapps/work_7002/WEB-INF/classes"
AGENT_NEW="/opt/webapps/agent_7003/WEB-INF/lib"
WEB_NEW="/opt/webapps/web_8001/WEB-INF/lib"
ANLS_API_NEW="/opt/webapps/anls_api_8002/WEB-INF/classes"
CMS_NEW="/opt/webapps/cms_9001/WEB-INF/classes"
LIVE_WORK_NEW="/opt/webapps/live_work_9002/WEB-INF/classes"
#######################################
ADMIN_OLD="/opt/$TOKEN/webapps/admin_17001/WEB-INF/lib"
WORK_OLD="/opt/$TOKEN/webapps/work_17002/WEB-INF/classes"
AGENT_OLD="/opt/$TOKEN/webapps/agent_17003/WEB-INF/lib"
WEB_OLD="/opt/$TOKEN/webapps/web_18001/WEB-INF/lib"
ANLS_API_OLD="/opt/$TOKEN/webapps/anls_api_18002/WEB-INF/classes"
CMS_OLD="/opt/$TOKEN/webapps/cms_19001/WEB-INF/classes"
LIVE_WORK_OLD="/opt/$TOKEN/webapps/live_work_19002/WEB-INF/classes"
########################################
# 创建临时目录
if [ $STRUCTURE == 1 ]; then
        mkdir /opt/src/upload/temp_src
        TEMP="/opt/src/upload/temp_src"
elif [ $STRUCTURE == 2 ];then
        mkdir /opt/pub/src/upload/temp_src
        TEMP="/opt/pub/src/upload/temp_src"
fi
########################################
while true; do
        if [ $STRUCTURE == 1 ];then
                ADMIN=$ADMIN_NEW
                WORK=$WORK_NEW
                AGENT=$AGENT_NEW
                WEB=$WEB_NEW
                ANLS_API=$ANLS_API_NEW
                CMS=$CMS_NEW
                LIVE_WORK=$LIVE_WORK_NEW
                break
        elif [ $STRUCTURE == 2 ]; then
                ADMIN=$ADMIN_OLD
                WORK=$WORK_OLD
                AGENT=$AGENT_OLD
                WEB=$WEB_OLD
                ANLS_API=$ANLS_API_OLD
                CMS=$CMS_OLD
                LIVE_WORK=$LIVE_WORK_OLD
                break
        else
                read -p "您的输入有误，请重新输入您所要更换的为新架构(1)还是老架构(2)(1/2)：" STRUCTURE
        fi
done

# admin_7001
function MODIFY_ADMIN(){
        if [ ! -e $ADMIN/gameplat-resources-0.0.1-SNAPSHOT.jar ];then
            echo -e "\n\033[31madmin实例文件找不到，请检查\033[0m\n"
        else
            cp $ADMIN/gameplat-resources-0.0.1-SNAPSHOT.jar $TEMP/
            cd $TEMP && jar -xf $TEMP/gameplat-resources-0.0.1-SNAPSHOT.jar
            cd $TEMP && rm gameplat-resources-0.0.1-SNAPSHOT.jar
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_MASTERIP#g" $TEMP/spring/datasource-master.xml
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_SLAVEIP#g" $TEMP/spring/datasource-slave.xml
            sed -i -r "s:hostname=([0-9]{1,3}\.){3}[0-9]{1,3}:hostname=$NEW_MASTERIP:g" $TEMP/redis.properties
            cd $TEMP && zip -r gameplat-resources-0.0.1-SNAPSHOT.jar ./*
            sudo -u ybdeploy cp $TEMP/gameplat-resources-0.0.1-SNAPSHOT.jar $ADMIN
            rm -rf  $TEMP/*
            #重启实例
            if [ $STRUCTURE == 1 ];then
                    sudo /etc/init.d/tomcat_7001 stop
                    sudo /etc/init.d/tomcat_7001 start
            elif [ $STRUCTURE == 2 ];then
                    sudo /etc/init.d/tomcat_7001 stop
                    sudo /etc/init.d/tomcat_7001 start
            fi
            echo -e "\033[36madmin实例已更新重启\033[0m"
        fi
}
# work_7002
function MODIFY_WORK(){
        if [ ! -e $WORK/redis.properties ];then
            echo -e "\n\033[31mwork实例文件找不到，请检查\033[0m\n"
        else
            cp $WORK/spring/{datasource-master.xml,datasource-slave.xml} $TEMP/
            cp $WORK/redis.properties $TEMP/ 
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_MASTERIP#g" $TEMP/datasource-master.xml
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_SLAVEIP#g" $TEMP/datasource-slave.xml
            sed -i -r "s:hostname=([0-9]{1,3}\.){3}[0-9]{1,3}:hostname=$NEW_MASTERIP:g" $TEMP/redis.properties
            sudo -u ybdeploy cp $TEMP/datasource-master.xml $WORK/spring/datasource-master.xml
            sudo -u ybdeploy cp $TEMP/datasource-slave.xml $WORK/spring/datasource-slave.xml
            sudo -u ybdeploy cp $TEMP/redis.properties $WORK/redis.properties
            cd $TEMP && rm -rf datasource-master.xml datasource-slave.xml redis.properties
            #重启实例
            if [ $STRUCTURE == 1 ];then
                    sudo /etc/init.d/tomcat_7002 stop
                    sudo /etc/init.d/tomcat_7002 start
            elif [ $STRUCTURE == 2 ];then
                    sudo /etc/init.d/tomcat_7002 stop
                    sudo /etc/init.d/tomcat_7002 start
            fi
            echo -e "\033[36mwork实例已更新重启\033[0m"
        fi
}

# agent_7003
function MODIFY_AGENT(){
        if [ ! -e $AGENT/gameplat-resources-0.0.1-SNAPSHOT.jar ];then
            echo -e "\n\033[31magent实例文件找不到，请检查\033[0m\n"
        else
            cp $AGENT/gameplat-resources-0.0.1-SNAPSHOT.jar $TEMP/
            cd $TEMP && jar -xf $TEMP/gameplat-resources-0.0.1-SNAPSHOT.jar
            rm $TEMP/gameplat-resources-0.0.1-SNAPSHOT.jar
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_MASTERIP#g" $TEMP/spring/datasource-master.xml
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_SLAVEIP#g" $TEMP/spring/datasource-slave.xml
            sed -i -r "s:hostname=([0-9]{1,3}\.){3}[0-9]{1,3}:hostname=$NEW_MASTERIP:g" $TEMP/redis.properties
            cd $TEMP && zip -r gameplat-resources-0.0.1-SNAPSHOT.jar ./*
            sudo -u ybdeploy cp $TEMP/gameplat-resources-0.0.1-SNAPSHOT.jar $AGENT
            rm -rf $TEMP/*
            #重启实例
            if [ $STRUCTURE == 1 ];then
                    sudo /etc/init.d/tomcat_7003 stop
                    sudo /etc/init.d/tomcat_7003 start
            elif [ $STRUCTURE == 2 ];then
                    sudo /etc/init.d/tomcat_7003 stop
                    sudo /etc/init.d/tomcat_7003 start
            fi
            echo -e "\033[36magent实例已更新重启\033[0m"
        fi
}
# web_8001
function MODIFY_WEB(){
        if [ ! -e $WEB/gameplat-resources-0.0.1-SNAPSHOT.jar ];then
            echo -e "\n\033[31mweb实例文件找不到，请检查\033[0m\n"
        else
            cp $WEB/gameplat-resources-0.0.1-SNAPSHOT.jar $TEMP/
            cd $TEMP && jar -xf $TEMP/gameplat-resources-0.0.1-SNAPSHOT.jar
            cd $TEMP && rm gameplat-resources-0.0.1-SNAPSHOT.jar
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_MASTERIP#g" $TEMP/spring/datasource-master.xml
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_SLAVEIP#g" $TEMP/spring/datasource-slave.xml
            sed -i -r "s:hostname=([0-9]{1,3}\.){3}[0-9]{1,3}:hostname=$NEW_MASTERIP:g" $TEMP/redis.properties
            cd $TEMP && zip -r gameplat-resources-0.0.1-SNAPSHOT.jar ./*
            sudo -u ybdeploy cp $TEMP/gameplat-resources-0.0.1-SNAPSHOT.jar $WEB
            rm -rf $TEMP/*
            #重启实例
            if [ $STRUCTURE == 1 ];then
                    sudo /etc/init.d/tomcat_8001 stop
                    sudo /etc/init.d/tomcat_8001 start
            elif [ $STRUCTURE == 2 ];then
                    sudo /etc/init.d/tomcat_8001 stop
                    sudo /etc/init.d/tomcat_8001 start
            fi
            echo -e "\033[36mweb实例已更新重启\033[0m"
        fi
}

# anls_api_8002
function MODIFY_ANLS_API(){
        if [ ! -e $ANLS_API/application.properties ];then
            echo -e "\n\033[31mwanls_8002实例文件找不到，请检查\033[0m\n"
        else
            cp $ANLS_API/application.properties $TEMP/
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_MASTERIP#g" $TEMP/application.properties
            sed -i -r "s:spring.redis.host=([0-9]{1,3}\.){3}[0-9]{1,3}:spring.redis.host=$NEW_MASTERIP:g" $TEMP/application.properties
            sudo -u ybdeploy cp $TEMP/application.properties $ANLS_API
            cd $TEMP && rm -rf application.properties
            #重启实例
            if [ $STRUCTURE == 1 ];then
                    sudo /etc/init.d/tomcat_8002 stop
                    sudo /etc/init.d/tomcat_8002 start
            elif [ $STRUCTURE == 2 ];then
                    sudo /etc/init.d/tomcat_8002 stop
                    sudo /etc/init.d/tomcat_8002 start
            fi
            echo -e "\033[36manls_api实例已更新重启\033[0m"
        fi
}

# cms_9001
function MODIFY_CMS(){
        if [ ! -e $CMS/redis.properties ];then
            echo -e "\n\033[31mcms实例文件找不到，请检查\033[0m\n"
        else
            cp $CMS/spring/{datasource-master.xml,datasource-slave.xml} $TEMP/
            cp $CMS/redis.properties $TEMP/
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_MASTERIP#g" $TEMP/datasource-master.xml
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_SLAVEIP#g" $TEMP/datasource-slave.xml
            sed -i -r "s:hostname=([0-9]{1,3}\.){3}[0-9]{1,3}:hostname=$NEW_MASTERIP:g" $TEMP/redis.properties
            sudo -u ybdeploy cp $TEMP/datasource-master.xml $CMS/spring/datasource-master.xml
            sudo -u ybdeploy cp $TEMP/datasource-slave.xml $CMS/spring/datasource-slave.xml
            sudo -u ybdeploy cp $TEMP/redis.properties $CMS/redis.properties
            cd $TEMP && rm -rf datasource-master.xml datasource-slave.xml redis.properties
            #重启实例
            if [ $STRUCTURE == 1 ];then
                    sudo /etc/init.d/tomcat_9001 stop
                    sudo /etc/init.d/tomcat_9001 start
            elif [ $STRUCTURE == 2 ];then
                    sudo /etc/init.d/tomcat_9001 stop
                    sudo /etc/init.d/tomcat_9001 start
            fi
            echo -e "\033[36mcms实例已更新重启\033[0m"
        fi
}

# live_work_9002
function MODIFY_LIVE_WORK(){
        if [ ! -e $LIVE_WORK/redis.properties ];then
            echo -e "\n\033[31mlive-work实例文件找不到，请检查\033[0m\n"
        else
            cp $LIVE_WORK/spring/{datasource-master.xml,datasource-slave.xml} $TEMP/
            cp $LIVE_WORK/redis.properties $TEMP/
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_MASTERIP#g" $TEMP/datasource-master.xml
            sed -i -r "s#mysql://([0-9]{1,3}\.){3}[0-9]{1,3}#mysql://$NEW_SLAVEIP#g" $TEMP/datasource-slave.xml
            sed -i -r "s:hostname=([0-9]{1,3}\.){3}[0-9]{1,3}:hostname=$NEW_MASTERIP:g" $TEMP/redis.properties
            sudo -u ybdeploy cp $TEMP/datasource-master.xml $LIVE_WORK/spring/datasource-master.xml
            sudo -u ybdeploy cp $TEMP/datasource-slave.xml $LIVE_WORK/spring/datasource-slave.xml
            sudo -u ybdeploy cp $TEMP/redis.properties $LIVE_WORK/redis.properties
            cd $TEMP && rm -rf datasource-master.xml datasource-slave.xml redis.properties
            #重启实例
            if [ $STRUCTURE == 1 ];then
                    sudo /etc/init.d/tomcat_9002 stop
                    sudo /etc/init.d/tomcat_9002 start
            elif [ $STRUCTURE == 2 ];then
                    sudo /etc/init.d/tomcat_9002 stop
                    sudo /etc/init.d/tomcat_9002 start
            fi
            echo -e "\033[36mlive_work实例已更新重启\033[0m"
        fi
}

#############################################################################
while true; do
    echo -e "\033[36m \t\t\t+---------------------------------------------+\t\t\t \033[0m"  
    echo -e "\033[36m \t\t\t|      请选择您要更改mysql ip的tomcat实例     |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t+---------------------------------------------+\t\t\t \033[0m"  
    echo -e "\033[36m \t\t\t|           (1) admin——7001                   |\t\t\t \033[0m"  
    echo -e "\033[36m \t\t\t|           (2) work——7002                    |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t|           (3) agent——7003                   |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t|           (4) web——8001                     |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t|           (5) anls_api——8002                |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t|           (6) cms——9001                     |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t|           (7) live_work——9002               |\t\t\t \033[0m"   
    echo -e "\033[36m \t\t\t|           (8) ALL(所有实例)                 |\t\t\t \033[0m" 
    echo -e "\033[36m \t\t\t|           (0) 退出菜单                      |\t\t\t \033[0m"
    echo -e "\033[36m \t\t\t+---------------------------------------------+\t\t\t \033[0m"
        read -p "输入您所要更换的tomcat实例(1/2/3/4/5/6/7/8/0)：" MODE

        case $MODE in
                0)
                        rm -rf $TEMP
                        exit
                ;;
                1)
                        MODIFY_ADMIN
                        rm -rf $TEMP
                        exit
                ;;
                2)
                        MODIFY_WORK
                        rm -rf $TEMP
                        exit
                ;;
                3)
                        MODIFY_AGENT
                        rm -rf $TEMP
                        exit
                ;;
                4)
                        MODIFY_WEB
                        rm -rf $TEMP
                        exit
                ;;
                5)
                        MODIFY_ANLS_API
                        rm -rf $TEMP
                        exit
                ;;
                6)
                        MODIFY_CMS
                        rm -rf $TEMP
                        exit
                ;;
                7)
                        MODIFY_LIVE_WORK
                        rm -rf $TEMP
                        exit
                ;;
                8)
                        MODIFY_ADMIN
                        MODIFY_WORK
                        MODIFY_AGENT
                        MODIFY_WEB
                        MODIFY_ANLS_API
                        MODIFY_CMS
                        MODIFY_LIVE_WORK
                        rm -rf $TEMP
                        exit
                ;;
                *)
                        rm -rf $TEMP
                        exit
                ;;
        esac
done
