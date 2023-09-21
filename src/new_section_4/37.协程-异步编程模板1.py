#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 19:26
# @Author  : toby
# @File    : 37.协程-异步编程模板1.py
# @Software: PyCharm
# @Desc: 无参无返模板

import asyncio


async def coroutine1():
    print("coroutine1 start")
    await asyncio.sleep(1)
    print("coroutine1 end")


async def coroutine2():
    print("coroutine2 start")
    await asyncio.sleep(1)
    print("coroutine2 end")


async def coroutine3():
    print("coroutine3 start")
    await asyncio.sleep(1)
    print("coroutine3 end")


async def main():
    await asyncio.gather(coroutine1(), coroutine2(), coroutine3())


asyncio.run(main())
