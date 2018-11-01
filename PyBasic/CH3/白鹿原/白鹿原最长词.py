# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:22:34 2018

@author: 10696
"""

import os
import jieba

os.chdir('C:\\Users\\10696\\Desktop\\project\\PyBasic\\')
f = open('白鹿原.txt', encoding = 'utf8')
ls = jieba.lcut(f.read())

'''
白鹿原最长单词
ls = jieba.lcut(f.read())
A = set(ls)
maxw = ''
for w in A:
    if len(w) > len(maxw):
        maxw = w
    if len(w) == len(maxw) and w > maxw:
        maxw = w
print(maxw)
f.close()
'''

'''
最多单词
d = {}
for w in ls:
    d[w] = d.get(w, 0) + 1
maxc = 0
maxw = ''
for k in d:
    if d[k] > maxc and len(k) > 2:
        maxc = d[k]
        maxw = k
    if d[k] == maxc and len(k) >2 and k > maxw:
        maxw = k
print(maxw)
f.close()
'''

A = set(ls)
N = eval(input())
num = 0
for w in A:
    if len(w) == N:
        num += 1
print(num)
    
    
    
    
    
    
    