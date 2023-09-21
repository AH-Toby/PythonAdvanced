#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 21:02
# @Author  : toby
# @File    : 39.协程-事件循环set_task_factory方法.py
# @Software: PyCharm
# @Desc:
import asyncio


def custom_task_factory(loop, coro):
    task = asyncio.Task(coro, loop=loop)
    task.my_custom_attribute = "This is a custom attribute"
    return task


async def my_coroutine():
    await asyncio.sleep(1)


async def main():
    loop = asyncio.get_event_loop()

    # 设置自定义任务工厂
    loop.set_task_factory(custom_task_factory)

    # 创建协程任务
    task = asyncio.create_task(my_coroutine())
    await task

    # 访问自定义属性
    print(task.my_custom_attribute)


asyncio.run(main())
