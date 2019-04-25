# -*- encoding: utf-8 -*-
'''
@File    :   chinaunix.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/24 11:23   Jonas           None
'''
 
import requests

s = requests.Session()

get_url = 'http://account.chinaunix.net/login/login'

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

r = s.post(url=get_url,headers=headers,data=formdata)
print(r.text)

# 访问登录后的页面
info_url = 'http://account.chinaunix.net/ucenter/user/index'

r = s.get(url=info_url,headers=headers)

print(r.text)