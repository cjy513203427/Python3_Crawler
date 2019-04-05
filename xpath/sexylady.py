# -*- encoding: utf-8 -*-
'''
@File    :   sexylady.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/5 11:11   Jonas           None
'''

import urllib.request
import urllib.parse
from lxml import etree
import time
import os


def handle_request(url, page):
    # 第一页规律不一样，分开判断
    if page == 1:
        url = url.format('')
    else:
        url = url.format('_' + str(page))

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 "
                      "Safari/537.36 "
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


# 解析内容
def parse_content(content):
    tree = etree.HTML(content)
    '''
        src本应该获取到，事实上为0，这里用到了懒加载技术
        懒加载：用到再加载
        实现方式：<img src2="图片路径">
    '''

    image_list = tree.xpath("//div[@id='container']/div/div/a/img/@src2")
    # print(image_list)
    # print(len(image_list))
    for img_src in image_list:
        download_image(img_src)

def download_image(image_src):
    dirpath = 'sexy'
    # 创建文件夹
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    # 文件名
    filename = os.path.basename(image_src)
    # 图片路径
    filepath = os.path.join(dirpath,filename)

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 "
                      "Safari/537.36 "
    }
    request = urllib.request.Request(url=image_src, headers=headers)
    response = urllib.request.urlopen(request)
    with open(filepath,'wb')as fp:
        fp.write(response.read())

def main():
    url = 'http://sc.chinaz.com/tupian/xingganmeinvtupian{}.html'
    # http://sc.chinaz.com/tupian/xingganmeinvtupian_2.html
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page, end_page + 1):
        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)


if __name__ == '__main__':
    main()
