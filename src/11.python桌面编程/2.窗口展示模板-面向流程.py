# -*- coding: utf-8 -*-

"""
@author: Toby
@software: PyCharm
@file: 2.窗口展示模板-面向流程.py
@time: 2022/7/21 17:19
"""
import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("")
window.resize(500, 500)



window.show()

sys.exit(app.exec_())