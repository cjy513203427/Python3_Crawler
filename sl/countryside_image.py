# -*- encoding: utf-8 -*-
'''
@File    :   countryside_image.py
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/22 14:36   Jonas           None
'''
 
import time

from selenium import webdriver

path = r'E:\开发工具\phantomjs-2.1.1-windows\bin\phantomjs.exe'

browser = webdriver.PhantomJS(path)

url = 'http://sc.chinaz.com/tupian/xiangcuntianyuan.html'

browser.get(url)
time.sleep(3)
# 保存两次html，检查是否存在懒加载
with open(r'phantomjs/图片1.html','w',encoding='utf8')as fp:
    fp.write(browser.page_source)

js = 'document.body.scrollTop=10000'
browser.execute_script(js)
time.sleep(3)

with open(r'phantomjs/图片2.html','w',encoding='utf8')as fp:
    fp.write(browser.page_source)

browser.quit()