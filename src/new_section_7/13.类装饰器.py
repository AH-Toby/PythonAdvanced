#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 11:57
# @Author  : toby
# @File    : 13.类装饰器.py
# @Software: PyCharm
# @Desc:

class Func(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("类装饰器运行")
        return self.func(*args, **kwargs)


@Func  # 相当于 operate_func[作为引用] = Func(operate_func)
def operate_func(data):
    return f"类装饰器输入值{data}"


ret = operate_func(111)  # operate_func[作为引用(111)
print(ret)
