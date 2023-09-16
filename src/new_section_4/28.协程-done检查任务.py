#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/15 16:15
# @Author  : toby
# @File    : 28.协程-done检查任务.py
# @Software: PyCharm
# @Desc:
import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    print("Coroutine completed")


async def main():
    # 创建协程任务
    task = asyncio.create_task(my_coroutine())

    # 检查任务是否已完成
    if task.done():
        print("Task is already done")
    else:
        print("Task is not done yet")

    # 等待任务完成
    await task

    # 再次检查任务是否已完成
    if task.done():
        print("Task is now done")
    else:
        print("Task is not done yet")

asyncio.run(main())