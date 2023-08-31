# -*- coding: utf-8 -*-
# @Time    : 2023/8/31 23:23
# @Author  : toby
# @File    : 4.线程代码类封装以及线程执行顺序.py
# @Software: PyCharm
# @Desc:
import threading


class MyThread(threading.Thread):
    def run(self):
        # 重写run方法
        print(f"{self.name}:线程运行了")


if __name__ == '__main__':
    for i in range(10):
        a = MyThread()
        a.start()


