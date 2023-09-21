#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 11:36
# @Author  : toby
# @File    : 59.协程-线程一定效率更高嘛.py
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
    await hello2()
    await hello1()
    print("Hello again 03 end")


loop = asyncio.get_event_loop()
tasks = [hello3()]
loop.run_until_complete(asyncio.wait(tasks))

loop.close()

b = time.time()
print('---------------------------------------')
print(b - a)
