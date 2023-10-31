#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 10:57
# @Author  : toby
# @File    : 6.装饰器实现.py
# @Software: PyCharm
# @Desc:
def set_fun(func):
    def call_func():
        print("内部代码")
        func()

    return call_func


@set_fun  # 这个是语法糖相当于 operate_func = set_fun(operate_func)
# 要添加功能的函数
def operate_func():
    print("要添加功能的函数")


operate_func()
