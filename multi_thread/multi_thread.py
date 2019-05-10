# -*- encoding: utf-8 -*-
'''
@File    :   multi_thread.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/4/30 15:55   Jonas           None
'''

import time
'''
一个主线程，主线程在运行
def sing():
    for x in range(1,6):
        print("唱歌")
        time.sleep(1)

def dance():
    for x in range(1,6):
        print("跳舞")
        time.sleep(1)

def main():
    sing()
    dance()

if __name__ == '__main__':
    main()
'''

'''
一个主线程，两个子线程（唱歌线程、跳舞线程）
'''

import threading

def sing(a):
    print('线程为%s,接收过来的参数为%s' %(threading.current_thread().name,a))
    for x in range(1,6):
        print("唱歌")
        time.sleep(1)

def dance(a):
    print('线程为%s,接收过来的参数为%s' % (threading.current_thread().name, a))
    for x in range(1,6):
        print("跳舞")
        time.sleep(1)

def main():
    a = '孙悟空'
    # 创建唱歌线程
    tsing = threading.Thread(target=sing,name="sing",args=(a,))
    # 创建跳舞线程
    tdance = threading.Thread(target=dance,name="dance",args=(a,))
    # 启动线程
    tsing.start()
    tdance.start()
    # 让主线程等待子线程结束之后再结束
    tsing.join()
    tdance.join()
    # 这里是主线程在运行
    print("主线程")


if __name__ == '__main__':
    main()