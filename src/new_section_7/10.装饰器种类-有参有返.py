#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 11:40
# @Author  : toby
# @File    : 10.装饰器种类-有参有返.py
# @Software: PyCharm
# @Desc:
def set_func(func):
    def call_func(data):
        return func(data)

    return call_func


@set_func  # 相当于  operate_func = set_func(operate_func)
def operate_func(data):
    return f"需要加操作的函数:函数参数{data}"


ret = operate_func(111)
print(ret)
