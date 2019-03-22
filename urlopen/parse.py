# encoding=utf-8
import urllib

'''
url只能由字母、数字、下划线组成，其他元素需要编码
'''

url = 'https://www.baidu.com/s?ie=utf-8&wd=汽车'
# 编码
ret = urllib.parse.quote(url)
# 解码
re = urllib.parse.unquote(ret)

print(ret)
print(re)
