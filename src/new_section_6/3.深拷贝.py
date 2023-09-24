#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/24 23:09
# @Author  : toby
# @File    : 3.深拷贝.py
# @Software: PyCharm
# @Desc:
import copy

original_list = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original_list)
print(deep_copy)
