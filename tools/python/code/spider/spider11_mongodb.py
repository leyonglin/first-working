# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:13:58 2019

@author: bangde
"""

#mongodb常用语句
#show dbs
#use spiderdb
#show collections
#db.t1.find().pretty()
#db.t1.count()
#db.dropDatabase()


import pymongo

DBNAME="spiderdb1"
TABNAME="t11"


#创建数据库连接对象
conn = pymongo.MongoClient("192.168.3.3",27017)

#创建库对象
#db = conn.spiderdb
#使用变量
db = conn[DBNAME]

#创建集合对象
#myset = db.t1
myset = db[TABNAME]

#在t1集合中插入1条文档
myset.insert_one({"name":"Tom11"})
#出现TypeError: 'Collection' object is not callable 错误，执行下面语句
#myset.insert({"name":"Tom"})

print("success")


