# -*- coding: utf-8 -*-
import random

class ATM():
    '''
    ATM机类， 假设只有一个ATM机，最长服务时间为5，服务时间均匀分布（随机）
    '''
    
    def __init__(self, maxtime = 5):
        self.t_max = maxtime
        
    def getServCompleteTime(self, start = 0):
        return start + random.randint(1, self.t_max)
    

class Customers():
    '''
    Customers类，n个顾客，最长到达间隔为10，均匀分布
    '''
    
    def __init__(self, n):
        self.count = n
        self.left = n
        
    def getNextArrvTime(self, start = 0, arrvtime = 10):
        if self.left != 0:
            self.left -= 1
            return start + random.randint(1, arrvtime)
        else:
            return 0
        
    def isOver(self):
        return True if self.left == 0 else False
    

c = Customers(100)
a = ATM()
wait_list = []        # 等待队列，由到达时间(next_arrv)组成的列表
wait_time = 0         # 等待时间，队列总等待时间
cur_time = 0          # 当前时间/全局之间
cur_time += c.getNextArrvTime()   # 全局时间以第一个客户到达为开始
wait_list.append(cur_time)        # 第一个客户到达的时间进入等待队列

'''
整体思路

需要一个全局时间，以ATM机每次处理结束为驱动，等待队列维护客户到达时间，
当时间变化时，驱动等待队列变化
'''

while len(wait_list) != 0 or not c.isOver():
    # 总体while循环，所有顾客均完成服务后结束
    
    if wait_list[0] <= cur_time:
        next_time = a.getServCompleteTime(cur_time)
        del wait_list[0]
    else:
        next_time = cur_time + 1
    # next_time 受ATM机操作驱动，ATM处理完当前业务时，时间前进/ATM空置，时间+1
    
    if not c.isOver() and len(wait_list) == 0:
        next_arrv = c.getNextArrvTime(cur_time)
        wait_list.append(next_arrv)
    # 当前无人等待，且还有未到达顾客：更新wait_list(期间next_time不断+1, 直至客户到达)
        
    if not c.isOver() and wait_list[-1] < next_time:
        next_arrv = c.getNextArrvTime(wait_list[-1])
        wait_list.append(next_arrv)
        while next_arrv < next_time and not c.isOver():
            next_arrv = c.getNextArrvTime(next_arrv)
            wait_list.append(next_arrv)
    # 截至next_time, 在时间更迭过程中，还可能到达客户，需要持续产生客户
    #直至其到达时间超过next_time
    
    # 在每个事件更迭周期，累积wait_time
    for i in wait_list:
        if i <= cur_time:
            wait_time += next_time - cur_time
        elif cur_time < i < next_time:
            wait_time += next_time - i
        else:
            pass
        # pass 为无需等待的情况
        
    cur_time = next_time    # 驱动事件
    
print(wait_time / c.count)
# 计算平均等待时间
    
    
    
    
    
    
    
    
    
    
    
    
    