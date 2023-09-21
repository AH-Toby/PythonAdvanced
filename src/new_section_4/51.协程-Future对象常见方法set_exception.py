#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 10:32
# @Author  : toby
# @File    : 51.协程-Future对象常见方法set_exception.py
# @Software: PyCharm
# @Desc:
import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    raise ValueError("An error occurred")


async def main():
    # 创建一个 asyncio.Future 对象
    future = asyncio.Future()

    # 启动异步操作，此处故意引发异常
    asyncio.create_task(my_coroutine()).add_done_callback(
        lambda task: future.set_exception(task.exception())
    )

    try:
        # 等待 asyncio.Future 完成
        await future
    except asyncio.CancelledError:
        print("The task was cancelled.")
    except Exception as e:
        print("An error occurred:", e)  # 输出 "An error occurred: An error occurred"


if __name__ == "__main__":
    asyncio.run(main())
