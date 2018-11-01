# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:36:30 2018

@author: 10696
"""

# 第二题
class Echo:
    def __init__(self, name):
        self.name = name
        print("Hello {}!".format(name))

    def __add__(self, others):
        if str(self.name).lower() == str(others.name).lower():
            print("Hello, the SAME name!")
        else:
            print("Hello, NOT the same!")

s = input()
name1 = Echo(s.split()[0])
name2 = Echo(s.split()[1])
name1 + name2

# 第三题
class Echo():
    def __init__(self, name):
        self.name = name
        print("Hello {}".format(name))

    def __pow__(self, k):
        if k == 0:
            out = ""
        else:
            out = self.name
            out += (", " + self.name) * (k - 1)
        print("Hello {}!".format(out))

s = input()
name = s.split()[0]
k = eval(s.split()[1])
echoA = Echo(name)
echoA ** k

##第一题
class Echo:
    def __init__(self, name):
        self.name = name
        print("Hello {}!".format(name))
    def __len__(self):
        a = 0
        for i in self.name:
            if ord(i) in range(65, 91):
                a += 1
            else:
                pass
        return a
        print("Hello {}!".format(a))

s = input()
echoA = Echo(s)
len(echoA)

# 第一题2
class Echo:
    def __init__(self, name):
        self.name = name
        print("Hello {}!".format(name))
    def __len__(self):
        a = 0
        for c in self.name:
            if c.isupper():
                a += 1
        return a
        print("Hello %d!" %a)
        # 一定要有返回值  新增return a
        #print("Hello {}!".format(a))

s = input()
echoA = Echo(s)
len(echoA)