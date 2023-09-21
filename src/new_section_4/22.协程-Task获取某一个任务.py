#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 11:20
# @Author  : toby
# @File    : 22.协程-Task获取某一个任务.py
# @Software: PyCharm
# @Desc:
import asyncio


async def test_coroutine():
    current_task = asyncio.current_task()  # 获取当前任务
    print(f"Current task name: {current_task.get_name()}")
    await asyncio.sleep(1)


async def main():
    # 创建2个任务
    task1 = asyncio.create_task(test_coroutine(), name="Task 1")
    # 等待任务完成
    await task1


asyncio.run(main())
