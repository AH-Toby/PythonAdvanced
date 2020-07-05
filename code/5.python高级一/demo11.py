# -*- coding:utf-8 -*-


# coding=utf-8
class Foo(object):
    def get_bar(self):
        print("getter...")
        return 'laowang'

    def set_bar(self, value):
        """必须两个参数"""
        print("setter...")
        return 'set value' + value

    def del_bar(self):
        print("deleter...")
        return 'laowang'

    BAR = property(get_bar, set_bar, del_bar, "description...")


obj = Foo()

bar = obj.BAR  # 自动调用第一个参数中定义的方法：get_bar
print(bar)

obj.BAR = "alex"  # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入

desc = Foo.BAR.__doc__  # 自动获取第四个参数中设置的值：description...
print(desc)

del obj.BAR  # 自动调用第三个参数中定义的方法：del_bar方法
