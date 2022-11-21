#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：threading_module_04.py
@Author  ：Toby
@Date    ：2022/11/21 15:49 
@Description：线程执行代码类封装
"""

import threading


class WorkThread(threading.Thread):
    def run(self):
        print("%s:线程运行了" % self.name)


if __name__ == '__main__':
    a = WorkThread()
    a.start()
    b = WorkThread()
    b.start()
