#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/8 10:22
# @Author  : toby
# @File    : 2.一切皆对象.py
# @Software: PyCharm
# @Desc:
class CC(object):
    num = 100

    def test(self):
        print("test is show")


cc = CC()
cc.test()

xx = cc
xx.test()

print(cc.__class__)  # 查看创建者
print(cc.__class__.__class__)
print(cc.__class__.__class__.__class__)
print(int.__class__)

