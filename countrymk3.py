# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'countrymk3.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_countryprog(object):
    def setupUi(self, countryprog):
        countryprog.setObjectName("countryprog")
        countryprog.resize(260, 299)
        countryprog.setToolTipDuration(7)
        countryprog.setAutoFillBackground(True)
        countryprog.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(countryprog)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonqenter = QtWidgets.QPushButton(self.centralwidget)
        self.buttonqenter.setGeometry(QtCore.QRect(70, 180, 71, 31))
        self.buttonqenter.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.buttonqenter.setObjectName("buttonqenter")
        self.welcomelabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomelabel.setGeometry(QtCore.QRect(30, 20, 321, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setUnderline(True)
        self.welcomelabel.setFont(font)
        self.welcomelabel.setObjectName("welcomelabel")
        self.counameans = QtWidgets.QLineEdit(self.centralwidget)
        self.counameans.setGeometry(QtCore.QRect(150, 80, 51, 21))
        self.counameans.setObjectName("counameans")
        self.countryname = QtWidgets.QLabel(self.centralwidget)
        self.countryname.setGeometry(QtCore.QRect(30, 80, 141, 20))
        self.countryname.setObjectName("countryname")
        self.charanamean = QtWidgets.QLineEdit(self.centralwidget)
        self.charanamean.setGeometry(QtCore.QRect(140, 130, 51, 20))
        self.charanamean.setObjectName("charanamean")
        self.charactesearch = QtWidgets.QLabel(self.centralwidget)
        self.charactesearch.setGeometry(QtCore.QRect(30, 130, 201, 21))
        self.charactesearch.setObjectName("charactesearch")
        countryprog.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(countryprog)
        self.statusbar.setObjectName("statusbar")
        countryprog.setStatusBar(self.statusbar)

        self.retranslateUi(countryprog)
        QtCore.QMetaObject.connectSlotsByName(countryprog)

    def retranslateUi(self, countryprog):
        _translate = QtCore.QCoreApplication.translate
        countryprog.setWindowTitle(_translate("countryprog", "Country Character counter"))
        self.buttonqenter.setText(_translate("countryprog", "Enter"))
        self.welcomelabel.setText(_translate("countryprog", "Country App "))
        self.countryname.setText(_translate("countryprog", "Enter country name:"))
        self.charactesearch.setText(_translate("countryprog", "Enter character:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    countryprog = QtWidgets.QMainWindow()
    ui = Ui_countryprog()
    ui.setupUi(countryprog)
    countryprog.show()
    sys.exit(app.exec_())
