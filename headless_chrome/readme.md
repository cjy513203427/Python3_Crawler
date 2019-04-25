1.Headless Chrome
    无界面谷歌浏览器
    mac,linux要求版本59+以上，才支持这种模式
    windows要求版本60+以上，才支持这种模式

2.requests
    安装：pip install requests
    用来做什么？
        和urllib是功能类似、使用起来比urllib更简洁
    get请求
        r = requests.get(url=url,headers=headers)
    post请求
        r = requests.post(url=url,headers=headers)
    定制头部
        data：字典
        requests.get(url,headers=headers,params=data)
    响应对象
        r.text  字符串形式查看响应
        r.content   字节类型查看响应
        r.encoding  查看或者设置编码类型
        r.status_code   查看状态编码
        r.headers   查看响应头部
        r.url   查看所请求的url
        r.json()    查看json数据
    代理
    Cookie
        实现人人登录
    ChinaUnix
        登录思路：先get，再post，再get