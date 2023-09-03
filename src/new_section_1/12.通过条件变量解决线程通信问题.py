#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/4 00:45
# @Author  : toby
# @File    : 12.通过条件变量解决线程通信问题.py
# @Software: PyCharm
# @Desc:

import threading

# 创建条件变量
# 条件变量允许一个或多个线程等待特定条件的发生，然后通知其他线程，以实现线程之间的协作。
condition = threading.Condition()

shared_list = []  # 共享数据


def add_to_shared_list(item):
    with condition:
        # 修改共享数据
        shared_list.append(item)
        # 通知其他线程数据已更新
        condition.notify_all()


def remove_from_shared_list():
    with condition:
        while len(shared_list) == 0:
            # 等待共享数据不为空
            condition.wait()  # 通知其他线程为空

        # 修改共享数据
        item = shared_list.pop(0)
        return item


# 创建多个线程并启动
threads = []
for i in range(3):
    t = threading.Thread(target=add_to_shared_list, args=(i,))
    t.start()
    threads.append(t)

# 创建一个线程来消费共享数据
consumer_thread = threading.Thread(target=remove_from_shared_list)

# 启动消费者线程
consumer_thread.start()

# 等待所有线程执行完毕
for t in threads:
    t.join()

# 等待消费者线程执行完毕
consumer_thread.join()

# 打印最终的共享数据
print("Shared list:", shared_list)
