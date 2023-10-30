#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 14:11
# @Author  : toby
# @File    : 31.类级别的__module__.py
# @Software: PyCharm
# @Desc:
from person import Person

print(Person.__module__)


class MyClass:
    pass


# 使用 __module__ 获取类所在的模块的名称
module_name = MyClass.__module__
print(f"MyClass is defined in the module: {module_name}")
