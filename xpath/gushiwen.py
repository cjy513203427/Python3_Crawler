# -*- encoding: utf-8 -*-
'''
@File    :   haoduanzi.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/1 9:53   Jonas           None
'''
 
import urllib.request
import urllib.parse
from lxml import etree
import time
import json

item_list=[]

def handle_request(url, page):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 "
                      "Safari/537.36 "
    }
    data = {
        'page': page
    }
    query_string = urllib.parse.urlencode(data)
    url += query_string
    # print(url)
    request = urllib.request.Request(url=url,headers=headers)
    return request


def parse_content(content):
    # 生成对象
    tree = etree.HTML(content)
    # 抓取内容
    div_list = tree.xpath("//div[@class='left']/div[@class='sons']/div[@class='cont']")
    for odiv in div_list:
        # 获取标题
        title = odiv.xpath("./p[1]/a/b/text()")
        title_text = ''.join(title)
        # 获取内容
        content = odiv.xpath("./div[@class='contson']/text()")
        content_text = '\n'.join(content)

        print(title_text)
        print(content_text)
        item = {
            '标题':title_text,
            '内容':content_text
        }
        # 将内容添加到列表中
        item_list.append(item)
def main():
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    url = 'https://www.gushiwen.org/default.aspx?'
    for page in range(start_page,end_page+1):
        request = handle_request(url,page)
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)
        time.sleep(1)

    string = json.dumps(item_list,ensure_ascii=False)
    with open('gushiwen.json','w',encoding='utf8') as fp:
        fp.write(string)

if __name__ == '__main__':
    main()