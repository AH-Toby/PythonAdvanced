#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 15:01
# @Author  : toby
# @File    : 26.协程-运行协程.py
# @Software: PyCharm
# @Desc:
import asyncio


async def test_coroutine():
    await asyncio.sleep(1)
    print("Coroutine completed")


asyncio.run(test_coroutine())
