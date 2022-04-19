# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'countrymk1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QLabel

class Ui_countryprog(object):
    def setupUi(self, countryprog):
        countryprog.setObjectName("countryprog")
        countryprog.resize(383, 484)
        countryprog.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(countryprog)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonqenter = QtWidgets.QPushButton(self.centralwidget)
        self.buttonqenter.setGeometry(QtCore.QRect(90, 300, 151, 81))
        self.buttonqenter.setObjectName("buttonqenter")
        
        self.welcomelabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomelabel.setGeometry(QtCore.QRect(30, 20, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.welcomelabel.setFont(font)
        self.welcomelabel.setObjectName("welcomelabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)#line edit
        self.lineEdit.setGeometry(QtCore.QRect(80, 190, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 110, 141, 20))
        self.label_2.setObjectName("label_2")
        countryprog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(countryprog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 383, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        countryprog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(countryprog)
        self.statusbar.setObjectName("statusbar")
        countryprog.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())


        self.retranslateUi(countryprog)
        QtCore.QMetaObject.connectSlotsByName(countryprog)
        self.buttonqenter.clicked.connect(self.show_popup)### connect button click popu
            

        
        
    def retranslateUi(self, countryprog):
        _translate = QtCore.QCoreApplication.translate
        countryprog.setWindowTitle(_translate("countryprog", "MainWindow"))
        self.buttonqenter.setText(_translate("countryprog", "Enterbutton"))
        self.welcomelabel.setText(_translate("countryprog", "Hello welcome to the country program "))
        self.label_2.setText(_translate("countryprog", "Enter country name:"))
        self.menufile.setTitle(_translate("countryprog", "file"))

    

    def show_popup(self):
        textValue=self.lineEdit.text()
        QMessageBox.question(self, "Line Edit", "You have typed"+ textValue, QMessageBox.Ok, QMessageBox.ok)
    


        #msg=QMessageBox()
       #msg.setWindowTitle("Popup window title: You have just clicked")
        #msg.setText("HEllo")

        #x=msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    countryprog = QtWidgets.QMainWindow()
    ui = Ui_countryprog()
    ui.setupUi(countryprog)
    countryprog.show()
    sys.exit(app.exec_())
