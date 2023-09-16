#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/15 16:57
# @Author  : toby
# @File    : 31.协程-获取返回值1.py
# @Software: PyCharm
# @Desc:
import asyncio


async def hello1(a, b):
    print("Hello world 01 begin")
    await asyncio.sleep(3)  # 模拟耗时任务3秒
    print("Hello again 01 end")
    return a + b


coroutine = hello1(10, 5)
loop = asyncio.get_event_loop()  # 第一步：创建事件循环
task = asyncio.ensure_future(coroutine)  # 第二步:将多个协程函数包装成任务列表
loop.run_until_complete(task)  # 第三步：通过事件循环运行
print('-------------------------------------')
print(task.result())
loop.close()


