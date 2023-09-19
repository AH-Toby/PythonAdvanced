#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/19 17:50
# @Author  : toby
# @File    : 20.协程-事件循环.py
# @Software: PyCharm
# @Desc:
import asyncio


async def test_coroutine():
    print("start")
    await asyncio.sleep(2)  # 模拟异步操作
    print("end")


# 创建事件循环
loop = asyncio.get_event_loop()

# 运行协程任务
loop.run_until_complete(test_coroutine())

# 关闭事件循环
loop.close()
