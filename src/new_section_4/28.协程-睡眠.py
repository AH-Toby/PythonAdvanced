#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 15:10
# @Author  : toby
# @File    : 28.协程-睡眠.py
# @Software: PyCharm
# @Desc:
import asyncio


async def test_coroutine():
    print("start")
    result = await asyncio.sleep(1, result="睡眠")
    print(f"睡眠结果:{result}")
    print("end")

asyncio.run(test_coroutine())
