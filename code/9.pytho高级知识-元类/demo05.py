# -*- coding:utf-8 -*-
def test(class_name, supers_name, attrs):
    print(attrs)

    # attrs.pop("num")  # 删除一个属性
    attrs['num'] = 0
    return type(class_name, supers_name, attrs)


# python2下用的
class AA(object):
    # 告诉系统我自己创建类
    __metaclass__ = test
    num = 100


aa = AA()
print(AA.num)
