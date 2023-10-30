#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 15:47
# @Author  : toby
# @File    : 36.__str__方法的作用.py
# @Software: PyCharm
# @Desc:
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"MyClass instance with x={self.x} and y={self.y}"


# 创建一个 MyClass 类的对象
obj = MyClass(10, 20)

# 使用 str() 函数或 print() 函数来获取对象的字符串表示
print(str(obj))
