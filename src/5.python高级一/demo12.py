# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-


class Goods(object):
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, '价格属性描述。。。。')


obj = Goods()
original_price = obj.PRICE  # 获取商品价格
print(original_price)
obj.PRICE = 200  # 修改商品原价
desc = obj.PRICE.__doc__
print(desc)
del obj.PRICE  # 删除商品原价
