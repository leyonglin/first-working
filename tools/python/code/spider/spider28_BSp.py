# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:27:36 2019

@author: bangde
"""

import requests
from bs4 import BeautifulSoup

url = "http://www.budejie.com"
headers={"User-Agent":"Mozilla/5.0"}

#获取源码
res = requests.get(url,headers=headers)
res.encoding="utf-8"
html = res.text

#创建解析对象并解析
soup = BeautifulSoup(html,'lxml')
r_list = soup.find_all("div",attrs={"class":"j-r-list-c-desc"})

#for循环遍历
for r in r_list:
    print(r.a.string)