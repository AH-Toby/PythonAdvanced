# -*- coding: utf-8 -*-

"""
@author: Toby
@software: PyCharm
@file: 3.窗口展示模板-面向对象.py
@time: 2022/7/21 17:28
"""
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        """
        设置内部控件
        """
        
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())