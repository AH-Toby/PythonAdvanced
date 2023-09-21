#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 11:40
# @Author  : toby
# @File    : 61.协程-多任务实现并发wait方法.py
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
    done, pending = await asyncio.wait([task1, task2, task3])
    for done_task in done:
        print(done_task.result())  # 这里返回的是一个任务，不是直接的返回值，故而需要使用result函数进行获取


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()