# -*- encoding: utf-8 -*-
'''
@File    :   yidong.py
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/5/20 18:00   Jonas           None
'''


from lxml import etree

tree = etree.parse('login_success.html')
# ret = tree.xpath('//*[@id="title_QRDMP0008"]')
ret = tree.xpath('/html/body/div[4]/div[1]/div[2]/ul/li[4]/p/a')
print(ret)