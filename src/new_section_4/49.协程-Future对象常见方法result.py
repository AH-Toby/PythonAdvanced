#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 22:16
# @Author  : toby
# @File    : 49.协程-Future对象常见方法result.py
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
    await asyncio.sleep(2)  # 确保协程完成运行
    try:
        # 等待 asyncio.Future 完成并获取结果
        result = future.result()
        print(result)  # 输出 "Hello, World!"
    except asyncio.CancelledError:
        print("The task was cancelled.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    asyncio.run(main())
