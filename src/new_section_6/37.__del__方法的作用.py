#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 16:13
# @Author  : toby
# @File    : 37.__del__方法的作用.py
# @Software: PyCharm
# @Desc:
class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Object {self.name} is being destroyed")


# 创建 MyClass 类的对象
obj1 = MyClass("obj1")
obj2 = MyClass("obj2")

# 解除引用对象，触发 __del__ 方法
del obj1
del obj2
