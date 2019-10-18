# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:17:01 2019

@author: bangde
"""

import urllib
import re
import pymongo

DBNAME="spiderdb2"
TABNAME="t12"

class NeihanSpider():
    def __init__(self):
        self.baseurl = "https://maoyan.com/board/4?offset="
        self.headers={"User-Agent":"Mozilla/5.0"}
        self.page=0
        #对象操作可以在初始化时建立,有报错，不知道哪里出问题了
        self.conn = pymongo.MongoClient("192.168.3.3",27017)
        self.db = self.conn[DBNAME]
        self.myset = self.db[TABNAME]
        print("ok")
        
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
        self.writeTomongo(rlist)
    
    #保存csv数据
    def writeTomongo(self,rlist):
#        #对象操作可以在初始化时建立
#        conn = pymongo.MongoClient("192.168.3.3",27017)
#        db = conn[DBNAME]
#        myset = db[TABNAME]
#        这里的for循环一直无法执行，不知道为什么
        for r in rlist:
            print("ok")
            d = {
                    "name":r[0].strip(),
                    "star":r[1].strip(),
                    "time":r[2].strip()
                    }
            self.myset.insert(d)
#        self.myset.insert_one({"name":"Tom"})
        print("成功存入mongo库")
        
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
                break
    
if __name__=="__main__":
    spider = NeihanSpider()
    spider.workOn()
#














