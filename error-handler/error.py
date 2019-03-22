# encoding=utf-8
import urllib

"""
URLError
(1)没有网络
(2)服务器连接失败
(3)找不到指定的服务器

HTTPError
是URLError的子类


"""

# URLError_url = 'http://www.maodan.com'
HTTPError_url = 'https://www.cnblogs.com/Java-Starter/p/10524408.html'

try:
    response = urllib.request.urlopen(HTTPError_url)
    print(response)
except urllib.error.HTTPError as e:
    print(e)
except urllib.error.URLError as e:
    print(e)