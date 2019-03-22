# encoding=utf-8
import urllib

"""

Handler处理器
    使用代理
    使用Cookie

代理
    正向代理(我们需要的)：
        为客户端进行代理
    反向代理：
        为服务器端进行代理

"""

url = 'https://www.baidu.com'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 "
                  "Safari/537.36 "
}

# 创建一个Handler
handler = urllib.request.HTTPHandler()
# 通过Handler创建一个opener
opener = urllib.request.build_opener(handler)
# 构建请求对象
request = urllib.request.Request(url,headers = headers)
# 发送请求
response = opener.open(request)

print(response.read().decode())
