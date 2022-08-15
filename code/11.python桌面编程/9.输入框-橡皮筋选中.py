# -*- coding: utf-8 -*-

"""
@author: Toby
@software: PyCharm
@file: 9.输入框-橡皮筋选中.py
@time: 2022/7/25 16:59
"""
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("橡皮筋选中")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        """
        设置内部控件
        """
        qrb = QRubberBand(self)
        qrb.move(150, 100)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
