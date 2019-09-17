# -*- coding:utf-8 -*-
# create database dbforpymysql charset="utf8";
# create table userinfo(id int,name varchar(30),age int(10));
# insert into userinfo(id,name,age) values (1,"frank",123);
import pymysql
# import hashlib from sha1   #加密模块
#连接数据库

db = pymysql.connect(host="192.168.3.3",user="root",passwd="123456",\
                     database="dbforpymysql",charset="utf8",port=3306)
#使用cursor()方法创建一个游标对象
cursor = db.cursor()
#使用execute()方法执行SQL语句
# cursor.execute("SELECT * FROM userinfo")
try:                                                     #顺序执行，出现错误则不会往下执行
    # set_id = input("输入id：")
    # set_name = input("输入名字：")
    sql = "delete from userinfo where name='林乐勇'"        #汉字用单引号引起来
    cursor.execute(sql)
    print("delete ok")
    # sql = "INSERT INTO userinfo(id,name,age) VALUES(%s,%s,'123')"   #占位符%s
    sql = "INSERT INTO userinfo(id,name,age) VALUES('123','123','123')"
    cursor.execute(sql,[set_id,set_name])                           #列表参数
    print("insert ok")
    sql = "select * from userinfo"
    cursor.execute(sql)
    print("select ok")
    db.commit()
except Exception as e:
    db.rollback()
    print("failed",e)
#使用fetall()获取全部数据，fetchone()获取第一条查询数据，fetchmany(n)获取那条数据
data = cursor.fetchall()
dataone = cursor.fetchone()
#打印获取到的数据
print(data)                   #返回数据类型为元组嵌套
print("fetchont:",dataone)    #fetch的数据，取一条，少一条，类似迭代器
#提交到数据库
# db.rollback()
db.commit()
print('ok')
#关闭游标和数据库的连接
cursor.close()
db.close()
#运行结果
