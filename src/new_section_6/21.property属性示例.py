#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/26 15:48
# @Author  : toby
# @File    : 21.property属性示例.py
# @Software: PyCharm
# @Desc:
class Pager:
    def __init__(self, current_page):
        self.current_page = current_page  # 用户当前请求的页码
        self.per_items = 10  # 每页默认显示10条

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        return self.current_page * self.per_items


p = Pager(1)
print(p.start)
print(p.end)
