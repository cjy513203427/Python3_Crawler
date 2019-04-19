jsonpath
    Python处理json格式用到的函数
        import json
        json.dumps()：将字典或者列表转化为json格式的字符串
        json.loads()：将json格式字符串转化为python对象
        json.dump()：将字典或列表转化为json格式的字符串
        json.load()：从文件读取json格式的字符串，转化为python对象

    前端处理
        将json格式字符串转化为JSON对象
        JSON.parse('json格式字符串')
        eval('(' + json格式字符串 + ')')

    安装
        pip install lxml
        pip install jsonpath

    xpath和jsonpath的区别
        /   $   根元素
        .   @   当前元素
        /   .   子元素
        //  ..  任何位置
        *   *   通配符
        []  ?   过滤表达式

        xpath索引下标从1开始，jsonpath从0开始
