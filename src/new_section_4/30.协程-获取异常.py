#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/15 16:30
# @Author  : toby
# @File    : 30.协程-获取异常.py
# @Software: PyCharm
# @Desc:
import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    raise ValueError("First error")
    await asyncio.sleep(1)
    raise ValueError("Second error")


async def main():
    # 创建协程任务
    task = asyncio.create_task(my_coroutine())

    try:
        # 等待任务完成
        await task
    except asyncio.CancelledError:
        print("Task was cancelled")

    # 获取任务引发的最新异常
    exception = task.exception()
    if exception is not None:
        print("Task raised an exception:", exception)
    else:
        print("Task did not raise an exception")


asyncio.run(main())
