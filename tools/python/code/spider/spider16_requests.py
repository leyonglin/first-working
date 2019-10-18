# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:38:17 2019

@author: bangde
"""

import requests

url="http://www.baidu.com"
headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
#发请求获取响应对象
res = requests.get(url,headers=headers)

#获取编码格式
print(res.encoding)

#获取res的内容(字符串类型)
res.encoding="utf-8"
print(type(res.text))

#获取res的内容(bytes类型)
print(type(res.content))

#获取HTTP响应码
print(res.status_code)

#获取返回实际数据的URL地址
print(res.url)


