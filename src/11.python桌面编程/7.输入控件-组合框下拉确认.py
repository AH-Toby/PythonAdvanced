# -*- coding: utf-8 -*-

"""
@author: Toby
@software: PyCharm
@file: 7.输入控件-组合框下拉确认.py
@time: 2022/7/25 9:59
"""
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("组合框下拉确认")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        """
        设置内部控件
        """
        qcb = QComboBox(self)
        qcb.move(150, 150)

        qfc = QFontComboBox(self)
        qfc.move(150, 350)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
