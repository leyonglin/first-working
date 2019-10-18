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
import csv

class NeihanSpider():
    def __init__(self):
        self.baseurl = "https://maoyan.com/board/4?offset="
        self.headers={"User-Agent":"Mozilla/5.0"}
        self.page=0
        
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
        self.writeToCsv(rlist)
    
    #保存csv数据
    def writeToCsv(self,rlist):
        for r in rlist:
#            r = list(r)
            #去掉空格
            r=[r[0].strip(),r[1].strip(),r[2].strip()]
            with open("maoyan.csv","a",newline="",encoding="gb18030") as f:
                writer = csv.writer(f)
                writer.writerow(r)
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