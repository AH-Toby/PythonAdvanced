# -*- coding: utf-8 -*-

"""
@author: Toby
@software: PyCharm
@file: 4.按钮控件.py
@time: 2022/7/22 11:25
"""
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("按钮种类")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        """
        设置内部控件
        """
        btn1 = QPushButton(self)
        btn1.setText("QPushButton样式，可双击可点击")
        btn1.move(150, 100)

        btn2 = QCommandLinkButton(self)
        btn2.setText("QCommandLinkButton样式")
        btn2.move(150, 200)

        btn3 = QRadioButton(self)
        btn3.setText("QRadioButton样式")
        btn3.move(150, 300)

        btn4 = QCheckBox(self)
        btn4.setText("QCheckBox样式")
        btn4.move(150, 400)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
