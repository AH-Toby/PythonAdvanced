#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 21:37
# @Author  : toby
# @File    : 47.协程-Future对象常见函数ensure_future.py
# @Software: PyCharm
# @Desc:
import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    return "Hello, World!"


async def main():
    # 使用 asyncio.ensure_future() 创建一个 Task 对象
    task = asyncio.ensure_future(my_coroutine())

    # 将任务添加到事件循环中
    result = await task

    print(result)  # 输出 "Hello, World!"


if __name__ == "__main__":
    asyncio.run(main())
