#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 10:55
# @Author  : toby
# @File    : 53.协程-Future对象常见方法cancelled.py
# @Software: PyCharm
# @Desc:
import asyncio


async def my_coroutine():
    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Coroutine was cancelled")


async def main():
    task = asyncio.create_task(my_coroutine())
    await asyncio.sleep(0.5)  # 在0.5秒后取消任务
    task.cancel()

    if task.cancelled():
        print("Task was cancelled")
    else:
        print("Task was not cancelled")


if __name__ == "__main__":
    asyncio.run(main())
