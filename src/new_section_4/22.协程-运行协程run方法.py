#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 21:22
# @Author  : toby
# @File    : 22.协程-运行协程run方法.py
# @Software: PyCharm
# @Desc:
import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    print("Coroutine completed")


asyncio.run(my_coroutine())  # 运行协程
