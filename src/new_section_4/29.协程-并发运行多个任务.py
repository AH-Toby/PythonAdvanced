#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 15:12
# @Author  : toby
# @File    : 29.协程-并发运行多个任务.py
# @Software: PyCharm
# @Desc:
import asyncio


async def coroutine1():
    await asyncio.sleep(1)
    print("coroutine1 completed")


async def coroutine2():
    await asyncio.sleep(1)
    print("coroutine2 completed")


async def main():
    # 同时运行两个协程
    await asyncio.gather(coroutine1(), coroutine2())
    print("运行了两个协程")

asyncio.run(main())
