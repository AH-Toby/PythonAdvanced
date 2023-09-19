#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/18 17:30
# @Author  : toby
# @File    : 5.gevent添加补丁.py
# @Software: PyCharm
# @Desc:
import random
import time
import gevent
from gevent import monkey

# 未打补丁的代码
# 补丁代码, 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块
monkey.patch_all()  # 可以屏蔽后试试打完补丁前后程序运行情况


def coroutine_work(coroutine_name):
    for i in range(3):
        print(coroutine_name, i)
        time.sleep(random.randrange(1, 2))


# 执行多个任务
gevent.joinall(
    [
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2"),
    ]
)
