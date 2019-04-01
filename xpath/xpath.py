# -*- encoding: utf-8 -*-
'''
@File    :   xpath.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/1 9:31   Jonas           None
'''
 
from lxml import etree

tree = etree.parse('xpath.html')

# ret = tree.xpath('//div[@class="tang"]/ul/li[last()]/@id')

ret = tree.xpath('//div[@class="song"]')
string = ret[0].xpath('string(.)')
print(string.replace('\n','').replace('\t',''))