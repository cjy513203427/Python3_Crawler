# -*- encoding: utf-8 -*-
'''
@File    :   video_download.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/29 15:33   Jonas           None

首先向https://www.365yg.com/发送请求
将里面所有的标题链接获取到
依次向每个标题链接发送请求
获取下载链接，即video标签的src属性
再向下载链接发送请求，保存到本地
'''

import requests
from bs4 import BeautifulSoup
import time
from lxml import etree
import json
from selenium import webdriver

'''
接口信息
https://www.365yg.com/api/pc/feed/?min_behot_time=0&category=video_new&utm_source=toutiao&widen=1&tadrequire=true&as=A1C57C6C369B2B2&cp=5CC67BE27B126E1&_signature=Qr6EcxAXHnrLX73pfTm6xUK-hG

'''

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/72.0.3626.121 "
                  "Safari/537.36 "
}


def handle_href(a_href):
    r = requests.get(a_href,headers=headers)
    # 解析内容
    # 获取src属性,xpath表达式正确却获取不到，因为视频地址是通过js加载的
    # 通过PhantomJS来进行解决
    path = r'E:\开发工具\phantomjs-2.1.1-windows\bin\phantomjs.exe'
    browser = webdriver.PhantomJS(path)

    browser.get(a_href)
    time.sleep(3)

    # 获取源码，生成tree对象，然后查找video中的src对象

    tree = etree.HTML(browser.page_source)
    video_src = tree.xpath('/html/body/div/div[2]/div[1]/div/div/video/@src')
    print(video_src)
    # 下载功能受阻，无法爬取<video>的内容
    # videoId被加密




def handle_title(widen):
    url = 'https://www.365yg.com/api/pc/feed/?min_behot_time=0&category=video_new&utm_source=toutiao&widen={}&tadrequire=true&as=A1C57C6C369B2B2&cp=5CC67BE27B126E1&_signature=Qr6EcxAXHnrLX73pfTm6xUK-hG'
    # 将url和widen拼接起来，组成完整的url
    url = url.format(widen)
    r = requests.get(url=url, headers=headers)
    # 这里获取的网页内容只有js，没有html
    # 解析内容
    # 将json格式字符串转化成python对象
    obj = json.loads(r.text)

    data = obj['data']
    # 循环data列表，依次取出每一个视频信息
    for video_data in data:
        title = video_data['title']
        a_href = 'https://www.365yg.com'+video_data['source_url']
        print(title)
        print(a_href)
        # 取出所有和视频相关的数据
        # 获取链接
        # 发送请求，获取页面内容。解析内容，获取src
        handle_href(a_href)

def main():
    # 解析首页，返回所有标题链接
    for widen in range(1,5):
        handle_title(widen)


if __name__ == '__main__':
    main()
