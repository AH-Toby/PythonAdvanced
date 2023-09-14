#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 15:23
# @Author  : toby
# @File    : 13.协程yieldfrom高级用法3.py
# @Software: PyCharm
# @Desc:
def sub_generator():
    received = yield 'sub_generator says hello'
    yield f'sub_generator received: {received}'


def main_generator():
    response = yield from sub_generator()
    yield f'main_generator received: {response}'


gen = main_generator()
print(next(gen))  # 输出 'sub_generator says hello'
print(gen.send('Hi from main_generator'))  # 输出 'sub_generator received: Hi from main_generator'
