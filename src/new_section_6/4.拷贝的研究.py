#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/24 23:11
# @Author  : toby
# @File    : 4.拷贝的研究.py
# @Software: PyCharm
# @Desc:
import copy


# 可变对象研究
def deep_copy():
    a = [1, 2]
    b = a
    c = copy.deepcopy(a)
    print("地址---------------")
    print(id(a))
    print(id(b))
    print(id(c))
    print("值---------------")
    print(a)
    print(b)
    print(c)
    a.append(3)
    print("添加3后的值---------------")
    print(a)
    print(b)
    print(c)


def shallow_copy():
    a = [1, 2]
    b = a
    c = copy.copy(a)
    print("地址---------------")
    print(id(a))
    print(id(b))
    print(id(c))
    print("值---------------")
    print(a)
    print(b)
    print(c)
    a.append(3)
    print("添加3后的值---------------")
    print(a)
    print(b)
    print(c)


deep_copy()
print("-----" * 30)
shallow_copy()
