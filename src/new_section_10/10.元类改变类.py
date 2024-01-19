#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/19 19:49
# @Author  : toby
# @File    : 10.元类改变类.py
# @Software: PyCharm
# @Desc:元类改变类

def change_class(class_name: str, supers_name: tuple, attrs: dict):
    """
    元类
    """
    # 修改属性值
    attrs["num"] = 0
    return type(class_name, supers_name, attrs)


class AA(object, metaclass=change_class):
    num = 100


print(AA.num)
