# THIS FILE WILL HANDLE THE GUI AND WORK WITH THE SERVER
# TO INFORM THE USER ON ANY ACTIVITY

#import outside libraries 
import sys
<<<<<<< HEAD
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

#import inside scripts
from Spyware_Manager import detection
=======
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
>>>>>>> e632210294624364f29ffc6854071d33c3857c7c

#import inside scripts
from Spyware_Manager import detection

<<<<<<< HEAD
def show_res(output: QTextEdit):
    res = detection.ScanFile()
    text = "".join(str(i) for i in res if i != [])
=======

def show_res(output: QTextEdit):
    res = detection.ScanFile()
    text = ""
    for i in res:
        if i != []:
            text = text.join(str(i))
>>>>>>> e632210294624364f29ffc6854071d33c3857c7c
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
    
<<<<<<< HEAD
    button = QPushButton()
    button.setText("Scan")
    layout.addWidget(button)
    
    output = QLabel()
    output.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    output.setFont(QFont('Arial', 35))
    layout.addWidget(output)
    
    
    #buttons functions
    button.clicked.connect(lambda: show_res(output))
    
=======
    
    button = QPushButton()
    button.setText("Scan")
    layout.addWidget(button)
    
    output = QTextEdit()
    layout.addWidget(output)
    
    
    #buttons functions
    button.clicked.connect(lambda: show_res(output))
    
>>>>>>> e632210294624364f29ffc6854071d33c3857c7c
    
    win.show()
    
    sys.exit(app.exec())
if __name__ == "__main__":   
    window()