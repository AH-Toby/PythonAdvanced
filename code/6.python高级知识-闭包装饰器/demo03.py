# -*- coding:utf-8 -*-
# 先写一个闭包


def set_fun(func):
    def call_fun():
        print('权限')
        func()

    return call_fun


def test():
    print("test is show")


# 把args指向test函数引用
args = test
# 把test函数引用传入闭包获取到内层函数的引用，将a指向内层函数的引用
a = set_fun(args)
# 调用内层函数
a()

