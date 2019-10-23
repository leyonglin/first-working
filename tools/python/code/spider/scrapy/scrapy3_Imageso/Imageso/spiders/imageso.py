# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
import json
from Imageso.items import ImagesoItem


class ImagesoSpider(scrapy.Spider):
    name = 'imageso'
    allowed_domains = ['image.so.com']
    # start_urls = ['http://image.so.com/']
    #重写start_requests()方法,可以不使用start_urls
    def start_requests(self):
        baseurl = 'http://image.so.com/zjl?'
        for pg in range(0,91,30):
            params = {
                'ch': 'photography',
                't1': '226',
                'sn': pg,
                'listtype': 'new',
                'temp': '1',
            }
            params = urlencode(params)
            fullUrl = baseurl + params
            yield scrapy.Request(fullUrl,callback=self.parse)


    def parse(self, response):
        item = ImagesoItem()
        #response.text是json格式的字符串 --> 字典
        imaList=json.loads(response.text)['list']
        for img in imaList:
            item['imageName'] = img['title']
            item['imageUrl'] = img['qhimg_url']
            yield item