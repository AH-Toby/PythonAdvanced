#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 11:38
# @Author  : toby
# @File    : 60.协程-多任务实现并发gather方法.py
# @Software: PyCharm
# @Desc:
import asyncio
import time


async def hello1(a, b):
    print("Hello world 01 begin")
    await asyncio.sleep(3)  # 模拟耗时任务3秒
    print("Hello again 01 end")
    return a + b


async def hello2(a, b):
    print("Hello world 02 begin")
    await asyncio.sleep(2)  # 模拟耗时任务2秒
    print("Hello again 02 end")
    return a - b


async def hello3(a, b):
    print("Hello world 03 begin")
    await asyncio.sleep(4)  # 模拟耗时任务4秒
    print("Hello again 03 end")
    return a * b


async def main():  # 封装多任务的入口函数
    task1 = asyncio.ensure_future(hello1(10, 5))
    task2 = asyncio.ensure_future(hello2(10, 5))
    task3 = asyncio.ensure_future(hello3(10, 5))
    results = await asyncio.gather(task1, task2, task3)
    for result in results:  # 通过迭代获取函数的结果，每一个元素就是相对应的任务的返回值，顺序都没变
        print(result)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
