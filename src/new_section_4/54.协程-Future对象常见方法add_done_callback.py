#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 11:06
# @Author  : toby
# @File    : 54.协程-Future对象常见方法add_done_callback.py
# @Software: PyCharm
# @Desc:
import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    return "Hello, World!"


def callback(future):
    if future.cancelled():
        print("Future was cancelled")
    elif future.done() and not future.cancelled():
        result = future.result()
        print("Future result:", result)


async def main():
    # 创建一个 asyncio.Future 对象
    future = asyncio.Future()

    # 添加回调函数
    future.add_done_callback(callback)

    # 启动异步操作
    asyncio.create_task(my_coroutine()).add_done_callback(
        lambda task: future.set_result(task.result())
    )

    try:
        # 等待 asyncio.Future 完成
        await future
    except asyncio.CancelledError:
        print("Future was cancelled")


if __name__ == "__main__":
    asyncio.run(main())
