#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/15 14:22
# @Author  : toby
# @File    : 25.协程-多个协程函数时间等候.py
# @Software: PyCharm
# @Desc:

import asyncio


async def coroutine1():
    await asyncio.sleep(2)
    print("Coroutine 1 completed")


async def coroutine2():
    await asyncio.sleep(1)
    print("Coroutine 2 completed")


async def main():
    tasks = [coroutine1(), coroutine2()]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for task in done:
        print("Completed task:", task)

    for task in pending:
        print("Pending task:", task)


asyncio.run(main())
