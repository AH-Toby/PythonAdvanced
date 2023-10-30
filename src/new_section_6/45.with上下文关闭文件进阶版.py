#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/30 14:16
# @Author  : toby
# @File    : 45.with上下文关闭文件进阶版.py
# @Software: PyCharm
# @Desc:
def file(path, msg):
    f = open(path, 'w')
    try:
        f.write(msg)
    except IOError:
        print("open error")
    finally:
        f.close()


path = "output.txt"
msg = "python之禅2"
file(path, msg)
