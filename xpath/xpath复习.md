xpath
    pip install lxml
    什么是xpath?
        xml是用来存储和传输数据使用的
        和html的不同点：
        (1)html用来显示数据,xml用来存储和传输
        (2)html标签是固定的，xml标签是自定义的
        xpath用来查找xml中查找指定的元素，是路径表达式

        常用的路径表达式
        ./：从当前结点往下查找
        ../：从当前结点的父结点往下查找
        @：选取属性

        实例：
        /bookstore/book  选取根节点bookstore直接子节点所有的book
        //book  选取所有book
        bookstore//book  选取bookstore后代的所有book
        /bookstore/book[1]  选取bookstore第一个book元素
        /bookstore/book[last()]  选取bookstore最后一个book元素
        /bookstore/book[position()<3]  选取bookstore前两个book元素
        //title[@lang]  选取所有属性名为lang的title属性
        //title[@lang='eng']   	选取所有title元素，值为eng的lang属性。
        安装xpath插件
            谷歌安装xpath helper
        启停快捷键
            ctrl+shift+x
        属性定位
            //input[@id="kw"]
            //input[@class="bg s_btn"]
        层级定位和索引定位
            //div[@id="head"]/div/div[2]/a[1]
        逻辑运算
            //input[@class="s_ipt" and @name="wd"]
        模糊匹配
            contains  //input[contains(@class,"s_i")]
            starts-with  //input[starts-with(@class,"s")]
        取文本
            //div[@id="u1"]/a[5]/text()
            //div[@id="u1"]//text()
        取属性
            //div[@id="u1"]/a[5]/@href
        将内容拼接起来返回
            ret = tree.xpath('//div[@class="song"]')
            string = ret[0].xpath('string(.)')

        代码中使用xpath
            from lxml import etree
            两种方式使用：
                将html文档变成一个对象，然后调用对象的方法去查找指定的结点
                （1）本地文件
                    tree = etree.parse(文件名)
                （2）网络文件
                    tree = etree.HTML(网页字符串)


