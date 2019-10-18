# -*- coding: utf-8 -*-
import urllib
import re
#1.url规律
#    第一页：https://www.neihan8s.com/njjzw/
#    第二页：https://www.neihan8s.com/njjzw//index_2.html
#2.用正则匹配出内容
#    内容：	<div class="text-column-item box box-790">
#            <h3><a href="/njjzw/164041.html" class="title" title="1234567890哪个数字最勤劳，哪个数字最懒惰?">1234567890哪个数字最勤劳，哪个数字最懒惰?</a></h3>
#            <div class="desc"> 　　1懒惰;2勤劳。(1不做2不休)</div>
#    正则：<div class="text-column-item box box-790">.*?title="(.*?)".*?<div class="desc">(.*?)</div>
#3.写代码
class NeihanSpider():
    def __init__(self):
        self.baseurl = "https://www.neihan8s.com/njjzw/"
        self.headers={"User-Agent":"Mozilla/5.0"}
        self.page = 2
        
    #获取页面
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        #调用解析函数
        self.parsePage(html)
        
    #解析页面
    def parsePage(self,html):
        p = re.compile('<div class="text-column-item box box-790">.*?title="(.*?)".*?<div class="desc">(.*?)</div>',re.S)
        #匹配结果[("问题":"答案"),...]
        rlist=p.findall(html)
        self.writePage(rlist)
    
    #保存数据
    def writePage(self,rlist):
        for rtuple in rlist:
            with open("内涵.txt","a") as f:
                f.write(rtuple[0].strip()+"\n") 
                f.write(rtuple[1].strip()+"\n\n")
    
    #主函数
    def workOn(self):
        self.getPage(self.baseurl)
        while True:
            c = input("成功，是否继续(y/n):")
            if c.strip().lower() == "y":
                url = self.baseurl + "index_" + str(self.page) + ".html"
                self.getPage(url)
                self.page += 1
            else:
                print("爬取结束")
                break
    
if __name__=="__main__":
    spider = NeihanSpider()
    spider.workOn()