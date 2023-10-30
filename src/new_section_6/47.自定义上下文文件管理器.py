#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/30 14:20
# @Author  : toby
# @File    : 47.自定义上下文文件管理器.py
# @Software: PyCharm
# @Desc:
class File(object):
    def __init__(self, path, mode):
        self.file_path = path
        self.mode = mode

    def __enter__(self):
        self.f = open(self.file_path, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


path = "output.txt"
msg = "python之禅4"
with File(path, "w") as f:
    f.write(msg)
