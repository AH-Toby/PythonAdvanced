#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 16:49
# @Author  : toby
# @File    : 42.__call__方法的作用.py
# @Software: PyCharm
# @Desc:

class CallableClass:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        result = self.x + y
        return result


# 创建一个 CallableClass 类的对象
obj = CallableClass(10)

# 将对象当作函数调用
result = obj(5)

print(f"Result: {result}")
