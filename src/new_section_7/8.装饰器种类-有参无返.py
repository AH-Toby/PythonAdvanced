#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 11:12
# @Author  : toby
# @File    : 8.装饰器种类-有参无返.py
# @Software: PyCharm
# @Desc:
def set_func(func):
    def call_func(data):
        print(f"内部函数:{data}")
        func(data)

    return call_func


@set_func  # 相当于  operate_func = set_func(operate_func)
def operate_func(data):
    print(f"需要加操作的函数:{data}")


operate_func(111)
