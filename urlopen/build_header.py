# encoding=utf-8
import urllib

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 '
                  'Safari/537.36 '
}

#构建请求对象
request = urllib.request.Request(url=url,headers=headers)
#发送请求
response = urllib.request.urlopen(request)

print(response.read().decode())