# -*- coding: utf-8 -*-

#抓取百度贴吧多页内容
import urllib.request
import urllib.parse
import random

hlist = [
        {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"},
        {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"},
        {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
        ]

headers = random.choice(hlist)
baseurl = "http://tieba.baidu.com/f?"

name = input("请输入贴吧名称：")
begin = int(input("请输入起始页:"))
end = int(input("请输入终止页："))

kw = urllib.parse.urlencode({"kw":name})
for page in range(begin,end+1):
    pn = (page - 1) * 50
    url = baseurl +kw +"&pn=" +str(pn)
    #print(url)
    
    req = urllib.request.Request(url,headers={})
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    
    filename = "第" + str(page) + ".html"
    with open(filename,"w",encoding="gb18030") as f:
        f.write(html)
    print("第%d页爬取成功" % page)