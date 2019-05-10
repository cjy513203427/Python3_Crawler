# -*- encoding: utf-8 -*-
'''
@File    :   object_oriented_thread.py    
@Modify Time      @Author       @Desciption
------------      -------       -----------
2019/5/5 8:57   Jonas           None
'''

import threading
import time


# 写一个类,继承自threading.Thread
class SingThread(threading.Thread):
    def __init__(self, name, a):
        super().__init__()
        self.name = name
        self.a = a

    def run(self):
        print('线程为%s,接收过来的参数为%s' % (self.name, self.a))
        for x in range(1, 6):
            print("我在唱歌")
            time.sleep(1)


class DanceThread(threading.Thread):
    def __init__(self, name, a):
        super().__init__()
        self.name = name
        self.a = a

    def run(self):
        print('线程为%s,接收过来的参数为%s' % (self.name, self.a))
        for x in range(1, 6):
            print("我在跳舞")
            time.sleep(1)


def main():
    # 创建线程
    tsing = SingThread('SingThread','孙悟空')
    tdance = DanceThread('DanceThread','猪八戒')

    # 启动线程
    tsing.start()
    tdance.start()

    # 让主线程等待子线程执行结束
    tsing.join()
    tdance.join()

    print('主线程和子线程执行结束')


if __name__ == '__main__':
    main()
