# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conversation.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Settings import Ui_MainWindow
from main import *

class Ui_conversation(object):
    def settingswindow(self):
        self.win = QtWidgets.QMainWindow()
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self.win)
        self.win.show()

    def changetext(self):
        try:
            requests.get("https://www.google.com")
            _translate = QtCore.QCoreApplication.translate
            currenttext = self.pushButton_2.text()
            text = "Listening.."
            if text != currenttext:
                self.pushButton_2.setText(_translate("conversation", text))
                val = listen_to_me()
                self.label_2.setText(_translate("conversation", val))
                self.pushButton_2.setText(_translate("conversation", "Tap to speak"))
                command(val)
        except :
            response("you are offline, connect to the internet if you want to use your voice, or make use of the input field.")
        

    def send(self):
        text = self.lineEdit.text()
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.clear()
        self.label_2.setText(_translate("conversation", text))
        command(text)

    def setupUi(self, conversation):
        conversation.setObjectName("conversation")
        conversation.resize(305, 467)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/juliet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        conversation.setWindowIcon(icon)
        conversation.setStyleSheet("background-color:#730013;")
        self.centralwidget = QtWidgets.QWidget(conversation)
        self.centralwidget.setObjectName("centralwidget")

        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(210, 10, 75, 23))
        self.settings.setObjectName("Settingswindow")
        font = QtGui.QFont()
        font.setFamily("Geometr415 Blk BT")
        font.setBold(True)
        font.setPointSize(11)
        self.settings.setFont(font)
        self.settings.setStyleSheet("color: #8cffec")
        self.settings.clicked.connect(self.settingswindow)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 300, 20))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Geometr415 Blk BT")
        font.setBold(True)
        font.setPointSize(11)
        self.label.setStyleSheet("color: #8cffec")
        self.label.setFont(font)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 410, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setFamily("Geometr415 Blk BT")
        font.setBold(True)
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 410, 41, 23))
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setFamily("Geometr415 Blk BT")
        font.setBold(True)
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: #8cffec")
        self.pushButton.clicked.connect(self.send)


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(2, 90, 300, 50))
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()
        font.setFamily("Geometr415 Blk BT")
        font.setBold(True)
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setStyleSheet("background-color: white;" "border-radius:10px;")




        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 250, 110, 110))
        self.pushButton_2.setObjectName("speak")
        font = QtGui.QFont()
        font.setFamily("Geometr415 Blk BT")
        font.setBold(True)
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: white;" "border-radius:55px;")
        self.pushButton_2.pressed.connect(self.changetext)

        conversation.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(conversation)
        self.statusbar.setObjectName("statusbar")
        conversation.setStatusBar(self.statusbar)

        self.retranslateUi(conversation)
        QtCore.QMetaObject.connectSlotsByName(conversation)

    def retranslateUi(self, conversation):
        _translate = QtCore.QCoreApplication.translate
        conversation.setWindowTitle(_translate("conversation", "Juliet"))
        self.label.setText(_translate("conversation", "TALK TO ME!"))
        self.pushButton.setText(_translate("conversation", "Send"))
        self.settings.setText(_translate("conversation", "Settings"))
        self.pushButton_2.setText(_translate("conversation", "Tap to speak"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    conversation = QtWidgets.QMainWindow()
    ui = Ui_conversation()
    ui.setupUi(conversation)
    conversation.show()
    sys.exit(app.exec_())
