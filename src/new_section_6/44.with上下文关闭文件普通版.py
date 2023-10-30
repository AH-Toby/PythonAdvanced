#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/30 14:14
# @Author  : toby
# @File    : 44.with上下文关闭文件普通版.py
# @Software: PyCharm
# @Desc:

def file(path, msg):
    f = open(path, 'w')
    f.write(msg)
    f.close()


path = "output.txt"
msg = "python之禅"
file(path, msg)
