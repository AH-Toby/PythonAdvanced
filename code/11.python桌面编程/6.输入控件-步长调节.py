# -*- coding: utf-8 -*-

"""
@author: Toby
@software: PyCharm
@file: 6.输入控件-步长调节.py
@time: 2022/7/22 18:26
"""
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("输入控件-步长调节")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        """
        设置内部控件
        """
        qasb = QAbstractSpinBox(self)
        qasb.resize(100, 20)
        qasb.move(150, 50)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())