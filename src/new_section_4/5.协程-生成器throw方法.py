#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/13 16:36
# @Author  : toby
# @File    : 5.协程-生成器throw方法.py
# @Software: PyCharm
# @Desc:
# def throw_generator():
#     yield 'a'
#     yield 'b'
#     yield 'c'
#
#
# g = throw_generator()
# print(next(g))
# print(next(g))
# print('-------------------------')
# print(g.throw(StopIteration))
# print(next(g))


# def throw_generator():
#     try:
#         yield 'a'
#         yield 'b'
#         yield 'c'
#         yield 'd'
#         yield 'e'
#     except ValueError:
#         print('触发“ValueError"了')
#     except TypeError:
#         print('触发“TypeError"了')
#
#
# g = throw_generator()
# print(next(g))  # a
# print(next(g))  # b
# print('-------------------------')
# print(g.throw(ValueError))  # 触发“ValueError"了”，奔溃报StopIteration错误
# print('-------------------------')
# print(next(g))
# print(next(g))
# print('-------------------------')
# print(g.throw(TypeError))
# print('-------------------------')
# print(next(g))

def my_generator():
    while True:
        try:
            yield 'a'
            yield 'b'
            yield 'c'
            yield 'd'
            yield 'e'
        except ValueError:
            print('触发“ValueError"了')
        except TypeError:
            print('触发“TypeError"了')


g = my_generator()
print(next(g))  # a
print(next(g))  # b
print('-------------------------')
print(g.throw(ValueError))  # 触发“ValueError"了 a
print('-------------------------')
print(next(g))  # b
print(next(g))  # c
print('-------------------------')
print(g.throw(TypeError))  # 触发“TypeError"了 a
print('-------------------------')
print(next(g))  # b
