#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/22 15:59
# @Author  : toby
# @File    : 2.浅拷贝.py
# @Software: PyCharm
# @Desc:
import copy

original_list = [1, [2, 3], 4]
shallow_copy = copy.copy(original_list)
print(shallow_copy)
