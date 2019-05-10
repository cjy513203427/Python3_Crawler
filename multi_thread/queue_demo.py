# -*- encoding: utf-8 -*-
'''
@File    :   queue_demo.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/5/5 9:31   Jonas           None
'''
 
from queue import Queue

# 创建队列
q = Queue(5)
print(q.empty())
# 存数据
q.put('科比')
q.put('勒布朗')
q.put('JR')
print(q.qsize())
q.put('汤普森')
q.put('乔治希尔')
print(q.full())

# 取数据
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())