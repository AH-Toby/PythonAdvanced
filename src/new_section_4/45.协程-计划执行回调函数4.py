#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 21:28
# @Author  : toby
# @File    : 45.协程-计划执行回调函数4.py
# @Software: PyCharm
# @Desc:
import asyncio
import threading


def my_callback(arg1, arg2):
    print(f"Callback called with arguments: {arg1}, {arg2}")


async def main():
    loop = asyncio.get_event_loop()

    # 在不同的线程中调用 loop.call_soon_threadsafe()
    thread = threading.Thread(target=lambda: loop.call_soon_threadsafe(my_callback, "Hello", "World"))
    thread.start()
    thread.join()


if __name__ == "__main__":
    asyncio.run(main())
