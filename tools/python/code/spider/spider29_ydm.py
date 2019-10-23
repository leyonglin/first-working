# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:25:23 2019

@author: bangde
"""
import requests
from selenium import webdriver
from lxml import etree 
import time
from PIL import Image
from pytesseract import *
#ydm
from YDMPT import *

#访问网站得到driver.page.source
url="https://www.douban.com"
headers=''
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

#把验证码图片的链接提取出来，并发请求保存到本地
parseHtml=etree.HTML(driver.page_source)
rlink = parseHtml.xpath('//img[@id="captcha_image"]')[0]
res = requests.get(rlink,headers=headers)
res.encoding = "utf-8"
html = res.content
with open("验证码.jpg","wb") as f:
    f.write(html)

#ydm把图片转为字符串,信息在YMDPT中设置
cid, result = yundama.decode(filename, codetype, timeout);
print(result)

#用户名，密码，验证码，登陆豆瓣
uname = driver.find_element_by_name('form_email')
uname.send_keys('309435365@qq.com')
pwd = driver.find_element_by_name('form_password')
pwd.send_keys('zhanshen001')
yzm=driver.find_element_by_id(captcha_field')
yzm.send_keys(result)
time.sleep(10)
login=driver.find_element_by_class_name('bn-submit')
login.click()
time.sleep(2)

driver.quit()








