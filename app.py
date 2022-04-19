# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_goodone(object):
    def setupUi(self, goodone):
        goodone.setObjectName("goodone")
        goodone.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(goodone)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 60, 261, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(63, 30, 261, 21))
        self.textEdit.setObjectName("textEdit")
        self.yes = QtWidgets.QPushButton(self.centralwidget)
        self.yes.setGeometry(QtCore.QRect(64, 142, 131, 41))
        self.yes.setObjectName("yes")
        goodone.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(goodone)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        goodone.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(goodone)
        self.statusbar.setObjectName("statusbar")
        goodone.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(goodone)
        QtCore.QMetaObject.connectSlotsByName(goodone)

    def retranslateUi(self, goodone):
        _translate = QtCore.QCoreApplication.translate
        goodone.setWindowTitle(_translate("goodone", "MainWindow"))
        self.textEdit.setHtml(_translate("goodone", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; text-decoration: underline;\">What is your name?</span></p></body></html>"))
        self.yes.setText(_translate("goodone", "YES!"))
        self.menufile.setTitle(_translate("goodone", "file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    goodone = QtWidgets.QMainWindow()
    ui = Ui_goodone()
    ui.setupUi(goodone)
    goodone.show()
    sys.exit(app.exec_())
