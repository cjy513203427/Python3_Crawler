# -*- encoding: utf-8 -*-
'''
@File    :   gushiwen.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/25 16:51   Jonas           None
'''
 
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/72.0.3626.121 "
                  "Safari/537.36 "
}



def download_code(s):
    url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    r = s.get(url=url,headers=headers)
    r.encoding = 'uft8'
    soup = BeautifulSoup(r.text,'lxml')
    # 得到图片路径，下载到本地
    image_src = 'https://so.gushiwen.org' + soup.find('img',id='imgCode')['src']
    r_image = s.get(image_src,headers=headers)
    with open('code.png','wb') as fp:
        fp.write(r_image.content)
    # 查找表单所需要的两个参数
    __VIEWSTATE = soup.find('input',id = '__VIEWSTATE')['value']
    __VIEWSTATEGENERATOR = soup.find('input',id = '__VIEWSTATEGENERATOR')['value']
    return __VIEWSTATE,__VIEWSTATEGENERATOR

def login(__VIEWSTATE,__VIEWSTATEGENERATOR,s):
    post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx%3ftype%3ds'
    # 提示用户输入验证码
    code = input('请输入验证码：')
    form_data = {
        '__VIEWSTATE': __VIEWSTATE,

        '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,

        'from': 'http://so.gushiwen.org/user/collect.aspx?type=s',

        'email': '634208959@qq.com',

        'pwd': '123456',

        'code': code,

        'denglu': '登录'
    }
    r = s.post(url=post_url,headers=headers,data=form_data)

    with open('gushi.html','w',encoding='utf8') as fp:
        fp.write(r.text)


def main():
    # 创建会话,为了保持验证码的请求是基于会话的，因为每次发送验证码请求返回结果都不一致
    s = requests.Session()
    # 下载验证码
    __VIEWSTATE,__VIEWSTATEGENERATOR = download_code(s)

    login(__VIEWSTATE,__VIEWSTATEGENERATOR,s)


if __name__ == '__main__':
    main()
