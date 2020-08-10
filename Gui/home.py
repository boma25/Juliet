# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from convo import Ui_conversation
from main import *


class Ui_MainWindow(object):
    def next(self):
        self.win = QtWidgets.QMainWindow()
        self.Ui = Ui_conversation()
        self.Ui.setupUi(self.win)
        MainWindow.close()
        self.win.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 467)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/juliet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:#730013")
        MainWindow.setAutoFillBackground(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(20, 50, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Geometr415 Blk BT")
        font.setBold(True)
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setStyleSheet("color: #8cffec")
        self.name.setObjectName("name")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(5, 82, 191, 121))
        self.label.setObjectName("label")
        pixmap = QtGui.QPixmap("../assets/juliet home.png")
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())

        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(90, 400, 91, 41))
        self.commandLinkButton.setObjectName("Next")
        self.commandLinkButton.setStyleSheet("color: #8cffec")
        self.commandLinkButton.clicked.connect(self.next)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Juliet"))
        self.name.setText(_translate("MainWindow", "Hi i am Juliet Your Virtual Assistant"))
        self.commandLinkButton.setText(_translate("MainWindow", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    response("hi, i am juliet, your virtual assistant")
    response("click next to continue")
    sys.exit(app.exec_())
