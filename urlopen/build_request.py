# encoding=utf-8
import urllib

'''
7878
'''
# https://www.baidu.com/baidu?wd=java%E5%A4%9A%E7%BA%BF%E7%A8%8B&tn=monline_4_dg&ie=utf-8
url = 'https://www.baidu.com/'

name = 'boy'
age = 18
sex = '女'
height = '180'

data = {
    'name': name,
    'age': age,
    'sex': sex,
    'height': height,
    'weight': 180
}

'''
原生写法
lt = []
for k,v in data.items():
    lt.append(k + '=' + str(v))
# join连接字符串
query_string = '&'.join(lt)
'''

# 直接封装参数，支持特殊字符直接转义
query_string = urllib.parse.urlencode(data)

url = url + '?' + query_string
print(url)
