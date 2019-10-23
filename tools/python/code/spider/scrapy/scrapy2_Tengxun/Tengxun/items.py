# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TengxunItem(scrapy.Item):
    # define the fields for your item here like:
    # 按规律命名
    zhName = scrapy.Field()
    zhAddress = scrapy.Field()
    zhXin = scrapy.Field()
    zhDai = scrapy.Field()
    zhLink = scrapy.Field()
