# encoding=utf-8
import re
import urllib.request
import urllib.parse


def handle_request(url, page):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 "
                      "Safari/537.36 "
    }
    url = url + str(page) + '.html'
    request = urllib.request.Request(url=url, headers=headers)
    print(url)
    return request


def parse_content(content):
    '''
    <h3><a href="/lizhi/qianming/20190141198.html"><b>不怕失败才是成功的开始——不妥协的励志经典语录</b></a></h3>
    :param content:
    :return:
    '''
    pattern = re.compile(r'<h3><a href="/lizhi/qianming/\d+\.html"><b>(.*?)</b></a></h3>', re.S)
    lt = pattern.findall(content)
    print(lt)


def main():
    url = 'http://www.yikexun.cn/lizhi/qianming/list_50_'
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page, end_page + 1):
        # 生成请求对象
        request = handle_request(url, page)
        # 发送请求对象获取响应内容
        content = urllib.request.urlopen(request).read().decode()
        # 解析内容
        parse_content(content)


if __name__ == '__main__':
    main()
