#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 11:08
# @Author  : toby
# @File    : 55.协程-Future对象常见方法cancel.py
# @Software: PyCharm
# @Desc:
import asyncio


async def my_coroutine():
    try:
        await asyncio.sleep(1)
        print("Coroutine completed")
    except asyncio.CancelledError:
        print("Coroutine was cancelled")


async def main():
    # 启动异步操作
    task = asyncio.create_task(my_coroutine())
    await asyncio.sleep(0.4)
    task.cancel()

    # 去报任务被取消

    if task.cancelled():
        print("task was cancelled")
    else:
        print("task was not cancelled")


if __name__ == "__main__":
    asyncio.run(main())
