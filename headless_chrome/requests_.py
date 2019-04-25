# -*- encoding: utf-8 -*-
'''
@File    :   requests_.py
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/24 9:01   Jonas           None
'''
 
import requests

url = 'https://www.baidu.com'

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 "
                      "Safari/537.36 "
}

r = requests.post(url=url,headers=headers)
# print(r.encoding)
# r.encoding='utf8'
# print(r.text)
print(r.content)

# 带参数的get
# url = 'https://www.baidu.com/s'
# data = {
#     'wd':'中国'
# }
# parameters参数
# r = requests.get(url=url,headers=headers,params=data)
# 把结果写到文件中,写入失败,百度做了某种处理，导致无法爬取
with open('baidu.html','wb') as fp:
    fp.write(r.content)