#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 15:54
# @Author  : toby
# @File    : 15.协程-事件循环1.py
# @Software: PyCharm
# @Desc:
import asyncio


async def my_coroutine():
    print("Start")
    await asyncio.sleep(2)  # 模拟异步操作
    print("End")


# my_coroutine()  # 如果单独运行指挥返回一个协程对象
# 创建事件循环
loop = asyncio.get_event_loop()

# 运行协程任务
loop.run_until_complete(my_coroutine())

# 关闭事件循环
loop.close()
