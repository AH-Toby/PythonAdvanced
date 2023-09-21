#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 16:37
# @Author  : toby
# @File    : 35.协程-Task类常见函数result.py
# @Software: PyCharm
# @Desc:
import asyncio


async def test_coroutine():
    await asyncio.sleep(1)
    return "coroutine completed"


async def main():
    task = asyncio.create_task(test_coroutine())
    await task
    result = task.result()
    print(f"task result:{result}")

asyncio.run(main())
