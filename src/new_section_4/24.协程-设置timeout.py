#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/15 11:43
# @Author  : toby
# @File    : 24.协程-设置timeout.py
# @Software: PyCharm
# @Desc:
# import asyncio
#
#
# async def test_coroutine():
#     await asyncio.sleep(2)
#     print("协程运行完成")
#
#
# async def main():
#     try:
#         await asyncio.wait_for(test_coroutine(), timeout=1)
#     except asyncio.TimeoutError:
#         print("Timeout Error")
#
# asyncio.run(main())

# `asyncio.wait_for(test_coroutine(), timeout=1)` 等待 `test_coroutine` 协程完成，但设置了最大等待时间为1秒。
# 由于协程需要2秒才能完成，因此在1秒内没有完成，将引发 `asyncio.TimeoutError` 异常。
import asyncio


async def test_coroutine():
    await asyncio.sleep(0.5)
    print("协程运行完成")


async def main():
    try:
        await asyncio.wait_for(test_coroutine(), timeout=1)
    except asyncio.TimeoutError:
        print("Timeout Error")


asyncio.run(main())
