#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/13 14:22
# @Author  : toby
# @File    : 4.协程-生成器send的方法.py
# @Software: PyCharm
# @Desc:

# 1.send方法

def new_generator(n):
    for i in range(n):
        print(f"第{i}次运行")
        temp = yield i
        print(f"我是{temp}")
        print("-" * 30)


g = new_generator(5)
print(next(g))  # 输出0, 我是None
print(next(g))  # 输出1, 我是None
print(g.send(100))  # 输出2, 我是100, 将100 通过send传到temp
print(next(g))  # 输出3, 我是None
print(next(g))  # 输出4, 我是None
