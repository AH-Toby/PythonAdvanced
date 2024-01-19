#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/19 20:02
# @Author  : toby
# @File    : 11.自定义方法实现元类.py
# @Software: PyCharm
# @Desc:将类中所有的属性都改成大写

def change_class(class_name: str, supers_name: tuple, attrs: dict):
    new_attr = {key.upper() if not key.startswith("_") else key: value for key, value in attrs.items()}
    return type(class_name, supers_name, new_attr)


class AA(object, metaclass=change_class):
    bb = 'BB'


print(AA.BB)
