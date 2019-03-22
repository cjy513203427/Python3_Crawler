# coding=utf-8
import urllib.request

url = 'https://www.bilibili.com/'
'''
urlib.request
    urlopen:发送请求
    urlretrive:发送请求并下载
'''

'''
response
    read:读取内容，内容是字节类型
    geturl:获取url
    getheaders:获取头部信息
    getcode:获取状态码
    readlines:返回字节类型的列表
'''

response = urllib.request.urlopen(url)
'''
decode方法将字节转换成字符串
decode参数指定编码，不指定默认utf-8
print(response.read().decode())
'''

#写法一
# with open('bili.html', 'wb') as fp:
#     fp.write(response.read())

#写法二
with open('bili.html', 'w', encoding='utf-8') as fp:
    fp.write(response.read().decode())