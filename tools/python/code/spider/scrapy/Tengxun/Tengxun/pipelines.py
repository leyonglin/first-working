# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from settings import *
import pymysql



# class TengxunPipeline(object):
#     def process_item(self, item, spider):
#         print('---------------------------')
#         print(item['zhName'])
#         print(item['zhAddress'])
#         print(item['zhXin'])
#         print(item['zhDai'])
#         print(item['zhLink'])
#         print('---------------------------')
#         return item



class MysqlPipeline(object):
    def __init__(self):
        #数据库连接对象
        self.db=pymysql.connect(host=MYSQL_HOST,user=MYSQL_USER,password=MYSQL_PWD,database=MySQL_DB,charset="utf8")
        #游标对象
        self.cursor=self.db.cursor()




    def process_item(self, item, spider):
        ins = 'insert into jobs values(%s,%s,%s,%s,%s)'
        L = [item['zhName'],
             item['zhAddress'],
             item['zhXin'],
             item['zhDai'],
             item['zhLink'],
             ]
        self.cursor.execute(ins,L)
        self.db.commit()
        return  item
    #process_item处理完成后会执行此方法
    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
        print("mysql数据库断开连接")



# class MongoPipeline(object):
#     def __init__(self):
#         self.conn = pymongo.MongoClient(host=MONGODB_HOST,port=MONGODB_PORT)
#         self.db = self.conn[MONGODB_DB]
#         self.myset=self.db[MONGODB_SET]
# 
#     def process_item(self, item, spider):
#         #将item转换成字典
#         d = dict(item)
#         self.myset.insert_one(d)
# 
#         return item














