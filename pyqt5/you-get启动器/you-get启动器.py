#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from  startwindow import Ui_StartWindow
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(Mainwindow)
    ui.setupFunction()
    Mainwindow.show()
    sys.exit(app.exec_())