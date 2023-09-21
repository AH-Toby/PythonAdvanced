#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 11:31
# @Author  : toby
# @File    : 23.协程-Future对象使用.py
# @Software: PyCharm
# @Desc:
import asyncio

future = asyncio.Future()
future.set_result("Completed")


async def my_coroutine():
    result = await future
    print(result)


asyncio.run(my_coroutine())  # 输出 "Completed"
