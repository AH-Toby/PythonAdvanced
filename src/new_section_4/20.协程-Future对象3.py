#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 21:07
# @Author  : toby
# @File    : 20.协程-Future对象3.py
# @Software: PyCharm
# @Desc:
import asyncio

future = asyncio.Future()
future.set_exception(ValueError("Something went wrong"))


async def my_coroutine():
    try:
        await future
    except ValueError as e:
        print(f"Caught exception: {e}")


asyncio.run(my_coroutine())  # 输出 "Caught exception: Something went wrong"
