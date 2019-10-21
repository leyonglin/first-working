# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:19:46 2019

@author: bangde
"""

from bs4 import BeautifulSoup

html='''
<div class="fengyun">雄霸</div>
<div class="fengyun">fengcui</div>
<div class="fengyun2">
    <span>第二梦</span>
    <p>第三梦</p>
</div>
'''

#创建解析对象
soup = BeautifulSoup(html,'lxml')
r_list = soup.find_all("div",attrs={"class":"fengyun"})


#找到所有class为fengyun的div节点的文本
r_list = soup.find_all("div",attrs={"class":"fengyun"})
for r in r_list:
    #获取内容
    print(r.get_text())
#    print(r.string)
    

#找到class为fengyun2的div节点下span节点的文本
r_list = soup.find_all("div",attrs={"class":"fengyun2"})
for r in r_list:
    print(r.span.string)
    print(r.p.string)




