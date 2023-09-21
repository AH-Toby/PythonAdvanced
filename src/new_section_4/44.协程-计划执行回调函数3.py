#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 21:27
# @Author  : toby
# @File    : 44.协程-计划执行回调函数3.py
# @Software: PyCharm
# @Desc:
import asyncio


def my_callback(arg1, arg2):
    print(f"Callback called with arguments: {arg1}, {arg2}")


async def main():
    loop = asyncio.get_event_loop()

    # 使用 loop.call_soon() 调度回调函数立即执行
    loop.call_soon(my_callback, "Hello", "World")

    await asyncio.sleep(0.1)  # 等待一小段时间以确保回调函数执行


if __name__ == "__main__":
    asyncio.run(main())
