# -*- encoding: utf-8 -*-
'''
@File    :   renren.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/24 10:42   Jonas         先登录，保存会话，再利用Cookie访问人人网登录后的页面
'''
 
import requests

# 创建会话,保存会话信息
# 以后操作都通过s访问
s = requests.Session()

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 "
                      "Safari/537.36 "
}

post_url = 'https://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201933104799'

formdata = {
    'email':'18895358020',

    'icode':'',

    'origURL':'http://www.renren.com/home',

    'domain':'renren.com',

    'key_id':'1',

    'captcha_type':'web_login',

    'password':'3b48dec6c35d02e4e3619a845a3150460e03344529ac6c26a532b70448fb9d0f',

    'rkey':'31f2cea97b6657f3ef072f0195443bcd',

    'f':'http%3A%2F%2Fwww.renren.com%2F970143672'
}

r = s.post(url=post_url,headers=headers,data=formdata)

print(r.text)

get_url = 'https://www.renren.com/970143672/profile'

r = s.get(url=get_url,headers=headers)

print(r.text)