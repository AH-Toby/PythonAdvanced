#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 15:04
# @Author  : toby
# @File    : 27.协程-创建任务.py
# @Software: PyCharm
# @Desc:

import asyncio


async def test_coroutine():
    await asyncio.sleep(1)
    print("Coroutine completed")


async def main():
    # 创建任务1：
    task1 = asyncio.create_task(test_coroutine())
    # 创建任务2：
    task2 = asyncio.ensure_future(test_coroutine())
    await task1
    await task2

asyncio.run(main())
