#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 15:29
# @Author  : toby
# @File    : 34.__base__的作用.py
# @Software: PyCharm
# @Desc:
class Parent:
    pass


class Child(Parent):
    pass


# 使用 __bases__ 获取子类的基类
base_classes = Child.__bases__

# 输出基类的元组
print(f"Child 继承自以下基类: {base_classes}")
