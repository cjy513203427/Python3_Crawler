import json
import urllib.parse
import urllib.request


# https://sou.zhaopin.com
class ZhilianSpider(object):
    # url中不变的内容，要和参数拼接组成完整的url
    url = 'https://fe-api.zhaopin.com/c/i/sou?'

    def __init__(self, city_id, kw ):
        # 将上面的参数保存为自己的成员属性
        self.city_id = city_id
        self.kw = kw
        # 起始偏移量
        self.start = 0
        self.pageSize = 100
        # 未知的必需参数
        self.kt = 3

    # 爬取程序
    def run(self):
        # 循环爬取每一页数据
        for page in range(self.start, 80, 80):
            request = self.handle_request(page)
            content = urllib.request.urlopen(request).read()
            # 解析内容
            self.parse_content(content)

    def parse_content(self, content):
        # 生成对象
        h_json = json.loads(content)
        # 需要的列
        self.print_keyvalue_by_key(h_json,'jobName')

    # 根据key递归打印json
    def print_keyvalue_by_key(self,input_json,key):
            key_value=''
            if isinstance(input_json,dict):
                for json_result in input_json.values():
                    if key in input_json.keys():
                        key_value = input_json.get(key)
                    else:
                        self.print_keyvalue_by_key(json_result,key)
            elif isinstance(input_json,list):
                for json_array in input_json:
                    self.print_keyvalue_by_key(json_array,key)
            if key_value!='':
                print (str(key)+" = "+str(key_value))

    # 根据page拼接指定的url，然后生成请求对象
    def handle_request(self, page):
        data = {
            'cityId': self.city_id,
            'kw': self.kw,
            'start': self.start,
            'pageSize': '100',
            'kt': '3',
        }
        url_now = self.url + urllib.parse.urlencode(data)
        # 构建请求对象
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/72.0.3626.121 "
                          "Safari/537.36 "
        }

        request = urllib.request.Request(url=url_now, headers=headers)

        return request


def main():
    city_id = input('输入工作地点')
    kw = input('输入工作关键字')
    # 创建对象，启动爬取程序
    spider = ZhilianSpider(city_id, kw)
    spider.run()


if __name__ == '__main__':
    main()
