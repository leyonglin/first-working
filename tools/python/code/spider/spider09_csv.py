# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 02:01:08 2019

@author: 59748
"""

import csv

#打开csv文件
with open("test.csv","a",newline="",encoding="utf-8") as f:
#    初始化写入对象
    writer = csv.writer(f)
#   写入数据
    writer.writerow(["lin",28])
    writer.writerow(["wang",18])