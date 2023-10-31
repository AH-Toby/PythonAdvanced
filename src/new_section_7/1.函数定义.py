#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/30 17:06
# @Author  : toby
# @File    : 1.函数定义.py
# @Software: PyCharm
# @Desc:

def func(data):
    print(f"test is show data:{data}")


# 调用函数
func(111)

# 引用函数
ret = func

print(ret)
print(func)

# 通过引用调用函数
ret(222)


# 把函数单成参数传递
def functions(func):
    func(333)


functions(ret)
