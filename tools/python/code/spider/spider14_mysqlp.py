# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:18:17 2019

@author: bangde
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:29:12 2019

@author: 59748
"""
#找url规律
    #https://maoyan.com/board/4?offset=0
    #https://maoyan.com/board/4?offset=10
#写正则表达式
    #<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>
#写代码
import urllib
import re
import pymysql
import warnings


class NeihanSpider():
    def __init__(self):
        self.baseurl = "https://maoyan.com/board/4?offset="
        self.headers={"User-Agent":"Mozilla/5.0"}
        self.page=0
        
        self.db = pymysql.connect("192.168.3.3","root","123456","spiderdb",charset="utf8")
        self.cursor = self.db.cursor()
        
    #获取页面
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        #调用解析函数
        self.parsePage(html)
        
    #解析页面
    def parsePage(self,html):
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>',re.S)
        #匹配结果[("问题":"答案"),...]
        rlist=p.findall(html)
        self.writeTomysql(rlist)
    
    #保存csv数据
    def writeTomysql(self,rlist):
        #忽略警告
        warnings.filterwarnings("ignore")
        #有占位，需要传列表参数
        ins = 'insert into film(name,start,time) values(%s,%s,%s)'
        print("ok")
        #for好像时好时坏
        for r in rlist:
            L = [r[0].strip(),r[1].strip(),r[2].strip()]
#            print("ok")
            self.cursor.execute(ins,L)
            self.db.commit()
                 

    #主函数
    def workOn(self):
        self.getPage(self.baseurl)
        while True:
            c = input("成功，是否继续(y/n):")
            if c.strip().lower() == "y":
                url = self.baseurl + str(self.page)
                self.getPage(url)
                self.page += 10
#                for i in range(0.91,10):
#                    url = self.baseurl + str(self.page)
#                    self.getPage(url)
            else:
                print("爬取结束")
                self.cursor.close()
                self.db.close()
                break
    
if __name__=="__main__":
    spider = NeihanSpider()
    spider.workOn()