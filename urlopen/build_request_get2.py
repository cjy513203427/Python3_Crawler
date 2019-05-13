#encoding=utf-8
import urllib

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action='
url2 = 'http://10.153.195.92:8080/rdmp/clientAction.do?method=json&common=queryById&classes=userOptionServiceImpl&userid=lijun2'

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

req = urllib.request.Request(url=url2)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36')

response = urllib.request.urlopen(req)
print(response.read().decode())
