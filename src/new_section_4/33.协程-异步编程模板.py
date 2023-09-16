#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/15 17:10
# @Author  : toby
# @File    : 33.协程-异步编程模板.py
# @Software: PyCharm
# @Desc:
import asyncio


async def hello1():
    print("Hello world 01 begin")
    await asyncio.sleep(3)  # 模拟耗时任务3秒
    print("Hello again 01 end")


async def hello2():
    print("Hello world 02 begin")
    await asyncio.sleep(2)  # 模拟耗时任务2秒
    print("Hello again 02 end")


async def hello3():
    print("Hello world 03 begin")
    await asyncio.sleep(4)  # 模拟耗时任务4秒
    print("Hello again 03 end")


async def main():
    await asyncio.gather(hello1(), hello2(), hello3())

asyncio.run(main())
