#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 11:43
# @Author  : toby
# @File    : 25.协程-Future对象检查完成状态.py
# @Software: PyCharm
# @Desc:
import asyncio

future = asyncio.Future()
future.set_result("Completed")

print(future.done())  # 输出 True
print(future.result())  # 输出 "Completed"
