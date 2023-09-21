#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 15:26
# @Author  : toby
# @File    : 31.协程-设置运行超时时间.py
# @Software: PyCharm
# @Desc:

import asyncio


async def test_coroutine():
    await asyncio.sleep(3)  # 等待时间会超过协程设置的超时时间导致抛出错误
    print("协程运行完成")


async def main():
    try:
        await asyncio.wait_for(test_coroutine(), timeout=2)
    except asyncio.TimeoutError as e:
        print("超时")

asyncio.run(main())
