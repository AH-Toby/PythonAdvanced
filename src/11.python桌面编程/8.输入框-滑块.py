# -*- coding: utf-8 -*-

"""
@author: Toby
@software: PyCharm
@file: 8.输入框-滑块.py
@time: 2022/7/25 16:53
"""
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("滑块")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        """
        设置内部控件
        """
        qd = QDial(self)
        qd.move(150, 10)

        qs = QSlider(self)
        qs.move(150, 200)

        qsb = QScrollBar(self)
        qsb.move(150, 400)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
