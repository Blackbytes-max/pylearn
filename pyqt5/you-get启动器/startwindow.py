# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from multiprocessing import Process, Pool, cpu_count

import psutil
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(800, 320)
        StartWindow.setMaximumSize(QtCore.QSize(800, 320))
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cookies_path_selector = QtWidgets.QPushButton(self.centralwidget)
        self.cookies_path_selector.setGeometry(QtCore.QRect(740, 168, 25, 20))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cookies_path_selector.setFont(font)
        self.cookies_path_selector.setObjectName("cookies_path_selector")
        self.filesave_path_selector = QtWidgets.QPushButton(self.centralwidget)
        self.filesave_path_selector.setGeometry(QtCore.QRect(740, 228, 25, 20))
        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.filesave_path_selector.setFont(font)
        self.filesave_path_selector.setObjectName("filesave_path_selector")
        self.lineEdit_filesave_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filesave_path.setGeometry(QtCore.QRect(20, 228, 720, 20))
        self.lineEdit_filesave_path.setMaximumSize(QtCore.QSize(720, 16777215))
        self.lineEdit_filesave_path.setObjectName("lineEdit_filesave_path")
        self.lineEdit_filesave_path.setText(os.environ["HOMEDRIVE"] + os.environ["HOMEPATH"] + "\Videos")  # 预设值保存路径
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 72, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.lineEdit_links = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_links.setEnabled(True)
        self.lineEdit_links.setGeometry(QtCore.QRect(20, 60, 720, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_links.sizePolicy().hasHeightForWidth())
        self.lineEdit_links.setSizePolicy(sizePolicy)
        self.lineEdit_links.setMaximumSize(QtCore.QSize(720, 16777215))
        self.lineEdit_links.setObjectName("lineEdit_links")
        self.lineEdit_cookies_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cookies_path.setGeometry(QtCore.QRect(20, 168, 720, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_cookies_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_cookies_path.setSizePolicy(sizePolicy)
        self.lineEdit_cookies_path.setMaximumSize(QtCore.QSize(720, 16777215))
        self.lineEdit_cookies_path.setObjectName("lineEdit_cookies_path")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 72, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 151, 102, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.lineEdit_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filename.setGeometry(QtCore.QRect(20, 120, 720, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_filename.sizePolicy().hasHeightForWidth())
        self.lineEdit_filename.setSizePolicy(sizePolicy)
        self.lineEdit_filename.setMaximumSize(QtCore.QSize(720, 16777215))
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 198, 72, 16))
        self.label_4.setObjectName("label_4")
        self.Cancel_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel_Button.setGeometry(QtCore.QRect(630, 270, 75, 23))
        self.Cancel_Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.Start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Button.setGeometry(QtCore.QRect(520, 270, 75, 23))
        self.Start_Button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Start_Button.setObjectName("Start_Button")
        self.err_info_label = QtWidgets.QLabel(self.centralwidget)
        self.err_info_label.setGeometry(QtCore.QRect(20, 270, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.err_info_label.setFont(font)
        self.err_info_label.setText("")
        self.err_info_label.setObjectName("err_info_label")
        self.quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button.setGeometry(QtCore.QRect(410, 270, 75, 23))
        self.quit_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.quit_button.setObjectName("quit_button")

        StartWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StartWindow)
        self.statusbar.setObjectName("statusbar")
        StartWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "You-get 快捷启动器"))
        self.cookies_path_selector.setText(_translate("StartWindow", "..."))
        self.filesave_path_selector.setText(_translate("StartWindow", "..."))
        self.label.setText(_translate("StartWindow", "参数和链接："))
        self.label_2.setText(_translate("StartWindow", "输出文件名："))
        self.label_3.setText(_translate("StartWindow", "cookies文件路径："))
        self.label_4.setText(_translate("StartWindow", "文件保存到："))
        self.Cancel_Button.setText(_translate("StartWindow", "取消"))
        self.Start_Button.setText(_translate("StartWindow", "启动"))
        self.quit_button.setText(_translate("StartWindow", "强制退出"))

    def setupFunction(self):
        self.cookies_path_selector.clicked.connect(self.setup_cookie_file_path)
        self.filesave_path_selector.clicked.connect(self.setup_filesave_path)
        self.Start_Button.clicked.connect(self.start_task)
        self.Cancel_Button.clicked.connect(self.cancel_task)
        self.quit_button.clicked.connect(self.quit_App)

        self.pid_list = [None]
        self.p = Pool(cpu_count())  # 创建进程池
        self.commed_links_history = []  # 记录历史命令行参数

    def setup_cookie_file_path(self):
        self.f_get = QtWidgets.QFileDialog()
        f_s, _ = self.f_get.getOpenFileName(None, "请选择文件", '/', 'Text files (*.txt)')  # 此处若将self指定为父组件，会出现TypeError
        if f_s:
            self.lineEdit_cookies_path.setText(f_s)

    def setup_filesave_path(self):
        self.dir_get = QtWidgets.QFileDialog()
        dir_s = self.dir_get.getExistingDirectory(None, '请选择文件夹', '/')
        if dir_s:
            self.lineEdit_filesave_path.setText(dir_s)

    def start_task(self):
        commend = ""
        commend_links = ""
        commend_filename = ""
        commend_dir = ""
        commend_cookies = ""
        if not self.lineEdit_links.text():
            self.err("参数或链接不能为空！")
        else:
            commend_links = self.lineEdit_links.text()
            if not os.access(self.lineEdit_filesave_path.text(), os.F_OK | os.R_OK | os.W_OK):
                self.err('无效的路径或目录不可写！')
            else:
                commend_dir = " --output-dir " + self.lineEdit_filesave_path.text()

                if not os.access(self.lineEdit_cookies_path.text(), os.F_OK | os.R_OK):
                    pass
                else:
                    commend_cookies = " --cookies " + self.lineEdit_cookies_path.text()
                if not self.lineEdit_filename.text():
                    pass
                else:
                    commend_filename = " -O " + self.lineEdit_filename.text()
                commend = "you-get  " + commend_links + commend_cookies + commend_dir + commend_filename
                if (commend_links in self.commed_links_history):  # 检查下载链接是否重复
                    self.err('重复的下载链接！')
                else:
                    self.p.apply_async(s_commend, args=(commend,))  # 异步创建子进程
                    self.commed_links_history.append(commend_links)

    def cancel_task(self):
        self.pid_list = pid_list_update(self.pid_list)
        if (len(self.pid_list)) == 0:
            QtWidgets.QApplication.exit()  # 退出
        else:
            sr = '还有' + str(len(self.pid_list)) + '个任务未完成'
            self.err(sr)

    def quit_App(self):
        self.p.close()  # 关闭进程池
        self.p.terminate()  # 关闭所有进程
        QtWidgets.QApplication.exit()  # 退出

    def err(self, err_info):
        self.err_info_label.setText(err_info)


def pid_checker(pid):
    if pid in psutil.pids():
        return True
    else:
        return False


def pid_list_update(li):
    return list(filter(pid_checker, li))


def s_commend(c):
    pid_list.append(os.getpid())
    os.system(c)
