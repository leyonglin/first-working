# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:24:16 2019

@author: bangde
"""

#百思不得其姐,多线程
#xpath表达式：//div[@class="j-r-list-c-desc"]/a/text()
import requests
from lxml import etree
from queue import Queue
import threading
import time

class bsSpider:
    def __init__(self):
        self.baseurl = "http://www.budejie.com/"
        self.headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
        #URL队列
        self.urlQueue = Queue()
        #响应html队列
        self.resQueue = Queue()
    
    
    #生成URL队列
    def getUrl(self):
        for pNum in range(1,11):
            url = self.baseurl + str(pNum)
            self.urlQueue.put(url)
    
    #请求,得到响应html，放到解析队列
    def getHtml(self):
        while True:
            #1.从url队列中get值
            url = self.urlQueue.get()
            #2.发请求，得响应，put到响应队列
            res = requests.get(url,headers=self.headers)
            res.encoding="utf-8"
            html=res.text
            #放到响应队列
            self.resQueue.put(html)
            #清除此任务
            self.urlQueue.task_done()
    
    #解析页面方法
    def getText(self):
        while True:
            html = self.resQueue.get()
            parseHtml = etree.HTML(html)
            r_list=parseHtml.xpath('//div[@class="j-r-list-c-desc"]/a/text()')
            for r in r_list:
                print(r+"\n")
            #清除任务
            self.resQueue.task_done()
                
    def run(self):
        #空列表，用来存放所有线程
        thlist = []
        #生成URL队列
        self.getUrl()
        #创建请求线程，放到列表中
        for i in range(3):
            thRes = threading.Thread(target=self.getHtml)
            thlist.append(thRes)
            
        #创建解析线程，放到列表中
        for i in range(3):
            thparse = threading.Thread(target=self.getText)
            thlist.append(thparse)
        
        #所有线程开始执行
        for th in thlist:
            th.setDaemon(True)
            th.start()
        
        #如果队列为空，则执行其它程序
        self.urlQueue.join()
        self.resQueue.join()

if __name__=="__main__":
    begin = time.time()
    spider = bsSpider()
    spider.run()
    end = time.time()
    print(end-begin)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    