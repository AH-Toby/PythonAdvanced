#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 10:08
# @Author  : toby
# @File    : 50.协程-Future对象常见方法set_result.py
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

    # 等待 asyncio.Future 完成
    result = await future
    print(result)  # 输出 "Hello, World!"


if __name__ == "__main__":
    asyncio.run(main())
