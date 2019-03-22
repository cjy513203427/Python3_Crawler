# encoding=utf-8
import urllib

# 创建Handler
# 183.63.53.171:3128
handler = urllib.request.ProxyHandler({'http': '183.63.53.171:3128'})
# 通过Handler创建一个opener
opener = urllib.request.build_opener(handler)

url = 'https://www.baidu.com/baidu?wd=ip'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 "
                  "Safari/537.36 "
}

# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)
# 发送请求
response = opener.open(request)

#print(response.read().decode())

# 为什么下载文件为空？？？？？？？用opener的模式会出现写入文件异常
with open('ip.html', 'wb') as fp:
    fp.write(response.read())
