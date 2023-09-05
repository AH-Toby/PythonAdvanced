#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/9/6 00:45
# @Author  : toby
# @File    : 5.迭代器生成斐波那锲数列.py
# @Software: PyCharm
# @Desc:
class FibIterator(object):
    """定义一个斐波那契额数列"""

    def __init__(self, nums):
        self.nums = nums  # 指明生成数列的前几个数
        self.first = 0  # 第一个数
        self.second = 1  # 第二个数
        self.count = 0  # 计数器

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.nums:
            data = self.first
            self.first, self.second = self.second, (self.first + self.second)
            self.count += 1
            return data
        else:
            raise StopIteration


if __name__ == '__main__':
    fb = FibIterator(3)
    for i in fb:
        print(i, end=",")
