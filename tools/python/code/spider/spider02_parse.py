# -*- coding: utf-8 -*-
#url转码
#请求模块
import urllib.request
#url地址编码模块
import urllib.parse

headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
baseurl = "http://www.baidu.com/s?"
#接收用户从终端输入
key = input("请输入要搜索的内容\n")
#进行urlencode编码,字典内有多个参数，会自动用&拼接起来
key = urllib.parse.urlencode({"wd":key})
#拼接url
url = baseurl + key 


req = urllib.request.Request(url,headers={})
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")

#保存到本地文件
with open("美女.html","w",encoding="gb18030") as f:
    f.write(html)