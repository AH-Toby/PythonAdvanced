#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/30 14:18
# @Author  : toby
# @File    : 46.with上下文关闭文件高级版.py
# @Software: PyCharm
# @Desc:
def file(path, msg):
    with open(path, "w") as f:
        f.write(msg)


path = "output.txt"
msg = "python之禅3"
file(path, msg)
