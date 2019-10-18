# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:51:45 2019

@author: bangde
"""

import pymysql
#处理警告的模块
import warnings

#过滤警告,ignore忽略警告
warnings.filterwarnings("ignore")


#创建数据连接对象
db = pymysql.connect("192.168.3.3","root","123456",charset="utf8")

#创建游标对象
cursor = db.cursor()

#利用游标对象的execute()方法执行命令
cdb = "create database if not exists spiderdb charset utf8"
udb = "use spiderdb"
ctab = "create table t1(id int)"
ins = "insert into t1 values(1)"
cursor.execute(cdb)
cursor.execute(udb)
cursor.execute(ctab)
cursor.execute(ins)

#提交到数据库执行
db.commit()

#关闭游标
cursor.close()

#断开数据库连接
db.close()