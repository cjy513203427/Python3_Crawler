# encoding=utf-8
import os
import urllib.parse
import urllib.request
import time
import re


def handle_request(url, page):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 "
                      "Safari/537.36 "
    }
    url = url + str(page) + '/'
    request = urllib.request.Request(url=url, headers=headers)
    print(url)
    return request


def download_image(content):
    '''
    带匹配区域
    <div class="thumb">
        <a href="/article/121633637" target="_blank">
        <img src="//pic.qiushibaike.com/system/pictures/12163/121633637/medium/8Z84DTSAGDW1F12I.jpg" alt="我就是右图第二个人">
        </a>
    </div>
    '''
    # 括号里保留要匹配的内容
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" .*?>.*?</div>', re.S)
    lt = pattern.findall(content)
    # print(lt)
    for image_src in lt:
        # 先处理image_src
        image_src = 'https:' + image_src
        # 创建文件夹
        dirname = 'qiutu'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        filename = image_src.split('/')[-1]
        filepath = dirname+'/'+filename
        # 发送请求，下载图片
        print('图片' + str(filename) + '下载开始...')
        urllib.request.urlretrieve(image_src,filepath)
        print('图片' + str(filename) + '下载结束...')


def main():
    url = 'https://www.qiushibaike.com/pic/page/'
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page, end_page + 1):
        print('第'+str(page)+'页开始下载...')
        # 生成请求对象
        request = handle_request(url, page)
        # 发送请求对象获取响应内容
        content = urllib.request.urlopen(request).read().decode()
        # 解析内容，提取图片连接，下载图片
        download_image(content)
        print('第' + str(page) + '页下载结束...')
        time.sleep(2)

if __name__ == '__main__':
    main()
