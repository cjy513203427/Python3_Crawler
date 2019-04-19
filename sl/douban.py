# -*- encoding: utf-8 -*-
'''
@File    :   douban.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/18 17:18   Jonas           None
'''

import time

from selenium import webdriver

path = r'E:\开发工具\phantomjs-2.1.1-windows\bin\phantomjs.exe'

browser = webdriver.PhantomJS(path)

url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action='

browser.get(url)
time.sleep(3)

browser.save_screenshot(r'phantomjs\douban1.png')

# 让browser执行简单的js代码，模拟滚动到底部
js = 'document.body.scrollTop=10000'
browser.execute_script(js)

time.sleep(3)
browser.save_screenshot(r'phantomjs\douban2.png')

# 获取网页的源码，保存到文件中
html = browser.page_source

with open(r'phantomjs\domain.html','w',encoding='utf-8') as fp:
    fp.write(html)

browser.quit()
