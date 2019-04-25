# -*- encoding: utf-8 -*-
'''
@File    :   bus_line.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/25 14:29   Jonas           None
'''

import requests
from lxml import etree

items = []
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/72.0.3626.121 "
                  "Safari/537.36 "
}


def parse_navigation():
    url = 'https://hefei.8684.cn/'
    r = requests.get(url, headers=headers)
    # 解析内容，获取所有导航链接
    tree = etree.HTML(r.text)
    # 查找以数字开头的所有链接
    number_href_list = tree.xpath('//div[@class="bus_kt_r1"]/a/@href')
    # 查找以字母开头的所有链接
    char_href_list = tree.xpath('//div[@class="bus_kt_r2"]/a/@href')
    # 将所有需要的链接返回
    return number_href_list + char_href_list


def parse_thirdclass_route(content):
    tree = etree.HTML(content)
    # 获取公交线路信息
    bus_number = tree.xpath('//div[@class="bus_i_t1"]/h1/text()')[0]
    # 获取运行时间
    run_time = tree.xpath('//p[@class="bus_i_t4"][1]/text()')[0]
    # 获取票价信息
    ticket_info = tree.xpath('//p[@class="bus_i_t4"][2]/text()')[0]
    # 获取更新时间
    update_time = tree.xpath('//p[@class="bus_i_t4"][4]/text()')[0]
    # 获取上行总站数
    up_total = tree.xpath('//span[@class="bus_line_no"]/text()')[0]
    # 获取上行所有站名
    up_site_list = tree.xpath('//div[@class="bus_line_site "][1]/div/div/a/text()')
    try:
        # 获取下行总站数
        down_total = tree.xpath('//span[@class="bus_line_no"]/text()')[1]
        # 获取上行所有站名
        down_site_list = tree.xpath('//div[@class="bus_line_site "][2]/div/div/a/text()')
    except Exception as e:
        down_total = ''
        down_site_list = []
    # 将每一条公交线路信息放入到字典中
    item = {
        '线路名称': bus_number,
        '运行时间': run_time,
        '票价信息': ticket_info,
        '更新时间': update_time,
        '上行站数': up_total,
        '上行站点': up_site_list,
        '下行站数': down_total,
        '下行站点': down_site_list,
    }
    items.append(item)


def parse_secondclass_route(content):
    tree = etree.HTML(content)
    # 写Xpath，获取每一个线路
    route_list = tree.xpath('//div[@id="con_site_1"]/a/@href')
    route_name = tree.xpath('//div[@id="con_site_1"]/a/text()')
    i = 0
    # 遍历上面列表
    for route in route_list:
        print('开始爬取%s线路'% route_name[i])
        route = 'https://hefei.8684.cn' + route
        r = requests.get(url=route, headers=headers)
        # 解析内容，获取每一路公交的详细url
        parse_thirdclass_route(r.text)
        i+=1


def parse_secondclass(navi_list):
    # 遍历列表，依次发送请求、解析内容，获取每一个页面所有的公交路线
    for first_url in navi_list:
        first_url = 'https://hefei.8684.cn' + first_url
        print('开始爬取%s所有的公交信息' % first_url)
        r = requests.get(url=first_url, headers=headers)
        # 解析内容，获取每一路公交的详细url
        parse_secondclass_route(r.text)
        print('结束爬取%s所有的公交信息' % first_url)


def main():
    # 爬取第一页导航链接
    navi_list = parse_navigation()
    # 爬取二级页面
    parse_secondclass(navi_list)
    # 爬取完毕
    fp = open('合肥公交.txt', 'w', encoding='utf8')
    for item in items:
        fp.write(str(item) + '\n')
    fp.close()


if __name__ == '__main__':
    main()
