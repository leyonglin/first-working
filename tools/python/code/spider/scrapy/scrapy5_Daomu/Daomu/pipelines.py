# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from Daomu.settings import *
class DaomuPipeline(object):
    def process_item(self, item, spider):
        print('+++++++++++++++++')
        print(item['title'])
        print(item['zhNum'])
        print(item['zhName'])
        print(item['zhlink'])
        return item

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