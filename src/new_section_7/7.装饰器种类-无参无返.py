#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 11:05
# @Author  : toby
# @File    : 7.装饰器种类-无参无返.py
# @Software: PyCharm
# @Desc:
def set_func(func):
    def call_func():
        print("内部函数")
        func()

    return call_func


@set_func  # 相当于  operate_func = set_func(operate_func)
def operate_func():
    print("需要加操作的函数")


operate_func()
