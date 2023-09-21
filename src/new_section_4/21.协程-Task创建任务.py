#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 11:06
# @Author  : toby
# @File    : 21.协程-Task创建任务.py
# @Software: PyCharm
# @Desc:
import asyncio


async def test_coroutine():
    await asyncio.sleep(1)
    return "Task is complete"


async def main():
    # 创建2个任务
    task1 = asyncio.create_task(test_coroutine())
    task2 = asyncio.create_task(test_coroutine())

    # 等待任务完成
    result1 = await task1
    result2 = await task2
    print(result1)
    print(result2)


asyncio.run(main())
