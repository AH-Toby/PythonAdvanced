#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 18:28
# @Author  : toby
# @File    : 17.协程-任务Task获取某一个任务的方法.py
# @Software: PyCharm
# @Desc:

import asyncio


async def my_coroutine():
    current_task = asyncio.current_task()
    print(f"Current task: {current_task.get_name()}")


async def main():
    task1 = asyncio.create_task(my_coroutine())
    task2 = asyncio.create_task(my_coroutine())
    await task1
    await task2

asyncio.run(main())
