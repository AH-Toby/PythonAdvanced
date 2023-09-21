#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 21:14
# @Author  : toby
# @File    : 42.协程-计划执行回调函数1.py
# @Software: PyCharm
# @Desc:loop.call_later
import asyncio


def my_callback(arg1, arg2):
    print(f"Callback called with arguments: {arg1}, {arg2}")


async def main():
    loop = asyncio.get_event_loop()
    cancel_obj = loop.call_later(2, my_callback, "Hello", "World")
    # cancel_obj.cancel()  # 取消运行
    await asyncio.sleep(3)  # 等待足够的时间以确保回调函数执行


if __name__ == "__main__":
    asyncio.run(main())
