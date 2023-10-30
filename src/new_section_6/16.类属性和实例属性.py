#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/25 15:58
# @Author  : toby
# @File    : 16.类属性和实例属性.py
# @Software: PyCharm
# @Desc:

class Province(object):
    country = "中国"

    def __init__(self, name):
        self.name = name


# 创建一个实例
obj = Province("山东省")
# 访问实例属性
print(obj.name)
# 访问类属性
print(Province.country)
