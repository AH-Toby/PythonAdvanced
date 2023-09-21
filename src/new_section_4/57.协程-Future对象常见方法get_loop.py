#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 11:22
# @Author  : toby
# @File    : 57.协程-Future对象常见方法get_loop.py
# @Software: PyCharm
# @Desc:
import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    return "Hello, World!"


async def main():
    # 创建一个 asyncio.Future 对象
    future = asyncio.Future()

    # 启动异步操作
    asyncio.create_task(my_coroutine()).add_done_callback(
        lambda task: future.set_result(task.result())
    )

    try:
        # 等待 asyncio.Future 完成
        await future
    except asyncio.CancelledError:
        print("Future was cancelled")

    # 获取并输出与 Future 关联的事件循环
    future_loop = future.get_loop()
    if future_loop is not None:
        print("Future is associated with the event loop.")
    else:
        print("Future is not associated with any event loop.")


if __name__ == "__main__":
    asyncio.run(main())
