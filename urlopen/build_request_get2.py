#encoding=utf-8
import urllib

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action='

'''
start=0 limit=20
start=20 limit=20
'''

page = int(input('请输入第几页'))

page_size = 20

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 "
                  "Safari/537.36 "
}
#构建get参数
data = {
    'start': (page-1)*page_size,
    'limit': page_size,
}

query_string = urllib.parse.urlencode(data)

url+=query_string

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)

print(response.read().decode())
