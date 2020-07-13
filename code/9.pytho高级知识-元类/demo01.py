# -*- coding:utf-8 -*-
class CC(object):
    num = 100

    def test(self):
        print("test is show")


cc = CC()
cc.test()

xx = CC
bb = xx()
bb.test()


print(cc.__class__)
print(cc.__class__.__class__)
print(cc.__class__.__class__.__class__)

print(int.__class__)
