# -*- coding: utf-8 -*-

"""
@author: Toby
@software: PyCharm
@file: 5.输入控件-纯键盘输入.py
@time: 2022/7/22 17:35
"""
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("输入控件-纯键盘输入")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        """
        设置内部控件
        """
        inp1 = QLineEdit(self)
        inp1.setText("输入框")
        inp1.move(150, 50)

        inp2 = QTextEdit(self)
        inp2.setText("多行文本输入框")


        inp2.resize(180, 90)
        inp2.move(150, 100)

        inp3 = QPlainTextEdit(self)
        inp3.resize(180, 90)
        inp3.move(150, 200)

        inp4 = QKeySequenceEdit(self)
        inp4.move(150, 400)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
