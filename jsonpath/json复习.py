# -*- encoding: utf-8 -*-
'''
@File    :   json.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/7 9:34   Jonas           None
'''

import json

lt = [
    {'name': '王宝强', 'age': 30},
    {'name': '马蓉', 'age': 35},
    {'name': '贾乃亮', 'age': 32},
    {'name': '李小璐', 'age': 25},
    {'name': '宋喆', 'age': 31},
]

string = json.dumps(lt)

print(string)

obj = json.loads(string)
print(obj)

json.dump(lt,open('json.txt','w',encoding='utf8'))
obj = json.load(open('json.txt','r',encoding='utf8'))
