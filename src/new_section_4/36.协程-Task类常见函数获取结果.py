#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 16:41
# @Author  : toby
# @File    : 36.协程-Task类常见函数获取结果.py
# @Software: PyCharm
# @Desc:
import asyncio


async def test_coroutine(a, b):
    await asyncio.sleep(1)
    return a + b


# 方式1，通过result函数获取
coroutine = test_coroutine(10, 5)
loop = asyncio.get_event_loop()  # 第一步：创建事件循环
task = asyncio.ensure_future(coroutine)  # 第二步:将多个协程函数包装成任务列表
loop.run_until_complete(task)  # 第三步：通过事件循环运行
print('-------------------------------------')
print(task.result())
loop.close()

# 方式2：通过定义回调函数获取
# def call_back(future):
#     print(future.result())
#
#
# loop = asyncio.get_event_loop()  # 第一步：创建事件循环
# task = asyncio.ensure_future(test_coroutine(10, 5))  # 第二步:将多个协程函数包装成任务
# task.add_done_callback(call_back)  # 并被任务绑定一个回调函数
# loop.run_until_complete(task)
# loop.close()

# 方式3，直接获取
# result = asyncio.run(test_coroutine(10, 5))
# print(result)
