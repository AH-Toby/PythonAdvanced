#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 11:42
# @Author  : toby
# @File    : 11.装饰器种类-通用装饰器.py
# @Software: PyCharm
# @Desc:
def set_func(func):
    def call_func(*args, **kwargs):
        return func(*args, **kwargs)

    return call_func


@set_func  # 相当于  operate_func = set_func(operate_func)
def operate_func(data, name="操作函数"):
    return f"需要加操作的函数-函数参数值：{data}，{name}"


ret = operate_func(1111)
print(ret)
