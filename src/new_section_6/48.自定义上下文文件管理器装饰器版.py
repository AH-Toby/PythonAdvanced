#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/30 14:26
# @Author  : toby
# @File    : 48.自定义上下文文件管理器装饰器版.py
# @Software: PyCharm
# @Desc:
from contextlib import contextmanager


@contextmanager
def file(path, mode):
    f = open(path, mode)
    yield f
    f.close()


path = "output.txt"
msg = "python之禅5"
with file(path, "w") as f:
    f.write(msg)
