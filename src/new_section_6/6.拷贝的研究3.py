#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/24 23:36
# @Author  : toby
# @File    : 6.拷贝的研究3.py
# @Software: PyCharm
# @Desc:
import copy


# 外层不可变对内层可变对象研究
def deep_copy():
    a = ([1, 2], 3)
    b = copy.deepcopy(a)
    print("地址---------------")
    print(id(a))
    print(id(b))
    print("值---------------")
    print(a)
    print(b)
    a[0].append(3)
    print("内侧添加3后的值---------------")
    print(a)
    print(b)  # 深拷贝拷贝全部


def shallow_copy():
    a = ([1, 2], 3)
    b = copy.copy(a)
    print("地址---------------")
    print(id(a))
    print(id(b))
    print("值---------------")
    print(a)
    print(b)
    a[0].append(3)
    print("内侧添加3后的值---------------")
    print(a)
    print(b)  # 浅拷贝拷贝只拷贝最外侧引用


deep_copy()
print("-----" * 30)
shallow_copy()
