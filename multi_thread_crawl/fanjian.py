# coding=utf-8
import threading
import time
from queue import Queue
import requests
from lxml import etree
import json

# 用来存放采集线程
g_crawl_list = []
# 用来存放解析线程
g_parse_list = []


# 采集线程类
class CrawlThread(threading.Thread):
    def __init__(self, name, page_queue, data_queue):
        super(CrawlThread, self).__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'http://www.fanjian.net/jiantu-{}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/70.0.3538.67 Safari/537.36',
        }

    def run(self):
        print('%s---线程启动' % self.name)
        while 1:
            # 判断何时退出
            if self.page_queue.empty():
                break
            # 从队列中取出页码
            page = self.page_queue.get()
            # 拼接url，发送请求
            url = self.url.format(page)
            r = requests.get(url=url, headers=self.headers)
            # 将相应内容存放到data_queue中
            self.data_queue.put(r.text)
        print('%s---线程退出' % self.name)


# 解析线程类
class ParserThread(threading.Thread):
    def __init__(self, name, data_queue, lock, fp):
        super(ParserThread, self).__init__()
        self.name = name
        self.data_queue = data_queue
        self.lock = lock
        self.fp = fp

    def run(self):
        print('%s---线程启动' % self.name)
        while 1:
            # 判断何时退出
            # 从data_queue中取出一页数据
            try:
                data = self.data_queue.get(True, 10)
                # print(111111)
            except Exception as e:
                break
            # 解析内容即可
            self.parse_content(data)
        print('%s---线程退出' % self.name)

    # 解析内容
    def parse_content(self, data):
        tree = etree.HTML(data)

        li_list = tree.xpath('//ul[@class="cont-list"]/li')

        # print(li_list)
        items = []
        for oli in li_list:
            # 获取图片标题
            title = oli.xpath('./h2/a/text()')[0]
            # 获取图片url
            image_url = oli.xpath('./div/p/img/@data-src')
            item = {
                '标题': title,
                '连接': image_url
            }
            items.append(item)
        # 写到文件中,线程锁锁住，线程完成写操作之后解锁，不然程序将卡住
        self.lock.acquire()
        self.fp.write(json.dumps(items, ensure_ascii=False) + "\n")
        self.lock.release()


# 创建队列
def create_Queue():
    # 创建一个页码队列
    page_queue = Queue()
    for page in range(1, 1874):
        page_queue.put(page)
    # 创建每一页的内容队列
    data_queue = Queue()
    return page_queue, data_queue


# 创建采集线程
def create_crawl_thread(page_queue, data_queue):
    crwal_name = ['采集线程1号', '采集线程2号', '采集线程3号', '采集线程4号', '采集线程5号', '采集线程6号']
    # 创建一个采集线程
    for name in crwal_name:
        tcrawl = CrawlThread(name=name, page_queue=page_queue, data_queue=data_queue)
        g_crawl_list.append(tcrawl)


# 创建解析线程
def create_parse_thread(data_queue, fp, lock):
    parse_name = ['解析线程1号', '解析线程2号', '解析线程3号']
    for name in parse_name:
        # 创建一个解析线程
        t_parse = ParserThread(name=name, data_queue=data_queue, fp=fp, lock=lock)
        g_parse_list.append(t_parse)


def main():
    # 创建队列函数
    page_queue, data_queue = create_Queue()
    # 打开文件
    fp = open('jian.json', 'a', encoding='utf8')
    # 创建锁
    lock = threading.Lock()
    # 创建采集线程
    create_crawl_thread(page_queue=page_queue, data_queue=data_queue)
    time.sleep(10)
    # 创建解析线程
    create_parse_thread(data_queue=data_queue, fp=fp, lock=lock)
    # 启动所有采集线程
    for tcrawl in g_crawl_list:
        tcrawl.start()
    # 启动所有解析线程
    for tparse in g_parse_list:
        tparse.start()
    # 主线程等待子线程结束
    for tcrawl in g_crawl_list:
        tcrawl.join()
    for tparse in g_parse_list:
        tparse.join()
    # 关闭json文件
    fp.close()
    print("主线程，子线程全部结束！")


if __name__ == '__main__':
    main()
