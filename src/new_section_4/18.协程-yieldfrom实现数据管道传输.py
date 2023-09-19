#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/19 17:10
# @Author  : toby
# @File    : 18.协程-yieldfrom实现数据管道传输.py
# @Software: PyCharm
# @Desc:
def sub_generator():
    receiver = yield "sub_generator says hello"
    yield f"sub_generator receive:{receiver}"


def main_generator():
    response = yield from sub_generator()
    yield f"main_generator receive:{response}"


gen = main_generator()
print(next(gen))  # 启动协程
print(gen.send("main 发送消息"))
# print(gen.send("main 发送消息"))
print(next(gen))
