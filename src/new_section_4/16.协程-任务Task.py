#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 18:20
# @Author  : toby
# @File    : 16.协程-任务Task.py
# @Software: PyCharm
# @Desc:
import asyncio


async def test_coroutine():
    await asyncio.sleep(1)
    return "Task is complete"


async def main():
    # 创建两个任务
    task1 = asyncio.create_task(test_coroutine())
    task2 = asyncio.ensure_future(test_coroutine())

    # 等待任务完成
    result1 = await task1
    result2 = await task2

    print(result1)
    print(result2)


asyncio.run(main())
