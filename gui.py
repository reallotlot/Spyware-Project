# THIS FILE WILL HANDLE THE GUI
import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

#import the scrypt manager
from Spyware_Manager import Manager

#set up the side navigation bar
def side_bar(window: QWidget):
    background = QLabel(window)
    background.setGeometry(0,0,100,540)
    background.setStyleSheet('hello')

#set up the gui
def main():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("SpywareDetection")
    win.setFixedSize(960,540)
    win.setStyleSheet("background-color: #f5f5dc")
    
    layout = QVBoxLayout()
    win.setLayout(layout)

    ico = QIcon("Design\\logo.png")
    win.setWindowIcon(ico)
    
    button = QPushButton()
    button.setText("Scan")
    layout.addWidget(button)
    
    output = QLabel()
    output.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    output.setFont(QFont('Arial', 35))
    layout.addWidget(output)
    

    #add sidebar
    side_bar(win)
    
    
    #buttons functions
    button.clicked.connect(lambda: show_res(output))
    
    
    win.show()
    
    sys.exit(app.exec())
    
    
def show_res(output: QTextEdit):
    res = Manager.Analysis(r'\malware').run_analysis()
    output.setText(res + '\n')
    
if __name__ == "__main__":
    main()
    