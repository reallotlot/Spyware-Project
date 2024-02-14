# THIS FILE WILL HANDLE THE GUI AND WORK WITH THE SERVER
# TO INFORM THE USER ON ANY ACTIVITY

import sys
from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setGeometry(0, 0, 960, 540)
    win.setWindowTitle("SpywareDetection")
    
    ico = QIcon("Design\\logo.png")
    win.setWindowIcon(ico)
    
    
    win.show()
    
    sys.exit(app.exec())
if __name__ == "__main__":   
    window()