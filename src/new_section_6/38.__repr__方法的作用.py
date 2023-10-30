#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 16:27
# @Author  : toby
# @File    : 38.__repr__方法的作用.py
# @Software: PyCharm
# @Desc:
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"MyClass({self.x}, {self.y})"


# 创建一个 MyClass 类的对象
obj = MyClass(10, 20)

# 使用 repr() 函数来获取对象的官方字符串表示
repr_str = repr(obj)
print(repr_str)

# 通过官方字符串表示形式创建对象
new_obj = eval(repr_str)
print(new_obj.x, new_obj.y)
