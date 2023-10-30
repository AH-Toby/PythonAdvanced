#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 16:51
# @Author  : toby
# @File    : 43.索引操作.py
# @Software: PyCharm
# @Desc:
class Foo(object):

    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

result = obj['k1']  # 自动触发执行 __getitem__
obj['k2'] = 'kkk'  # 自动触发执行 __setitem__
del obj['k1']  # 自动触发执行 __delitem__
