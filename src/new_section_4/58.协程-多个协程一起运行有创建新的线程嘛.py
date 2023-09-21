#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 11:34
# @Author  : toby
# @File    : 58.协程-多个协程一起运行有创建新的线程嘛.py
# @Software: PyCharm
# @Desc:
import asyncio
import time
import threading

a = time.time()


async def hello1():
    print(f"Hello world 01 begin,my thread is:{threading.currentThread()}")
    await asyncio.sleep(3)
    print("Hello again 01 end")


async def hello2():
    print(f"Hello world 02 begin,my thread is:{threading.currentThread()}")
    await asyncio.sleep(2)
    print("Hello again 02 end")


async def hello3():
    print(f"Hello world 03 begin,my thread is:{threading.currentThread()}")
    await asyncio.sleep(1)
    print("Hello again 03 end")


loop = asyncio.get_event_loop()
tasks = [hello1(), hello2(), hello3()]
loop.run_until_complete(asyncio.wait(tasks))

loop.close()

b = time.time()
print('---------------------------------------')
print(b - a)
