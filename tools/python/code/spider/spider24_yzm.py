# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:02:42 2019

@author: bangde
"""

from selenium import webdriver

#创建浏览器对象
driver = webdriver.PhantomJS(executable_path='C:\\Users\\bangde\\Desktop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')

#发请求，获取响应
driver.get('http://www.renren.com')

#输入用户名
uname = driver.find_element_by_name('email')
uname.send_keys('18633615542')

#输入密码
pwd = driver.find_element_by_name('password')
pwd.send_keys('zhanshen001')

#验证码，屏幕截图，从终端输入验证码，发送
driver.save_screenshot('yzm.png')
yzm = input("请输入验证码")
driver.find_element_by_name('icode').send_keys(yzm)

#登陆按钮点击
driver.find_element_by_id('login').click

#屏幕截图
driver.save_screenshot('成功.png')

#关闭浏览器
driver.quit()