#!/usr/bin/python
# http://blog.chinaunix.net/uid-27571599-id-3484048.html


import threading
import time
 
def worker():
    print "test"
    time.sleep(1)
 
for i in xrange(5):
    t = threading.Thread(target=worker)
    t.start()
 
print "current has %d threads" % (threading.activeCount() - 1)

# threading.Thread(target=worker, args=())
# threading.activeCount()  
# threading.enumerate()的使用。此方法返回当前运行中的Thread对象列表
# threading.setDaemon()的使用。设置后台进程。
# t=threading.Thread(target=worker)
# t.setDaemon(True)
# t.start()


# python threading 两种创建方式
# 1、调用函数

# 要使用Thread，最简单的方法就是用一个目标函数实例化一个Thread对象，并调用start()让它开始工作。

import threading

def worker(num):
    print 'worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start


 

# 2、派生进程

# 开始时，Thread要完成一些基本初始化，然后调用其run()方法，这会调用传递到构造函数的目标函数。要创建Thrad的一个子类，需要覆盖run()来完成所需的工作。

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                   )

class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')
        return

for i in range(5):
    t = MyThread()
    t.start()

