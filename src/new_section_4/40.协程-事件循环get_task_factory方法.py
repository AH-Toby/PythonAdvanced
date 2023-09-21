#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 21:06
# @Author  : toby
# @File    : 40.协程-事件循环get_task_factory方法.py
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

    # 获取当前事件循环的任务工厂
    current_task_factory = loop.get_task_factory()
    print("Current task factory:", current_task_factory)


asyncio.run(main())
