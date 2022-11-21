#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：threading_module_05.py
@Author  ：Toby
@Date    ：2022/11/21 17:28 
@Description：线程的支持顺序
"""
import threading
from time import sleep


class WorkThread(threading.Thread):
    def run(self):
        sleep(1)
        print("%s:线程运行了" % self.name)


if __name__ == '__main__':
    for i in range(10):
        a = WorkThread()
        a.start()
        # 可以添加足够的延迟时间来保证子线程之间顺序执行
        # sleep(1)

