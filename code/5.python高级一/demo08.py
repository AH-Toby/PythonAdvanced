# -*- coding:utf-8 -*-
# ############### 定义 ###############
class Pager:
    """
    旧式类
    """
    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val


# ############### 调用 ###############
p = Pager(1)
print(p.start)  # 就是起始值，即：m
print(p.end)  # 就是结束值，即：n
