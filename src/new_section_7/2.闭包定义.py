#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/30 17:28
# @Author  : toby
# @File    : 2.闭包定义.py
# @Software: PyCharm
# @Desc:

def func(num):
    def func_in(number_in):
        print(f"func_in函数，number_in is {number_in}")
        return num + number_in

    return func_in


ret = func(10)
print(ret)
final_rest = ret(200)
print(final_rest)
