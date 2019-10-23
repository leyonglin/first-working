# -*- coding: utf-8 -*-

#创建命令：scrapy genspider tengxun bj.58.com

import scrapy
from Tengxun.items import TengxunItem


class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['bj.58.com']
    #url是一个列表，具体可以看scrapy.Spider中的start_requests方法
    url = "https://bj.58.com/kefu/pn"
    start_urls = [url + str(1)]

    def parse(self, response):
        # 把70页的url地址斗个调度器入队列
        for i in range(1, 71):
            url = self.url + str(i)
            # scrapy.Request(),yield输出到调度器,说明url需要parseHtml函数进行解析（即返回response的时候先经过parseHtml）
            yield scrapy.Request(url, callback=self.parseHtml)

    def parseHtml(self, response):
        # 下载器下载完返回的response定义处理
        # 创建item对象
        item = TengxunItem()
        # 每个职位节点对象列表
        baseList = response.xpath('//ul[@id="list_con"]/li')
        for base in baseList:
            item['zhName'] = base.xpath('//span[@class="name"]/text()').extract()[0]
            item['zhAddress'] = base.xpath('//span[@class="address"]/text()').extract()
            if item['zhAddress']:
                item['zhAddress'] = item['zhAddress'][0]
            else:
                item['zhAddress'] = "无"
            item['zhXin'] = base.xpath('//p[@class="job_salary"]/text()').extract()[0]
            item['zhDai'] = base.xpath('//div/span[2]/text()').extract()[0]
            #链接的提取有问题
            item['zhLink'] = base.xpath('//a/@href').extract()[0]
            yield item

        # item['zhName'] = response.xpath('//ul[@id="list_con"]/li//span[@class="name"]/text()').extract()[0]
        # item['zhAddress'] = response.xpath('//ul[@id="list_con"]/li//span[@class="address"]/text()').extract()[0]
        # item['zhXin'] = response.xpath('//ul[@id="list_con"]/li//p[@class="job_salary"]/text()').extract()[0]
        # item['zhDai'] = response.xpath('//ul[@id="list_con"]/li//div/span[2]/text()').extract()[0]
        # item['zhLink'] = response.xpath('//ul[@id="list_con"]/li//a/@href').extract()[0]
        # yield item

##使用redis_key配置
##class TengxunSpider(scrapy.Spider):
##    name = 'tengxun'
##    allowed_domains = ['bj.58.com']
##    #发送命令，分布式服务器执行爬取命令（scrapy crawl tengxun）后等待redis执行lpush mycrawler:start_urls URL(就是爬取程序的redis_key)统一开始爬取
##    redis_key = 'mycrawler:start_urls'
##    ##动态获取域限制(allowed_domains,这样才能跨域名爬取)，但是和allowed_domains只能二选一
##    def __init__(self, *args, **kwargs):
##        # Dynamically define the allowed domains list.
##        domain = kwargs.pop('domain', '')
##        self.allowed_domains = filter(None, domain.split(','))
##        super(MyCrawler, self).__init__(*args, **kwargs)






