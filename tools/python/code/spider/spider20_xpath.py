# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:59:12 2019

@author: 59748
"""
from lxml import etree

html = '''
<div class="wrapper">
    <i class="iconfont icon-back" id="back"></i>
    <a href="/" id="channel">新浪社会</a>
    <ul id="nav">
        <li><a href="https://blog.csdn.net/notbaron/article/details/61423957" title="blog">blog</a></li>
        <li><a href="https://www.toutiao.com" title="今日头条">今日头条</a></li>
        <li><a href="view-source:https://www.toutiao.com/" title="source">source</a></li>
    </ul>
    <i class="iconfont icon-liebiao" id="menu"></i>
</div>


'''

#创建解析对象(etree.HTML())
parseHtml = etree.HTML(html)
#解析对象调用xpath()
#1.匹配出所有的href的值
r1 = parseHtml.xpath("//a/@href")
print(r1)
#2.把href中的/匹配出来
r2=parseHtml.xpath('//div[@class="wrapper"]/a/@href')
print(r2)
#3.把href中的非/匹配出来
r3=parseHtml.xpath('//ul[@id="nav"]/li/a/@href')
#r3=parseHtml.xpath('//ul[@id="nav"]//a/@href')
print(r3)
#4.获取所有a节点的文本内容
#r4=parseHtml.xpath('//a')
r4=parseHtml.xpath('//a/text()')
print(r4)
#5.获取所有a节点文本内容（不包括最上面的新浪社会）
#r5=parseHtml.xpath('//ul[@id="nav"]/li/a')
r5=parseHtml.xpath('//ul[@id="nav"]/li/a/text()')
print(r5)




