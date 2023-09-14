#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 21:28
# @Author  : toby
# @File    : 23.协程-创建任务.py
# @Software: PyCharm
# @Desc:
import asyncio

async def my_coroutine():
    await asyncio.sleep(1)
    print("Coroutine completed")


task = asyncio.create_task(my_coroutine())