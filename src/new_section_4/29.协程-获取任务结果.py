#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/15 16:24
# @Author  : toby
# @File    : 29.协程-获取任务结果.py
# @Software: PyCharm
# @Desc:

import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    return "Coroutine completed"


async def main():
    # 创建协程任务
    task = asyncio.create_task(my_coroutine())

    # 等待任务完成
    await task

    # 获取任务的结果
    result = task.result()
    print("Task result:", result)


asyncio.run(main())
