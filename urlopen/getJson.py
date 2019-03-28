# encoding=utf-8
import json
import urllib.request

'''
https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=664&workExperience=-1&education=-1&companyType=-1
&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&_v=0.57983897&x-zp-page-request-id
=3c782edf718b46c3972e4f9912b09c8f-1553738888842-156115
'''
# url = 'https://sou.zhaopin.com?'
url = 'https://fe-api.zhaopin.com/c/i/sou?'
# 参数写成一个字典

data = {
    'cityId': '合肥',
    'kw': '算法工程师',
    # 起始偏移量
    'start': '0',
    # 最大100
    'pageSize': '100',
    # 未知的必需参数
    'kt': '3',

}


def print_keyvalue_all(input_json):
    key_value = ''

    if isinstance(input_json, dict):  # isinstance() 函数来判断一个对象是否是一个已知的类型

        for key in input_json.keys():  # keys() 函数以列表返回一个字典所有的键。

            key_value = input_json.get(key)  # get() 函数返回指定键的值，如果值不在字典中返回默认值。

            if isinstance(key_value, dict):  # dict字典

                print_keyvalue_all(key_value)

            elif isinstance(key_value, list):

                for json_array in key_value:
                    print_keyvalue_all(json_array)

            else:

                print(str(key) + " = " + str(key_value))

    elif isinstance(input_json, list):

        for input_json_array in input_json:
            print_keyvalue_all(input_json_array)


def print_keyvalue_by_key(input_json, key):
    key_value = ''
    if isinstance(input_json, dict):
        for json_result in input_json.values():
            if key in input_json.keys():
                key_value = input_json.get(key)
            else:
                print_keyvalue_by_key(json_result, key)
    elif isinstance(input_json, list):
        for json_array in input_json:
            print_keyvalue_by_key(json_array, key)
    if key_value != '':
        print(str(key) + " = " + str(key_value))


query_string = urllib.parse.urlencode(data)
url += query_string

response = urllib.request.urlopen(url)
hjson = json.loads(response.read())
# print(print_keyvalue_all(hjson))
print(print_keyvalue_by_key(hjson, 'eduLevel'))
