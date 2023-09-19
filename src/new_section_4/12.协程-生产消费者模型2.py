#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/19 14:54
# @Author  : toby
# @File    : 12.协程-生产消费者模型2.py
# @Software: PyCharm
# @Desc:
import time


def consumer(name):
    print(f"{name} 准备吃包子，呼叫店小二")
    while 1:
        baozi = yield
        print(f"包子{baozi + 1}来了，被{name}吃了！")


def producer(name, c1, c2):
    next(c1)
    next(c2)
    print(f"{name}开始准备做包子啦！")
    for i in range(5):
        time.sleep(1)
        print(f'做了第{i + 1}包子，分成两半,你们一人一半')
        c1.send(i)
        c2.send(i)
        print("---" * 30)


c1 = consumer("张三")
c2 = consumer("李四")
producer("店小二", c1, c2)
