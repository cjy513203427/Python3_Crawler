# -*- encoding: utf-8 -*-
'''
@File    :   firefox.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/5/10 17:07   Jonas           None
'''
 
import time
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')
# 模拟创建一个浏览器对象，然后通过对象去操作浏览器
path = 'E:\开发工具\geckodriver.exe'
browser = webdriver.Firefox(executable_path=path,firefox_options=firefox_options)

url = "https://www.baidu.com"
browser.get(url)

# time.sleep(3)
# 查找input输入框
my_input = browser.find_element_by_id('kw')
# 往框里面写入文字
my_input.send_keys("星际争霸")

# time.sleep(3)

# 查找搜索按钮
button = browser.find_element_by_class_name('s_btn')
button.click()
browser.save_screenshot('baidu222.png')

# time.sleep(3)

button = browser.find_element_by_xpath('//*[@id="2"]/h3/a')
button.click()

# time.sleep(3)

browser.quit()