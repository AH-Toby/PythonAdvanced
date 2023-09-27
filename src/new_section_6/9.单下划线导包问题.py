#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/25 14:46
# @Author  : toby
# @File    : 9.单下划线导包问题.py
# @Software: PyCharm
# @Desc:
import person

print(person._from_package)  # 可以访问到

from person import *
# print(_from_package)  # 访问不到

from person import _from_package  # 可以导包得到并访问
print(_from_package)
