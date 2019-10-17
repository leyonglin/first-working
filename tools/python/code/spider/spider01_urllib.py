# -*- coding: utf-8 -*-
#urllib模块爬取数据
import urllib.request

#利用Request()方法构建请求对象
url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
req = urllib.request.Request(url,headers={})

#利用urlopen()方法获取响应对象
res = urllib.request.urlopen(req)

#利用响应对象的read().decode("utf-8")获取内容
html = res.read().decode("utf-8")
#print(html)

#获取响应码
print(res.getcode())

#获取实际数据URL
print(res.geturl())