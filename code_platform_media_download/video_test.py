# -*- encoding: utf-8 -*-
'''
@File    :   video_test.py
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/29 15:26   Jonas           None
'''
import requests

url = 'http://v3-tt.ixigua.com/6fb8d50b5ca90296eb3005b5d6b2c3c4/5cc6b4da/video/m' \
      '/220b7d587c0ca834c12b5b1a97720fc4d391161dfb2400005ad7b4458547/?rc' \
      '=ajhyNTxnOGVvbTMzZDczM0ApQHRAbzo1Njc1MzQzMzM1NDUzNDVvQGgzdSlAZjN1KWRzcmd5a3VyZ3lybHh3Zjc2QDVoa18uNjNqL18tLS4tMHNzLW8jbyMxMy8uMS4tLjQtMjYxNi06I28jOmEtcSM6YHZpXGJmK2BeYmYrXnFsOiMzLl4%3D&vfrom=xgplayer '

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 "
                      "Safari/537.36 "
}

r = requests.get(url=url,headers=headers)

with open('1.mp4','wb') as fp:
    fp.write(r.content)