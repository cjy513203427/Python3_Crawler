简单使用
    使用方式:可以将一个html文档，转化为指定的对象
    通过对象的方法或者属性去查找指定的内容
        (1)转化为本地文件
            soup = BeautifulSoup(open('本地文件'),'lxml')
        (2)转化为网络文件
            soup = BeautifulSoup('字符串类型或者字节类型','lxml')
    1.根据标签名查找
        soup.a  只能找到第一个符合要求的标签
    2.获取属性
        soup.a.attrs    获取所有属性和值，返回一个字典
        soup.a.attrs['href']    获取href属性
        soup.a['href']    也可简写为这种形式
    3.获取内容
        soup.a.string
        soup.a.text
        soup.a.get_text()
        如果标签里面还存在标签，那么string获取到的结果为None
        其他两个可以直接获取内容
    4.find
        soup.find('a')  找到第一个符合要求的a
        soup.find('a' tile='XXX')
        soup.find('a',alt='XXX')
        soup.find('a',class_='XXX')
        soup.find('a',id='XXX')
    5.find_allW
        soup.find_all('a')
        soup.find_all(['a','b'])
        soup.find_all('a',limit=2) 取出前两个
    6.select
        根据选择器选择指定的内容
        常见选择器：标签选择器，类选择器，id选择器，并集选择器，组合选择器，层级选择器，伪类选择器，属性选择器
            标签选择器：a
            类选择器：.dudu
            id选择器：#lala
            组合选择器：a,.dudu,#lala,.meme
            div .dudu #lala .meme .xix 下面好多级
            div > p > a > .lala 只能是下面一级
            input[name='lala']
            select返回的是列表

