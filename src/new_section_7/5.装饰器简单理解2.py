#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 10:56
# @Author  : toby
# @File    : 5.装饰器简单理解2.py
# @Software: PyCharm
# @Desc:
def set_fun(func):
    def call_func():
        print("内部代码")
        func()

    return call_func


# 要添加功能的函数
def operate_func():
    print("要添加功能的函数")


operate_func = set_fun(func=operate_func)
operate_func()
