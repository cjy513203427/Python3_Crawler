#encoding=utf-8
import urllib

word = input("输入想搜索的内容")
url = 'https://search.bilibili.com/all?'

#参数写成一个字典
data = {
    'from_source':'banner_search',
    'keyword':word,
}

query_string = urllib.parse.urlencode(data)
url += query_string

response = urllib.request.urlopen(url)

filename = word + '.html'
with open(filename,'wb') as fp:
    fp.write(response.read())