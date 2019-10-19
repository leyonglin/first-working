# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:11:08 2019

@author: bangde
"""

#导入selenium中得webdriver
from selenium import webdriver



#设置chrome为无界面浏览器
#opt = webdriver.ChromeOptions()
#设置无界面浏览器
#opt.set_headless()
#设置分辨率
#opt.add_argument('windows-size=1920x3000')   

#创建浏览器对象
#driver = webdriver.Chrome(options=opt)    #没参数默认是有界面的，会自动打开浏览器
#窗口最大化
#driver.maximize_window()


#创建phantomjs浏览器对象，警告是因为selenium现在对phantomjs支持不友好，推荐用谷歌或火狐
driver = webdriver.PhantomJS(executable_path='C:\\Users\\bangde\\Desktop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
#存放到python安装目录得Script目录下，可以不用路径
#driver = webdriver.PhantomJS()



#发请求，在内存在打开一个网页
driver.get('http://www.baidu.com')

#获取网页源码
print(driver.page_source)

#获取网页截屏
driver.save_screenshot('百度.png')

#关闭浏览器
driver.quit()





#from selenium import webdriver
#
##创建phantomjs浏览器对象，警告是因为selenium现在对phantomjs支持不友好，推荐用谷歌或火狐
#driver = webdriver.PhantomJS(executable_path='C:\\Users\\bangde\\Desktop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
#
##打开内涵段子
#driver.get('https://www.neihan8s.com/njjzw//')
#
##单节点
#rOne = driver.find_element_by_class_name('text-column-item')
#print(rOne.text)
#
##多节点
#rlist=driver.find_elements_by_class_name('text-column-item')
#for r in rlist:
#    print(r.text)
#    print('*' * 40)