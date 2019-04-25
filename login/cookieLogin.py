# encoding=utf-8
import urllib.request
import urllib.parse
import http.cookiejar

'''
    先登录，保存下Cookie，再访问登录后的页面
'''

# 创建一个cookiejar
cj = http.cookiejar.CookieJar()
# 通过CookieJar创建一个Handler
handler = urllib.request.HTTPCookieProcessor(cj)
# 根据handler创建一个opener
opener = urllib.request.build_opener(handler)

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201924921672'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 "
                  "Safari/537.36 "
}

form_data = {
    'email': '18895358020',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '49d9290b2d36b326dec2fa73acd5c581df0e665699cb49b1c63280e9db118938',
    'rkey': '3a31816bcbf6fdd110f5c5d786fc440d',
    'f': 'http%3A%2F%2Fwww.renren.com%2F970143672%2Fprofile'
}

request = urllib.request.Request(url=post_url, headers=headers)
form_data = urllib.parse.urlencode(form_data).encode()
response = opener.open(request, data=form_data)

print(response.read().decode())

get_url = 'http://www.renren.com/970143672/profile'
request = urllib.request.Request(url=get_url, headers=headers)
response = opener.open(request)

print(response.read().decode())
