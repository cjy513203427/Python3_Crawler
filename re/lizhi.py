# encoding=utf-8
import re
import urllib.request
import urllib.parse


def handle_request(url, page=None):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 "
                      "Safari/537.36 "
    }
    if page is not None:
        url = url + str(page) + '.html'
    request = urllib.request.Request(url=url, headers=headers)
    # print(url)
    return request


def get_text(a_href):
    # 调用函数构建请求对象
    request = handle_request(a_href)
    # 发送请求，获得响应
    content = urllib.request.urlopen(request).read().decode()
    # 解析内容
    pattern = re.compile('<div class="neirong">(.*?)</div>',re.S)
    lt = pattern.findall(content)
    # lt是一个含有一个元素的列表，获取第一个元素即可
    text = lt[0]
   
    # 删除无用标签
    pat_li = re.compile(r'<.*?>')
    text = pat_li.sub(' ', text)
    return text


def parse_content(content):
    '''
    <h3><a href="/lizhi/qianming/20190141198.html"><b>不怕失败才是成功的开始——不妥协的励志经典语录</b></a></h3>
    :param content:
    :return:
    '''
    pattern = re.compile(r'<h3><a href="(/lizhi/qianming/\d+\.html)">(.*?)</a></h3>', re.S)
    lt = pattern.findall(content)
    # 返回的lt是一个列表，列表中的元素都是元组，元组中第一个元素就是正则中第一个小括号匹配到的内容，
    # 元组中第二个元素就是正则中第二个小括号匹配到的内容
    for href_title in lt:
        # 获取内容的链接
        a_href = 'http://www.yikexun.cn' + href_title[0]
        # 获取标题
        title = href_title[-1]
        # 向a_href发送请求，获取响应内容
        text = get_text(a_href)
        # 写入到html文件中
        string = '<h1>'+title+'</h1>'+'<p>'+text+'</p>'
        # 'a'是追加模式
        with open('lizhi.html','a',encoding='utf8') as fp:
            fp.write(string)


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
