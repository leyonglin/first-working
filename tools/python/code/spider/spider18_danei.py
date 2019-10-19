# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:01:00 2019

@author: bangde
"""

import requests
import pymysql
import re

class NoteSpider():
    def __init__(self):
        self.url="http://code.tarena.com.cn/"
        self.headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
        #web客户端验证参数(元组)
        self.auth = ("tarenacode","code_2013")
    
        #库对象
#        self.db = pymysql.connect("ip","user","password","database",charset="utf8")
        self.db = pymysql.connect("192.168.3.3","root","123456","spiderdb",charset="utf8")
        #游标对象
        self.cursor = self.db.cursor()
        
        
    #获取并解析页面
    def getPrasePage(self):
        #三部获取网页内容
        res =requests.get(self.url,auth=self.auth,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        #正则编译对象，两部过滤内容
#            p = re.compile('正则',re.S) #re.S匹配 “\n”
        p =re.compile('<a href="(.*?)/.*?</a>',re.S)
        rlist = p.findall(html)
        
        self.writePage(rlist)
    
    #保存数据
    def writePage(self,rlist):
#        ctab = "create table if not exists tarenaNote(name  varchar(20))"
#        self.cursor.execute(ctab)
        ins = 'insert into tarenaNote(name) values(%s)'
        for r in rlist:
            #如果有其它数据，可以用if判断并过滤
            self.cursor.execute(ins,[r])
            self.db.commit()
        self.cursor.close()
        self.db.close()




if __name__=="__main__":
    spider = NoteSpider()
    spider.getPrasePage()
    print("ok")