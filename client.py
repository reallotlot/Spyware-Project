# THIS FILE WILL HANDLE THE GUI AND WORK WITH THE SERVER
# TO INFORM THE USER ON ANY ACTIVITY

#import outside libraries 
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon

#import inside scripts
from Spyware_Manager import detection


def show_res(output: QTextEdit):
    res = detection.ScanFile()
    text = ""
    for i in res:
        if i != []:
            text = text.join(str(i))
    output.setText(text)

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("SpywareDetection")
    win.setFixedSize(960,540)
    
    layout = QVBoxLayout()
    win.setLayout(layout)

    ico = QIcon("Design\\logo.png")
    win.setWindowIcon(ico)
    
    
    button = QPushButton()
    button.setText("Scan")
    layout.addWidget(button)
    
    output = QTextEdit()
    layout.addWidget(output)
    
    
    #buttons functions
    button.clicked.connect(lambda: show_res(output))
    
    
    win.show()
    
    sys.exit(app.exec())
if __name__ == "__main__":   
    window()