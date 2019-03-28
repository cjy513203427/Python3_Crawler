from bs4 import BeautifulSoup

#生成对象
soup = BeautifulSoup(open('soup_test.html',encoding='utf8'),'lxml')

# print(soup.a)
# print(soup.a['href'])
# print(soup.a.attrs['href'])

# print(soup.a.get_text())

# print(soup.div.get_text())

# print(soup.find('a'))

# print(soup.find('a',title="qin"))

# print(soup.find('a',class_="du"))

# div = soup.find('div',class_="song")
# print(div.find_all(['a','b']))

# print(soup.select('.tang>ul>li>a')[3])
# print(soup.select('#qiwang'))

div = soup.find('div',class_="tang")
print(div.select('#qiwang'))