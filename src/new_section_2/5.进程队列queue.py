#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/5 00:27
# @Author  : toby
# @File    : 5.进程队列queue.py
# @Software: PyCharm
# @Desc:
from multiprocessing import Queue

q = Queue(3)  # 创建长度为3的队列
q.put("消息1")  # 推送消息
q.put("消息2")
print(q.full())  # 队列是否已满
q.put("消息3")
print(q.full())  # 队列是否已满

# try:
#     q.put("消息4", timeout=2)
# except Exception as e:
#     print(e)
#     print("消息列队已满")
#
# try:
#     q.put_nowait("消息4")
# except Exception as e:
#     print(e)
#     print("消息列队已满")

# 推荐写法
if not q.full():
    q.put_nowait("消息4")

# 获取消息时应该先判断消息队列是否为空再读取
for i in range(3):
    if not q.empty():
        print(q.get_nowait())