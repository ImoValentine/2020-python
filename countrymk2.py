# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'countrymk2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton, QAction, QLineEdit, QApplication, QMainWindow##Import this library for pop up message box

class Ui_countryprog(object):
    def setupUi(self, countryprog):
        countryprog.setObjectName("countryprog")
        countryprog.resize(383, 484)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Pictures/Atom Icons - Download Free Vector Icons _ Noun Project_files/34971-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        countryprog.setWindowIcon(icon)
        countryprog.setAutoFillBackground(True)
        countryprog.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(countryprog)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonqenter = QtWidgets.QPushButton(self.centralwidget)#Button
        self.buttonqenter.setGeometry(QtCore.QRect(110, 300, 151, 81))#Button geometry
        self.buttonqenter.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.buttonqenter.setObjectName("buttonqenter")
        self.welcomelabel = QtWidgets.QLabel(self.centralwidget)#Welcome label
        self.welcomelabel.setGeometry(QtCore.QRect(30, 20, 321, 61))
        self.namelabel=QtWidgets.QLabel(self.centralwidget)#name label
        self.namelabel.setGeometry(QtCore.QRect(250, 25, 150, 850))## Geometry Of name label
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setUnderline(True)
        self.welcomelabel.setFont(font)
        self.welcomelabel.setObjectName("welcomelabel")
        self.counameans = QtWidgets.QLineEdit(self.centralwidget)#country name
        self.counameans.setGeometry(QtCore.QRect(90, 130, 181, 20))
        self.counameans.setObjectName("counameans")
        self.countryname = QtWidgets.QLabel(self.centralwidget)
        self.countryname.setGeometry(QtCore.QRect(120, 100, 141, 20))
        self.countryname.setObjectName("countryname")
        self.charanamean = QtWidgets.QLineEdit(self.centralwidget)#character name
        self.charanamean.setGeometry(QtCore.QRect(90, 230, 181, 20))
        self.charanamean.setObjectName("charanamean")
        self.charactesearch = QtWidgets.QLabel(self.centralwidget)
        self.charactesearch.setGeometry(QtCore.QRect(90, 190, 201, 21))
        self.charactesearch.setObjectName("charactesearch")
        countryprog.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(countryprog)
        self.statusbar.setObjectName("statusbar")
        countryprog.setStatusBar(self.statusbar)

        self.retranslateUi(countryprog)
        QtCore.QMetaObject.connectSlotsByName(countryprog)

        self.buttonqenter.clicked.connect(self.showpopup)###button click popup- connects to pop up to display


    def retranslateUi(self, countryprog):
        _translate = QtCore.QCoreApplication.translate
        countryprog.setWindowTitle(_translate("countryprog", "Country Character counter"))#button
        self.buttonqenter.setText(_translate("countryprog", "Enter button"))
        self.welcomelabel.setText(_translate("countryprog", "Greetings user welcome to the country program "))#label
        self.countryname.setText(_translate("countryprog", "Enter country name:"))#label
        self.charactesearch.setText(_translate("countryprog", "Enter character for search: e.g. A-Z"))#label
        self.namelabel.setText(_translate("countryprog", "Imraan Jacobs 11641584"))

    
    def showpopup(self): ###pop up window for result
        textBoxValue1=self.counameans.text()##storing line edit in string variable
        textBoxValue2=self.charanamean.text()##storing character inpur as string variable
        lowt1=textBoxValue1.lower()
        lowt2=textBoxValue2.lower()
        disp_count_char=lowt1.count(lowt2)
        
        QMessageBox.question(self.centralwidget, "message", "Your country name is: \n" +textBoxValue1+ "\n" + "\n Your character is: "+textBoxValue2+ " \n \n Occurs: "+ str(disp_count_char)+ " times(Upper and Lower case included)", QMessageBox.Ok, QMessageBox.Ok)
      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    countryprog = QtWidgets.QMainWindow()
    ui = Ui_countryprog()
    ui.setupUi(countryprog)
    countryprog.show()
    sys.exit(app.exec_())
