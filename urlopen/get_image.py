#encoding=utf-8
import urllib.request
img_url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1552393226677&di' \
          '=cebaf8acd575c1851826d10b4fd0b8e4&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem' \
          '%2Ff3d3572c11dfa9ecf473c23368d0f703918fc1b1.jpg '

'''
写法1
response = urllib.request.urlopen(img_url)

with open('qing.jpg','wb') as fp:
    fp.write(response.read())
'''

'''
写法2
'''
urllib.request.urlretrieve(img_url,'chun.jpg')