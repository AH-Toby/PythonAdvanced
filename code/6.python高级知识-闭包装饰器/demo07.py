# -*- coding:utf-8 -*-
def set_func(func):
    def call_fun():
        return func()
    return call_fun


@set_func
def test():
    return "test is show"


print(test())
