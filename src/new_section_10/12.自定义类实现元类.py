#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/19 20:09
# @Author  : toby
# @File    : 12.自定义类实现元类.py
# @Software: PyCharm
# @Desc:
from typing import Type


class ChangeClass(type):
    def __new__(cls, class_name: str, class_bases: tuple, class_dict: dict) -> Type:
        new_class_dict = {key.upper() if not key.startswith("_") else key: value for key, value in class_dict.items()}
        return super().__new__(cls, class_name, class_bases, new_class_dict)


class AA(object, metaclass=ChangeClass):
    bb = 'BB'


print(AA.BB)
