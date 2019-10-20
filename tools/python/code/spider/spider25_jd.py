# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:07:06 2019

@author: 59748
"""

from selenium import webdriver
import time
#创建浏览器对象
driver = webdriver.PhantomJS(executable_path='C:\\Users\\59748\\Desktop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')

#访问京东首页
driver.get('https://www.jd.com')

#找到搜索框按钮，接收终端输入，发送到搜索框
text = driver.find_element_by_class_name('text')
key = input('输入搜索内容')
text.send_keys(key)
#点击搜索按钮
button = driver.find_element_by_class_name('button')
button.click()
time.sleep(3)
#提取数据，分析数据
while True:
    #执行脚本，进度条拉到最底部
    driver.execute_script('window.srollTo(0,document.body.scrollHeight)')
    
    rlist=driver.find_elements_by_xpath('//div[@id="J_goodsList"]//li')
    for r in rlist:
        contentlist=r.text.split('\n')
        price = contentlist[0]
        name = contentlist[1]
        commit = contentlist[2]
        market = contentlist[3]
        d = {
                "价格":price,
                "名称":name,
                "评论":commit,
                "商家":market,
                }
        with open("jd.json","a",encoding="utf-8") as f:
            f.write(str(d) + "\n")
        
        #点击下一页
        if driver.page_source.find('pn-next disabled') == -1:
            driver.find_element_by_class_name('pn-next').click()
        else:
            print("爬取结束")
            break
        
    
driver.quit()