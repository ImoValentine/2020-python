


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton, QAction, QLineEdit, QApplication, QMainWindow##Import this libr


class Ui_country(object):
    def setupUi(self, country):
        country.setObjectName("country")
        country.resize(260, 299)
        country.setToolTipDuration(7)
        country.setAutoFillBackground(True)
        country.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(country)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(70, 180, 71, 31))
        self.button1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button1.setObjectName("button1")
        self.welcomelabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomelabel.setGeometry(QtCore.QRect(30, 20, 321, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setUnderline(True)
        self.welcomelabel.setFont(font)
        self.welcomelabel.setObjectName("welcomelabel")
        self.namelabel=QtWidgets.QLabel(self.centralwidget)#name label
        self.namelabel.setGeometry(QtCore.QRect(130, 25, 150, 450))## Geometry Of name label
        self.countryedi = QtWidgets.QLineEdit(self.centralwidget)
        self.countryedi.setGeometry(QtCore.QRect(150, 80, 51, 21))
        self.countryedi.setObjectName("countryedi")
        self.country_name1 = QtWidgets.QLabel(self.centralwidget)
        self.country_name1.setGeometry(QtCore.QRect(30, 80, 141, 20))
        self.country_name1.setObjectName("country_name1")
        self.character_sele = QtWidgets.QLineEdit(self.centralwidget)
        self.character_sele.setGeometry(QtCore.QRect(140, 130, 51, 20))
        self.character_sele.setObjectName("character_sele")
        self.charactesearch = QtWidgets.QLabel(self.centralwidget)
        self.charactesearch.setGeometry(QtCore.QRect(30, 130, 201, 21))
        self.charactesearch.setObjectName("charactesearch")
        country.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(country)
        self.statusbar.setObjectName("statusbar")
        country.setStatusBar(self.statusbar)

        self.retranslateUi(country)
        QtCore.QMetaObject.connectSlotsByName(country)

        self.button1.clicked.connect(self.showpopup)###button click popup- connects to pop up to display


    def retranslateUi(self, country):
        _translate = QtCore.QCoreApplication.translate
        country.setWindowTitle(_translate("country", "Country Character counter"))
        self.button1.setText(_translate("country", "Enter"))
        self.welcomelabel.setText(_translate("country", "Country App "))
        self.country_name1.setText(_translate("country", "Enter country name:"))
        self.charactesearch.setText(_translate("country", "Enter character:"))
        self.namelabel.setText(_translate("country", "Obssaa Danbobo 11481730"))

     
    def showpopup(self): ###pop up window for result
        textBoxValue1=self.countryedi.text()##storing line edit in string variable
        textBoxValue2=self.character_sele.text()##storing character inpur as string variable
        lowt1=textBoxValue1.lower()
        lowt2=textBoxValue2.lower()
        disp_count_char=lowt1.count(lowt2)
        
        QMessageBox.question(self.centralwidget, "message", "The country name is: \n" +textBoxValue1+ "\n" + "\n Character : "+textBoxValue2+ " \n \n Occurs: "+ str(disp_count_char)+ " times", QMessageBox.Ok, QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    country = QtWidgets.QMainWindow()
    ui = Ui_country()
    ui.setupUi(country)
    country.show()
    sys.exit(app.exec_())
