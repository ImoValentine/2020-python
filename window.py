from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QPushButton, QLineEdit
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Window"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()
 
 
    def InitWindow(self):
        
        self.LineEdit1=QLineEdit(self)
        self.LineEdit1.move(100,100)
        self.LineEdit1.resize(280, 40)

        self.LineEdit2=QLineEdit(self)
        self.LineEdit2.move(150,150)
        

        self.button=QPushButton("Show Text", self)
        self.button.move(270,250)
        self.button.clicked.connect(self.showpop)

        
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
 
    def showpop(self):
        textValue= self.LineEdit1.text()#storing of text
        charval=self.LineEdit2.text()#storing of character
        dispcount=textValue.count(charval)
        
        QMessageBox.question(self, "Line Edit", "Your country name is: "+ textValue+ "\n And your chosen character is "+ charval + "\n The character appears "+ str(dispcount) +" times", QMessageBox.Ok, QMessageBox.Ok)
     
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
