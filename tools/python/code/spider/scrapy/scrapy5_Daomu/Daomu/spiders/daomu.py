# -*- coding: utf-8 -*-
import scrapy
from Daomu.items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-1']

    def parse(self, response):
        item = DaomuItem()
        allm = response.xpath('//article/a/text()').extract()
        i=0
        for r in allm:
            item['title'] = r.split()[0]
            item['zhNum'] = r.split()[1]
            item['zhName'] = r.split()[2]
            item['zhlink'] = response.xpath('//article/a/@href').extract()[i]
            i+=1
            yield item

