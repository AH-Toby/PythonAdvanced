#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/21 10:48
# @Author  : toby
# @File    : 52.协程-Future对象常见方法done.py
# @Software: PyCharm
# @Desc:
import asyncio


async def test_coroutine():
    await asyncio.sleep(1)
    return "hello word"


async def main():
    future = asyncio.Future()
    # 启动异步函数
    asyncio.create_task(test_coroutine()).add_done_callback(
        lambda task: future.set_result(task.result())
    )
    await asyncio.sleep(2)  # 确保协程完成
    # 检查 asyncio.Future 是否已完成
    if not future.done():
        print("Future is not yet done.")
    else:
        result = future.result()
        print("Future result:", result)  # 输出 "Future result: Hello, World!"


if __name__ == '__main__':
    asyncio.run(main())
