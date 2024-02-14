# THIS FILE WILL HANDLE THE GUI AND WORK WITH THE SERVER
# TO INFORM THE USER ON ANY ACTIVITY

import sys
from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon


def change(button: QPushButton):
    button.setText("changed!")


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("SpywareDetection")
    win.setFixedSize(960,540)
    
    ico = QIcon("Design\\logo.png")
    win.setWindowIcon(ico)
    
    button = QPushButton(win)
    button.setText("CHANGE TEXT!!!")
    button.setGeometry(350,200,100,50)
    
    button.clicked.connect(lambda: change(button))
    
    win.show()
    
    sys.exit(app.exec())
if __name__ == "__main__":   
    window()