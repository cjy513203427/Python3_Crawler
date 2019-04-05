# -*- encoding: utf-8 -*-
'''
@File    :   testlist.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/5 10:38   Jonas           存储的时候'\n'是有效的（不会真正换行，以换行符形式存储），读取过来单独使用换行符直接生效
'''
 
# lt = [{'name':'宫本武藏\n小泉'}]
# fp = open('lala.txt','w',encoding='utf8')
# string = fp.write(str(lt))
# fp.close()

fp = open('lala.txt','r',encoding='utf8')
string = fp.read()
fp.close()

# lt = list(string)
lt = eval(string)
print(type(lt))
print(lt[0]['name'])
