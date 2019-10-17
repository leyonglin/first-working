# -*- coding: utf-8 -*-

import re

#html = """
#<div><p>和换行i</p></div>
#<div><p>立刻就顺丰单号</p></div>
#"""
#创建编译对象,非贪婪匹配在.*之后加一个?号
#p = re.compile('<div><p>.*?</p></div>',re.S)
#r = p.findall(html)
#print(html)


##分组
#s="A B C D"
#p1 = re.compile('\w+\s+\w+')
#print(p1.findall(s))
#
##先整体匹配，再从每组中输出分组
#p2 = re.compile('(\w+)\s+\w+')
#print(p2.findall(s))
#
#p3 = re.compile('(\w+)\s+(\w+)')
#print(p3.findall(s))


#代码匹配
html="""<div class="animal">
    <p class="name">
       <a title="Rabbit"></a>
    </p>
                
    <p class="content">
       small white rabbit white and white
    </p>"""
#print(html)  
#这里匹配，就相当于从开头匹配到结尾，
#<div class="animal">匹配一段字符串  .*?非贪婪匹配  title="匹配字符串  (.*?)分组/输出  .*?  class="content">  (.*?)  </p>           
p = re.compile('<div class="animal">.*?title="(.*?).*?class="content">(.*?)</p>',re.S)
rlist = p.findall(html)
#print(rlist)
for r in rlist:
    print("*" * 30)
    print("动物名称：%s" % r[0].strip())
    print("动物描述：%s" % r[1].strip())
    print("*" * 30)