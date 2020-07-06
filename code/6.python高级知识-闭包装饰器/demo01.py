# -*- coding:utf-8 -*-
def test(data):
    print("test is show")


# 调用函数
test(123)

# 引用函数
ret = test

print(ret)
print(test)

# 通过引用调用函数
ret(123)


# 把函数引用当成参数传递
def application(func):
    func(123)


application(ret)
