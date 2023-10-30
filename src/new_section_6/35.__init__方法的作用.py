#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 15:43
# @Author  : toby
# @File    : 35.__init__方法的作用.py
# @Software: PyCharm
# @Desc:
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 创建一个 MyClass 类的对象，并传递参数来初始化对象
obj = MyClass(10, 20)

# 访问对象的属性
print(f"x: {obj.x}, y: {obj.y}")
