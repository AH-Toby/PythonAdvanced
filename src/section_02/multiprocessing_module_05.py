#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：multiprocessing_module_05.py
@Author  ：Toby
@Date    ：2022/11/22 17:42 
@Description：进程间通信
"""
from multiprocessing import Queue


q = Queue(3)  # 初始化一个Queue对象，最多可接收三条put消息
q.put("消息1")
q.put("消息2")
print(q.full())
q.put("消息3")
print(q.full())

# 因为消息列队已满下面的try都会抛出异常，第一个try会等待2秒后再抛出异常，第二个Try会立刻抛出异常
try:
    q.put("消息4", timeout=2)
except Exception as e:
    print(e)
    print("消息列队已满")

try:
    q.put_nowait("消息4")
except Exception as e:
    print(e)
    print("消息列队已满")


# 推荐的方式，先判断消息列队是否已满，再写入
if not q.full():
    q.put_nowait("消息4")

# 读取消息时，先判断消息列队是否为空，再读取
if not q.empty():
    for i in range(3):
        print(q.get_nowait())
