# encoding=utf-8
import urllib

post_url = 'https://fanyi.baidu.com/sug'

word = input('请输入要查询的单词')

# 构建表单数据
form_data = {
    'kw': word,

}

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 "
                  "Safari/537.36 "
}
# 发送请求的过程
request = urllib.request.Request(url=post_url, headers=headers)
# 通过encode方法将str转成byte
# POST data should be bytes,an iterable of bytes, or a file object. It cannot be of type str.
form_data = urllib.parse.urlencode(form_data).encode()
# post参数写在urlopen里
respose = urllib.request.urlopen(request, data=form_data)

print(respose.read().decode())
