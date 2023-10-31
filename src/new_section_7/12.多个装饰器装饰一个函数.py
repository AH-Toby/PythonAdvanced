#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 11:45
# @Author  : toby
# @File    : 12.多个装饰器装饰一个函数.py
# @Software: PyCharm
# @Desc:
def set_func1(func):
    print("set_func1执行了")

    def call_func(*args, **kwargs):
        print("call_func1执行了")
        return func(*args, **kwargs)

    return call_func


def set_func2(func):
    print("set_func2执行了")

    def call_func(*args, **kwargs):
        print("call_func2执行了")
        return func(*args, **kwargs)

    return call_func


@set_func2
@set_func1  # 相当于  operate_func = set_func(operate_func)
def operate_func(data, name="操作函数"):
    return f"需要加操作的函数-函数参数值：{data}，{name}"


ret = operate_func(1111)
print(ret)
