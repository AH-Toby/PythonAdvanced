#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 20:42
# @Author  : toby
# @File    : 38.协程-异步编程模板2.py
# @Software: PyCharm
# @Desc:
import asyncio


async def coroutine1(a, b):
    print("coroutine1 start")
    await asyncio.sleep(1)
    print("coroutine1 end")
    return a + b


async def coroutine2(a, b):
    print("coroutine2 start")
    await asyncio.sleep(1)
    print("coroutine2 end")
    return a + b


async def coroutine3(a, b):
    print("coroutine3 start")
    await asyncio.sleep(1)
    print("coroutine3 end")
    return a + b


async def main():
    result = await asyncio.gather(coroutine1(10, 5), coroutine2(10, 5), coroutine3(10, 5))
    print(result)


asyncio.run(main())
