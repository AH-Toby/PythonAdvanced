# -*- coding:utf-8 -*-
# 实现一个简单的生成器
def my_generator(n):
    for i in range(n):
        yield i


if __name__ == '__main__':
    print(my_generator(10))

