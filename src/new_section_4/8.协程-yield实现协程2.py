#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/14 10:42
# @Author  : toby
# @File    : 8.协程-yield实现协程2.py
# @Software: PyCharm
# @Desc:


import time


# 定义一个消费者，他有名字name
# 因为里面有yield，本质上是一个生成器
def consumer(name):
    print(f'{name}  准备吃包子啦！,呼吁店小二')
    while True:
        baozi = yield  # 接收send传的值，并将值赋值给变量baozi
        print(f'包子 {baozi + 1} 来了,被 {name} 吃了！')


# 定义一个生产者，生产包子的店家，店家有一个名字name,并且有两个顾客c1 c2
def producer(name, c1, c2):
    next(c1)  # 启动生成器c1
    next(c2)  # 启动生成器c2
    print(f'{name} 开始准备做包子啦！')
    for i in range(5):
        time.sleep(1)
        print(f'做了第{i + 1}包子，分成两半,你们一人一半')
        c1.send(i)
        c2.send(i)
        print('------------------------------------')


c1 = consumer('张三')  # 把函数变成一个生成器
c2 = consumer('李四')
producer('店小二', c1, c2)
