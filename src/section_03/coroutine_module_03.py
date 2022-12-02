#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：PythonAdvanced 
@File    ：coroutine_module_03.py
@Author  ：Toby
@Date    ：2022/11/28 14:34 
@Description：迭代器示例斐波那契数列
"""
"""
举个例子，比如，数学中有个著名的斐波拉契数列（Fibonacci），数列中第一个数为0，第二个数为1，其后的每一个数都可由前两个数相加得到：
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""


class FibIterator(object):
    """自定义的一个可迭代对象"""

    def __init__(self, nums):
        """
        :param nums: int, 指明生成数列的前n个数
        """
        self.nums = nums
        self.num1 = 0  # 每次的第一位数
        self.num2 = 1  # 每次的第二位数
        self.counter = 0  # 计数器

    def __next__(self):
        if self.counter < self.nums:
            data = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.counter += 1
            return data
        elif self.counter == 0 and self.nums == 0:
            data = self.nums
            self.counter += 1
            return data
        elif self.counter <= 1 and self.nums == 1:
            data = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.counter += 1
            return data
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    fb = FibIterator(3)
    for i in fb:
        print(i, end=",")

