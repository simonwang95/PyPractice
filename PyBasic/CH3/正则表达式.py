# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 01:01:17 2018

@author: 10696
"""

'''
给定一个正则表达式，如下：

      [1-9]\d{5}

请获得输入的字符串，提取其中所有匹配字符串，对于每个匹配结果按照一行输出，包括：匹配字符串、在原字符串中的起始位置和结束位置，格式如下：

<匹配字符串>:<起始位置>,<结束位置>
北京理工大学100081 清华大学100084
'''
import re
s = input()
regex = re.compile(r"[1-9]\d{5}")
ls = regex.finditer(s.strip("\n"))
#print(ls)
#print(s)
for i in ls:
    w = i.group(0)
    a = i.start()
    b = i.end()
    print('{}:{},{}'.format(w, a, b))