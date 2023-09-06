#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/7 00:59
# @Author  : toby
# @File    : 8.send的使用.py
# @Software: PyCharm
# @Desc:
# 定义一个gen函数作用暂时保存，返回i的值; temp接收下次c.send("python")，send发送过来的值，c.next()等价c.send(None)

def gen():
    i = yield
    print("Received:", i)
    while True:
        i = yield i
        print("Received:", i)


# 创建生成器对象
gen = gen()

# 启动生成器
next(gen)

# 暂停在 yield 语句处，返回 i 的值
value = gen.send("Python")
print("Returned:", value)

# 继续执行，等待下一个值的发送
value = gen.send("Hello")
print("Returned:", value)
