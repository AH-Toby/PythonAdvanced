#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/20 11:33
# @Author  : toby
# @File    : 24.协程-Future对象异常处理.py
# @Software: PyCharm
# @Desc:
import asyncio

# 创建一个 Future 对象
future = asyncio.Future()

# 将 Future 对象的结果设置为异常
exception = ValueError("Custom exception")
future.set_exception(exception)

# 在 Future 对象上等待结果
try:
    result = asyncio.run(future)
    print(f"Future result: {result}")
except Exception as e:
    print(f"Error while waiting for Future: {e}")

