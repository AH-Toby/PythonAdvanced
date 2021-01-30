# -*- coding:utf-8 -*-
# send方法使用
def my_generator(n):
    for i in range(n):
        temp = yield  # 不返回值这时候无法迭代值，每次都是None
        print(f"我是{temp}")


g = my_generator(5)
print(next(g))  # 输出None,到yield停止抛出
# None

print("=" * 30)
print(next(g))  # 继续运行yield之后。此时temp还未被赋值所以是None,继续下次循环所以输出None
# 我是None
# None

print("*" * 30)
g.send(100)  # 继续yield之后的操作此时为，本来输出的2.但是传入了新值100，所以yield表达式为100也就是说temp为100
# 我是100

print("-" * 30)
print(next(g))
# 我是None
# None

print("+" * 30)
print(next(g))
# 我是None
# None
