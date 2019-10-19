# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:32:35 2019

@author: bangde
"""
from selenium import webdriver
import time

#创建phantomjs浏览器对象，警告是因为selenium现在对phantomjs支持不友好，推荐用谷歌或火狐
driver = webdriver.PhantomJS(executable_path='C:\\Users\\bangde\\Desktop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')

#打开百度
driver.get('http://www.baidu.com')

#找到搜索框，发送文字,id是因为搜索框有一个属性是id，一般填id/name/class
driver.find_element_by_id("kw").send_keys('美女')

#找到百度一下按钮，点击一下
driver.find_element_by_id('su').click()
#等待页面加载出来
time.sleep(3)

#截图
driver.save_screenshot('百度.png')

#关闭浏览器
driver.quit()
