#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 11:41
# @Author  : toby
# @File    : 62.协程-多任务实现并发as_completed方法.py
# @Software: PyCharm
# @Desc:
import asyncio


async def task1():
    await asyncio.sleep(2)
    return "Task 1 completed"


async def task2():
    await asyncio.sleep(1)
    return "Task 2 completed"


async def task3():
    await asyncio.sleep(3)
    return "Task 3 completed"


async def main():
    tasks = [task1(), task2(), task3()]

    for future in asyncio.as_completed(tasks):
        result = await future
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
