#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 15:32
# @Author  : toby
# @File    : 32.协程-多个协程函数时间等待.py
# @Software: PyCharm
# @Desc:
import asyncio


async def coroutine1():
    await asyncio.sleep(2)
    print("协程1函数运行完成")


async def corotine2():
    await asyncio.sleep(1)
    print("协程2函数运行完成")


async def main():
    task_list = [coroutine1(), corotine2()]
    done, pending = await asyncio.wait(task_list, return_when=asyncio.FIRST_COMPLETED)
    print(done)
    print(len(pending))

asyncio.run(main())
