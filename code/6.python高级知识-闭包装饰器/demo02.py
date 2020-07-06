# -*- coding:utf-8 -*-
# 第一种方法
# 每次都更具汇率和钱都写一遍
# 这种方法是太烦了
print("第一种方法")
rate_usa = 0.7
money = 100
# print(rate_usa * money)
print("第一种方法结束")

# 第二种方法封装成函数
# 这种方法还是太烦
print("第二种方法")


def count_rate(rate, money):
    print(rate * money)


count_rate(100, 1000)
print("第二种方法结束")

# 第三种方法用缺省参数来代替汇率的输入
# 这种方法还是太烦
print("第三种方法")


def count_rate(money, rate=0.7):
    print(money * rate)


count_rate(100)
count_rate(100, 1000)
print("第三种方法结束")

# 第四种方法用全局变量来代替汇率的输入
# 这种方法还是太烦
print("第四种方法")
rate = 100


def count_rate(money):
    print(money * rate)


count_rate(100)
print("第四种方法结束")

# 第五种方法分装成类
# 这种方法魔法方法 太多还是太烦
print("第五种方法")


class CountRate(object):
    def __init__(self, rate):
        self.rate = rate

    def __call__(self, money):
        print(self.rate * money)


usa = CountRate(0.7)
usa(200)
rate_jp = CountRate(1000)
rate_jp(1000)

print("第五种方法结束")

# 第六种方法：闭包解决
print("第六种方法")


def count(rate):
    def money(money):
        print(rate * money)

    return money


usa_rate = count(0.7)
usa_rate(100)
print("第六种方法结束")
