#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 11:53
# @Author  : toby
# @File    : 28.类级别的文档字符串.py
# @Software: PyCharm
# @Desc:
class MyClass:
    """
    This is the docstring of MyClass.
    It provides information about the class.
    """
    pass


print(MyClass.__doc__)  # 获取类的文档字符串
