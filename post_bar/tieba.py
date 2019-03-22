# encoding=utf-8
import os
import urllib

url = 'http://tieba.baidu.com/f?'

'''
输入吧名，输入起始页码，输入结束页码，然后在当前文件夹中创建一个当前吧名为名字的文件夹
文件名是吧名_page.html
'''
bar_name = input('请输入吧名')
start_page = int(input('请输入起始页码'))
end_page = int(input('请输入结束页码'))

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 "
                  "Safari/537.36 "
}
if not os.path.exists(bar_name):
    os.mkdir(bar_name);
# 通过循环爬取每一页的数据
for page in range(start_page, end_page + 1):
    # page是当前页
    data = {
        'ie': 'utf-8',
        'kw': bar_name,
        'pn': (start_page - 1) * 50
    }
    data = urllib.parse.urlencode(data)
    url_t = url + data
    # print(url_t)
    request = urllib.request.Request(url=url_t, headers=headers)
    print('第'+str(page)+'页开始下载......')
    response = urllib.request.urlopen(request)

    # 生成文件名
    filename = bar_name + '_' + str(page) + '.html'
    # 拼接文件路径
    filepath = bar_name + '/' + filename

    #写内容
    with open(filepath,'wb') as fp:
        fp.write(response.read())
    print('第'+str(page)+'页下载结束......', page)