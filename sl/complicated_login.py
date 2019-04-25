# -*- encoding: utf-8 -*-
'''
@File    :   complicated_login.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/22 15:05   Jonas           None
'''
 
import urllib.request
import urllib.parse

url = 'http://account.chinaunix.net/login/login'

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 "
                      "Safari/537.36 "
}

formdata = {
    'username':'cjy513203427',
    'password':'370523',
    '_token':'lHEkhng3WCjuwS1xlisBhmWF3sSDZKdtgV442WZu',
    '_t':'1555916658731'
}

formdata = urllib.parse.urlencode(formdata).encode()

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request,data = formdata)

print(response.read().decode())

# with open('unix.html','wb') as fp:
#     fp.write(response.read())