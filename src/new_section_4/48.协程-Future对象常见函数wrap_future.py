#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 21:59
# @Author  : toby
# @File    : 48.协程-Future对象常见函数wrap_future.py
# @Software: PyCharm
# @Desc:
import asyncio
import concurrent.futures


def blocking_function():
    import time
    time.sleep(2)
    return "Hello, World!"


async def main():
    # 创建一个 concurrent.futures.Future 对象
    executor = concurrent.futures.ThreadPoolExecutor()
    future = executor.submit(blocking_function)  # 启动阻塞函数

    # 使用 asyncio.wrap_future() 包装成 asyncio.Future 对象
    asyncio_future = asyncio.wrap_future(future)

    # 等待 asyncio.Future 完成
    result = await asyncio_future
    print(result)  # 输出 "Hello, World!"


if __name__ == "__main__":
    asyncio.run(main())
