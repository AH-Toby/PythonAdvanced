#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 15:38
# @Author  : toby
# @File    : 32.协程-按完成顺序生成结果.py
# @Software: PyCharm
# @Desc:
import asyncio


async def task1():
    await asyncio.sleep(2)
    return "task1 completed"


async def task2():
    await asyncio.sleep(1)
    return "task2 completed"


async def main():
    task_list = [task1(), task2()]
    result_list = [await result for result in asyncio.as_completed(task_list)]
    print(result_list)


asyncio.run(main())
