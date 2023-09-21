#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 21:10
# @Author  : toby
# @File    : 41.协程-事件时钟.py
# @Software: PyCharm
# @Desc:
import asyncio


async def my_coroutine():
    start_time = asyncio.get_event_loop().time()
    await asyncio.sleep(1)
    end_time = asyncio.get_event_loop().time()
    elapsed_time = end_time - start_time
    print(f"Coroutine took {elapsed_time:.2f} seconds to complete")


async def main():
    await my_coroutine()


if __name__ == "__main__":
    asyncio.run(main())
