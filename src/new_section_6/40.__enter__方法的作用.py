#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 16:35
# @Author  : toby
# @File    : 40.__enter__方法的作用.py
# @Software: PyCharm
# @Desc:
class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self  # 返回表示上下文的对象

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        # 可以在这里执行一些清理工作


# 使用上下文管理器
with MyContext() as context:
    print("Inside the context")
    # 在这个块中执行一些操作

print("Outside the context")
