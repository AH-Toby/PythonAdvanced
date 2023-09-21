#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 21:36
# @Author  : toby
# @File    : 46.协程-Future对象常见函数isfuture.py
# @Software: PyCharm
# @Desc:
import asyncio


async def my_coroutine():
    await asyncio.sleep(1)


async def main():
    future = asyncio.create_task(my_coroutine())

    print(asyncio.isfuture(future))  # 输出 True
    print(asyncio.isfuture("Hello"))  # 输出 False


if __name__ == "__main__":
    asyncio.run(main())
