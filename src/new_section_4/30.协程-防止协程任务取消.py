#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 15:16
# @Author  : toby
# @File    : 30.协程-防止协程任务取消.py
# @Software: PyCharm
# @Desc:
import asyncio


async def test_coroutine():
    await asyncio.sleep(1)
    print("coroutine run completed")


async def main():
    # 创建一个协程任务并使用shield来保护它
    task = asyncio.create_task(test_coroutine())
    await asyncio.shield(task)
    print("task completed")

asyncio.run(main())
