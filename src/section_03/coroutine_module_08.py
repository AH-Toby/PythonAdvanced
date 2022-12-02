#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：coroutine_module_08.py
@Author  ：Toby
@Date    ：2022/12/2 16:29 
@Description：gevent交替执行
"""
import gevent


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # 用来模拟一个耗时操作，注意不是time模块中的sleep
        gevent.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)
    g1.join()
    g2.join()
    g3.join()
