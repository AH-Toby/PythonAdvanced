#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 11:58
# @Author  : toby
# @File    : 29.函数或方法级别的文档字符串.py
# @Software: PyCharm
# @Desc:
def my_function():
    """
    This is the docstring of my_function.
    It provides information about what the function does.
    """
    pass


print(my_function.__doc__)  # 获取函数的文档字符串
