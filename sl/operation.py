# -*- encoding: utf-8 -*-
'''
@File    :   operation.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/18 15:34   Jonas           None
'''
import time

from selenium import webdriver

# 模拟创建一个浏览器对象，然后通过对象去操作浏览器
path = 'E:\开发工具\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)

url = "https://www.baidu.com"
browser.get(url)

time.sleep(3)
# 查找input输入框
my_input = browser.find_element_by_id('kw')
# 往框里面写入文字
my_input.send_keys("星际争霸")

time.sleep(3)

# 查找搜索按钮
button = browser.find_element_by_class_name('s_btn')
button.click()

time.sleep(3)

button = browser.find_element_by_xpath('//*[@id="2"]/h3/a')
button.click()

time.sleep(3)

browser.quit()
