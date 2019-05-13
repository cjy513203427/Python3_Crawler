# -*- encoding: utf-8 -*-
'''
@File    :   headless_chrome.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/22 16:10   Jonas           None
'''


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
path = 'E:\开发工具\chromedriver.exe'

browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)

url = 'https://www.baidu.com'

browser.get(url)
# time.sleep(3)

browser.save_screenshot('baidu.png')

browser.quit()
