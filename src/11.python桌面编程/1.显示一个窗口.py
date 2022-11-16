# -*- coding: utf-8 -*-

"""
@author: Toby
@software: PyCharm
@file: 1.显示一个窗口.py
@time: 2022/5/26 13:42
"""
import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("")
window.resize(500, 500)


window.show()

sys.exit(app.exec_())