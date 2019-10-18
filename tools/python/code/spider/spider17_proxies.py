# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:51:31 2019

@author: bangde
"""

import requests
url="http://httpbin.org/get"
headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
#普通代理proxies = proxies={"协议":"协议://IP:端口号"}
proxies = {"http":"http://183.207.229.140:8090"}
#私密代理proxies = {"http":"http://用户名:密码@IP地址:端口号"}
proxies = {"http":"http://309435365:szayclhp@112.74.108.33:16818"}

res=requests.get(url,proxies=proxies,headers=headers,timeout=3)
res.encoding = "utf-8"
html = res.text
print(html)