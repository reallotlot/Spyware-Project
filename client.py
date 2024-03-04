# THIS FILE WILL HANDLE THE GUI AND WORK WITH THE SERVER
# TO INFORM THE USER ON ANY ACTIVITY

#import outside libraries 
import sys, socket
import time
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


#set up the socket connection
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5555

ADDR = (HOST, PORT)


#set up the gui
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
    
    output = QLabel()
    output.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    output.setFont(QFont('Arial', 35))
    layout.addWidget(output)
    
    
    #buttons functions
    button.clicked.connect(lambda: show_res(output))
    
    
    win.show()
    
    sys.exit(app.exec())
    
    
def show_res(output: QTextEdit):
    client.send(bytes.fromhex("7363616E"))
    res = None
    while res is None:
        time.sleep(0.05)
        res = client.recv(2048).decode()
        
    output.setText(output.text() + res + "\n")
    

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(ADDR)
except:
    print("problem")
    
window()
    