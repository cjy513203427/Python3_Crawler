# encoding=utf-8
import urllib

url = 'http://www.renren.com/970143672/profile'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 "
                  "Safari/537.36 ",
    'Cookie':'anonymid=jth1629a42nzvd; depovince=GW; _r01_=1; _de=C4C8254100410D4B727E6F614F21270D; '
             'ln_uact=18895358020; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; '
             'ick_login=a792776c-c8c3-4293-9f3b-ef54d4242ed7; jebecookies=68b75978-fb57-491a-903d-2a29064e62d9|||||; '
             'JSESSIONID=abcH2DnbK_1FGhJIDXDMw; p=365d11ea3c825682b7b4fd16ade873ca2; first_login_flag=1; '
             't=bc8e6cd7b266c9f5ec33d839572feee02; societyguester=bc8e6cd7b266c9f5ec33d839572feee02; id=970143672; '
             'xnsid=623a0ea9; loginfrom=syshome '
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)


with open('renren.html','wb') as fp:
    fp.write(response.read())

