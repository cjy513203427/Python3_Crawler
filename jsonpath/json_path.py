# -*- encoding: utf-8 -*-
'''
@File    :   jsonpath.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/17 14:14   Jonas           None
'''

import jsonpath
import json

# 将json格式的字符串转化为python对象
obj = json.load(open('book.json', 'r', encoding='utf-8'))

# print(obj)

# 查询所有书的作者
# ret = jsonpath.jsonpath(obj,'$.store.book[*].author')

# 查找所有作者
# ret = jsonpath.jsonpath(obj,'$..author')

# 遍历store所有元素
# ret = jsonpath.jsonpath(obj,'$.store.*')

# store下面的所有price
# ret = jsonpath.jsonpath(obj, '$.store..price')

# 查找第三个book
# ret = jsonpath.jsonpath(obj,'$..book[2]')

# 查找最后一本书
# ret = jsonpath.jsonpath(obj,'$..book[(@.length-1)]')

# 前两本书
# ret = jsonpath.jsonpath(obj,'$..book[0,1]')

# 查找含有isbn这个key的数据
# ret = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')

# 查找所有price键对应的值小于10的所有book
ret = jsonpath.jsonpath(obj,'$..book[?(@.price<10)]')
print(ret)
