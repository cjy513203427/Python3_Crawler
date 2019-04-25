# -*- encoding: utf-8 -*-
'''
@File    :   proxy.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/24 10:14   Jonas           None
'''
 
import requests

url = 'https://www.baidu.com/baidu?wd=ip&ie=utf-8'

proxies = {
    'http':'183.63.53.171:3128'
}

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 "
                      "Safari/537.36 "
}

r = requests.get(url,headers=headers,proxies=proxies)
print(r.text)
# with open('daili.html','wb') as fp:
#     fp.write(r.content)