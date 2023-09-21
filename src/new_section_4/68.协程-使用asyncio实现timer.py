#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 14:09
# @Author  : toby
# @File    : 68.协程-使用asyncio实现timer.py
# @Software: PyCharm
# @Desc:
import asyncio


async def delay(time):
    await asyncio.sleep(time)


async def timer(time, function):
    while True:
        future = asyncio.ensure_future(delay(time))
        await future
        future.add_done_callback(function)


def func(future):
    print('done')


if __name__ == '__main__':
    asyncio.run(timer(2, func))
