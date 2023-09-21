#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 21:23
# @Author  : toby
# @File    : 43.协程-计划执行回调函数2.py
# @Software: PyCharm
# @Desc:
import asyncio


def my_callback(arg1, arg2):
    print(f"Callback called with arguments: {arg1}, {arg2}")


async def main():
    loop = asyncio.get_event_loop()
    current_time = loop.time()  # 获取当前时间戳

    # 计算未来的绝对时间点（例如，2 秒后）
    target_time = current_time + 2

    # 使用 loop.call_at() 安排回调函数在未来的特定时间点执行
    loop.call_at(target_time, my_callback, "Hello", "World")

    await asyncio.sleep(3)  # 等待足够的时间以确保回调函数执行


if __name__ == "__main__":
    asyncio.run(main())
