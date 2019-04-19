# -*- encoding: utf-8 -*-
'''
@File    :   taobao.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/17 14:56   Jonas           None
'''
import json
import re
import urllib.parse
import urllib.request

import jsonpath

'''P20手机tabao的评论JSON
https://rate.tmall.com/list_detail_rate.htm?itemId=566603286049&spuId=945605811&sellerId=2838892713&order=3
&currentPage=1&append=0&content=1'''

'''P20手机tabao的评论地址
https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.6f446a15gf40HZ&id=566603286049&skuId=3823664607130&areaId=340100&user_id=2838892713&cat_id=2&is_b=1&rn=53842f27e68892132989f2ddc8f3d695
'''

items_list = []
def main():
    url = "https://rate.tmall.com/list_detail_rate.htm?itemId=566603286049&spuId=945605811&sellerId=2838892713&order=3&currentPage=1&append=0&content=1"
    headers = {
        'Host': 'rate.tmall.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Referer': 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.6f446a15iEaOGH&id=566603286049&skuId=3823664607130&areaId=340100&user_id=2838892713&cat_id=2&is_b=1&rn=aee04cb327c5b71ec5920419dec38bb7',
        'Connection': 'keep-alive',
        'Cookie': 'isg=BA4O1oFK3s_AkmxY3SBuYbZRXOQQJ9MoVEh8TjhXepHMm671oB8imbRd1wdSmMqh; cna=Z/yFEkdBTBQCASQFasatX3lW; um=A502B1276E6D5FEF84BF76D5FCAABC43E29BB47A7E924DF45D48768F981D6C9E5623B3CA2B7BFC8BCD43AD3E795C914CF88213D43198F430587295A63ADD332A; enc=NbifkBuXBMEUpMo7bOkzf3tdO8A458d9azc2EAqNksTWjXt9SZRO%2BYrBcifXbH4NudjHbRaNlSdsrIzpVonb7A%3D%3D; lid=ployeeeioiaddsx; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; l=bBTpawPVvEvna5GFKOCZNuI8LJ_OSIOYYuPRwCAWi_5aK6Y_UO_Olar2pFv6Vs5RsmYB4B9rd4p9-etkm; hng=CN%7Czh-CN%7CCNY%7C156; t=23284d6e83cbda4acdedf45545a2f42e; tracknick=ployeeeioiaddsx; _tb_token_=74be38dee37e9; cookie2=1750c0fc9393b109fbf1a4b23664596d; _m_h5_tk=6a6c5d3fc78e5ae61ad8f61d56d5359a_1555492782554; _m_h5_tk_enc=c047e52596a1f54f72e266ddeafe59d5; dnk=ployeeeioiaddsx; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=W5iHLLyFe3xm&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTZ4SECZc1I5Q%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEfL89LsRGqlBR8%3D&id2=UUtIHRUDpg1jdg%3D%3D&nk2=E6g%2BeSGnSpDaU6vKca9i&lg2=WqG3DMC9VAQiUQ%3D%3D; _l_g_=Ug%3D%3D; unb=2338911265; lgc=ployeeeioiaddsx; cookie1=BxuQhco%2Fopwf6orV%2F4Ich8djfPnT%2B8%2Bf6lPiGdXOjRo%3D; login=true; cookie17=UUtIHRUDpg1jdg%3D%3D; _nk_=ployeeeioiaddsx; sg=x52; csg=8c51ddf4; whl=-1%260%260%260; x=__ll%3D-1%26_ato%3D0',
    }
    # 看评论需要登录环境，故使用Cookie
    request = urllib.request.Request(url=url, headers=headers)
    json_text = urllib.request.urlopen(request).read().decode()
    # print(json_text)
    # 比正则更简洁的去除字符串头尾的字符的方法
    # json_text = json_text.strip('() \t\n\rjsonp128')
    json_text = re.sub(r'jsonp128\(', '', json_text)
    json_text = re.sub(r'\)', '', json_text)
    # 将json格式字符串转化为python对象
    obj = json.loads(json_text)
    # print(obj)

    # 抓取评论内容
    # 用户名、评论内容、评论时间、手机类型

    # 取出rateDetail下的rateList
    commons_list = obj['rateDetail']['rateList']
    # print(commons_list)
    for comment in commons_list:
        # 用户名
        displayUserNick = jsonpath.jsonpath(comment, '$..displayUserNick')[0]
        # 评论内容
        rateContent = jsonpath.jsonpath(comment, '$..rateContent')[0]
        # 评论日期
        rateDate = jsonpath.jsonpath(comment, '$..rateDate')[0]
        # 手机信息
        auctionSku = jsonpath.jsonpath(comment, '$..auctionSku')[0]

        item = {
            '用户名':displayUserNick,
            '评论内容':rateContent,
            '评论日期':rateDate,
            '手机信息':auctionSku,
        }
        items_list.append(item)
        # print(item)

if __name__ == '__main__':
    main()
    # ensure_ascii禁止存储成ASCII码形式
    string = json.dumps(items_list,ensure_ascii=False)
    with open('Kommentar.txt','w',encoding='utf8') as fp:
        fp.write(string)