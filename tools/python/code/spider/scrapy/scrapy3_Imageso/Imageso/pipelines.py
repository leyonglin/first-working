# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#定义了图片管道类
import scrapy
from scrapy.pipelines.images import ImagesPipeline

#class要集成图片管道类
class ImagesoPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        #获取requests的方法
        yield scrapy.Request(url=item['imageUrl'])
