# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:21:48 2019

@author: bangde
"""

#cookie
import urllib.request

url="登陆后查看的网址"
#F12 -- Request Headers(携带cookie)全部复制
headers = {"":"",...}
req = urllib.request.Request(url,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")
print(html)