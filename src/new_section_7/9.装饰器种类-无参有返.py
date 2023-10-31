#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 11:36
# @Author  : toby
# @File    : 9.装饰器种类-无参有返.py
# @Software: PyCharm
# @Desc:
def set_func(func):
    def call_func():
        return func()

    return call_func


@set_func  # 相当于  operate_func = set_func(operate_func)
def operate_func():
    return "需要加操作的函数"


ret = operate_func()
print(ret)
