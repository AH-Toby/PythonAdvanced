#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/26 15:37
# @Author  : toby
# @File    : 20.property属性.py
# @Software: PyCharm
# @Desc:

class Foo:

    def func(self):
        print("普通方法")

    # 定义property属性
    @property
    def prop_func(self):
        return "定义property属性"


foo_obj = Foo()
foo_obj.func()
res = foo_obj.prop_func
print(res)
