#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/8 10:43
# @Author  : toby
# @File    : 3.类也是对象.py
# @Software: PyCharm
# @Desc:
class ObjectCreator(object):
    ...


my_object = ObjectCreator()
print(my_object)  # 你可以打印一个类，因为他也是对象


def echo(o):
    print(o)


echo(ObjectCreator)  # 你可以将类作为参数传递给哦函数

# 给类对象添加属性
print(hasattr(ObjectCreator, "new_attribute"))
ObjectCreator.new_attribute = "foo"
print(hasattr(ObjectCreator, "new_attribute"))

# 可以将类赋值给一个对象
ObjectCreatorMirror = ObjectCreator
print(ObjectCreatorMirror())
