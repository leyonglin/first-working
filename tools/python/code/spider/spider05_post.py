# -*- coding: utf-8 -*-

#POST，有道翻译获取结果
import urllib.request
import urllib.parse
import json


#接收用户输入
#key = input("请输入要翻译的内容：")
key = "hello"
#把Form Data定义成一个大字典(F12)
data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15713065230380",
        "sign": "a096c515c7aa9cda0421221cbc6ebf24",
        "ts": "1571306523038",
        "bv": "e218a051a7336600dfed880d272c7d6f",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
        }

#把data转为bytes数据类型
data = urllib.parse.urlencode(data).encode(encoding="utf-8")

#发请求，获取响应，得到内容
#此处url地址为F12抓到的POST的地址
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers={"User-Agent":"Mozilla/5.0"}
req = urllib.request.Request(url,data=data,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")
#print(html)

#把json格式的字符串转为python中的字典
rDict = json.loads(html)
print("输入的内容：%s\n输出结果：%s" % (rDict["translateResult"][0][0]["src"],rDict["translateResult"][0][0]["tgt"]))