#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/15 16:59
# @Author  : toby
# @File    : 32.协程-获取返回值2.py
# @Software: PyCharm
# @Desc:
import asyncio
import time


async def hello1(a, b):
    print("Hello world 01 begin")
    await asyncio.sleep(3)  # 模拟耗时任务3秒
    print("Hello again 01 end")
    return a + b


def callback(future):  # 定义的回调函数
    print(future.result())


loop = asyncio.get_event_loop()  # 第一步：创建事件循环
task = asyncio.ensure_future(hello1(10, 5))  # 第二步:将多个协程函数包装成任务
task.add_done_callback(callback)  # 并被任务绑定一个回调函数

loop.run_until_complete(task)  # 第三步：通过事件循环运行
loop.close()  # 第四步：关闭事件循环
