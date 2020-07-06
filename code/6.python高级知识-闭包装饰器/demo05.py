# -*- coding:utf-8 -*-
# 先写一个闭包


def set_fun(func):
    def call_fun():
        print('权限')
        func()

    return call_fun


@set_fun  # 这个是语法糖：相当于test = set_fun(test)
def test():
    print("test is show")


# 调用内层函数
test()
