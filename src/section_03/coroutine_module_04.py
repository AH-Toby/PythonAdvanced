#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：coroutine_module_04.py
@Author  ：Toby
@Date    ：2022/11/28 14:42 
@Description：
"""
"""
用生成器完成斐波那契数组
"""


def Fib(nums):
    counter = 0  # 计数器
    num1 = 0  # 第一个数据
    num2 = 1  # 第二个数据
    while counter < nums:
        data = num1
        num1, num2 = num2, num1 + num2
        counter += 1
        yield data
    return 'done'


if __name__ == '__main__':
    f = Fib(5)
    for i in Fib(5):
        print(i)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
#
#
# print(next(f))
