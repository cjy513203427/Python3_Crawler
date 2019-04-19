# -*- encoding: utf-8 -*-
'''
@File    :   phantomjs.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/18 17:02   Jonas           None
'''
import time

from selenium import webdriver

path = r'E:\开发工具\phantomjs-2.1.1-windows\bin\phantomjs.exe'

browser = webdriver.PhantomJS(path)

url = "https://www.baidu.com"
browser.get(url)

time.sleep(3)

browser.save_screenshot(r'phantomjs\baidu.png')
# 查找input输入框
my_input = browser.find_element_by_id('kw')
# 往框里面写入文字
my_input.send_keys("星际争霸")

time.sleep(3)

# 查找搜索按钮
button = browser.find_element_by_class_name('s_btn')
button.click()

time.sleep(3)

browser.save_screenshot(r'phantomjs\starcraft.png')

browser.quit()