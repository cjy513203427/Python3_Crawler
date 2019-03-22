# encoding=utf-8
import urllib

post_url = 'https://fanyi.baidu.com/v2transapi'

form_data = {
    'from': 'en',
    'to': 'zh',
    'query': 'wolf',
    'simple_means_flag': '3',
    # sign和token是加密参数，对应着上述参数，需要计算
    # 算法未知
    'sign': '275695.55262',
    'token': 'f304ae599ca7b33823d950788569a0ce'
}

headers = {
    'Host': 'fanyi.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 禁止压缩
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '101',
    'Connection': 'keep-alive',
    'Cookie': 'BAIDUID=8F30C965E70B7EB8E86BEF53BBE0F335:FG=1; BIDUPSID=8F30C965E70B7EB8E86BEF53BBE0F335; '
              'PSTM=1509880444; MCITY=-127%3A; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1551534009,1552447939,'
              '1552452196,1552458037; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; '
              'SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; '
              'from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A'
              '%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; '
              'to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A'
              '%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; '
              'BDUSS'
              '=BhZjZ1dzc3aVdnNWlvMlhsMUIzNTNvN0g5a0RFOXRjMUs4dlNCMFc4dXl6SzVjQVFBQUFBJCQAAAAAAAAAAAEAAADKpqwDNTY2NDQ2NzU0NQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALI~h1yyP4dccX; pgv_pvi=3544195072; locale=zh; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1552458054',
    'Cache-Control': 'max-age=0'

}

request = urllib.request.Request(url=post_url, headers=headers)

form_data = urllib.parse.urlencode(form_data).encode()

response = urllib.request.urlopen(request, form_data)

print(response.read().decode())
