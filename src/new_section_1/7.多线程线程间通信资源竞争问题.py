# -*- coding: utf-8 -*-
# @Time    : 2023/9/1 00:19
# @Author  : toby
# @File    : 7.多线程线程间通信资源竞争问题.py
# @Software: PyCharm
# @Desc:
import threading

# 共享资源
counter = 0


def increment():
    global counter
    for _ in range(100000):
        counter += 1


def decrement():
    global counter
    for _ in range(100000):
        counter -= 1


# 创建多个线程并启动
threads = []
for _ in range(10):
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=decrement)
    threads.append(t1)
    threads.append(t2)
    t1.start()
    t2.start()

# 等待所有线程执行完毕
for t in threads:
    t.join()

# 打印最终的共享资源值
print("Counter:", counter)
