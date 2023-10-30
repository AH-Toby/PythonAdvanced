#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 16:38
# @Author  : toby
# @File    : 41.__exit__方法的作用.py
# @Software: PyCharm
# @Desc:
class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self  # 返回表示上下文的对象

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type is not None:
            print(f"An exception of type {exc_type} occurred with value {exc_value}")
            with open("error.log", "a") as f:
                traceback.print_tb(traceback, file=f)
        # 可以在这里执行一些清理工作


# 使用上下文管理器
with MyContext() as context:
    print("Inside the context")
    # 在这个块中执行一些操作
    # 如果出现异常，它会在 __exit__ 中处理

print("Outside the context")
