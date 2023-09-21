#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 16:25
# @Author  : toby
# @File    : 34.协程-Task类常见函数done.py
# @Software: PyCharm
# @Desc:
import asyncio


async def test_coroutine():
    await asyncio.sleep(1)
    print("coroutine complete")


async def main():
    # 创建协程任务
    task = asyncio.create_task(test_coroutine())

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
