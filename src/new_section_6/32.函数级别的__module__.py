#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 14:14
# @Author  : toby
# @File    : 32.函数级别的__module__.py
# @Software: PyCharm
# @Desc:
def my_function():
    pass


# 使用 __module__ 获取函数所在的模块的名称
module_name = my_function.__module__
print(f"my_function is defined in the module: {module_name}")
