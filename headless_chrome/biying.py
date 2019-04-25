# -*- encoding: utf-8 -*-
'''
@File    :   biying.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/24 10:00   Jonas           None
'''

import requests

url = 'https://cn.bing.com/ttranslationlookup?&IG=64EEAEF7A4174FC59F30ACB149B63493&IID=translator.5038.10'

formdata = {
    'from': 'en',
    'to': 'zh-CHS',
    'text': 'Lion'
}

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 "
                      "Safari/537.36 "
}

r = requests.post(url=url,headers=headers,data=formdata)

print(r.json())