#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 21:11
# @Author  : toby
# @File    : 21.协程-Future对象4.py
# @Software: PyCharm
# @Desc:
import asyncio

future = asyncio.Future()
future.set_result("Completed")

print(future.done())    # 输出 True
print(future.result())  # 输出 "Completed"
