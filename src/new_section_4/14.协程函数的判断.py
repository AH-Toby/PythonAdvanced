#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 15:50
# @Author  : toby
# @File    : 14.协程函数的判断.py
# @Software: PyCharm
# @Desc:
import asyncio
import inspect


async def async_function():
    await asyncio.sleep(1)


def regular_function():
    pass


async def async_generator():
    yield 1


def regular_generator():
    yield 1


# 判断函数是否是协程函数
print(inspect.iscoroutinefunction(async_function))  # True
print(inspect.iscoroutinefunction(regular_function))  # False

# 判断函数是否是异步生成器函数
print(inspect.isasyncgenfunction(async_generator))  # True
print(inspect.isasyncgenfunction(regular_generator))  # False
