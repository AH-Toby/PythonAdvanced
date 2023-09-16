#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/15 14:29
# @Author  : toby
# @File    : 26.协程-按完成顺序生成结果.py
# @Software: PyCharm
# @Desc:
import asyncio


async def coroutine1():
    await asyncio.sleep(2)
    return "Coroutine 1 completed"


async def coroutine2():
    await asyncio.sleep(1)
    return "Coroutine 2 completed"


async def main():
    tasks = [coroutine1(), coroutine2()]

    for completed in asyncio.as_completed(tasks):
        result = await completed
        print("Completed task:", result)


asyncio.run(main())
