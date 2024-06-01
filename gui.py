# THIS FILE WILL HANDLE THE GUI
import sys,os
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

#import the scrypt manager
from Spyware_Manager import Manager


#get stylesheet
def load_stylesheet(path):
    with open(path, "r") as file:
        return file.read()


#set up the side navigation bar
def sidebar(window: QWidget):

    # Sidebar widget
    sidebar = QWidget(parent=window)
    sidebar.setObjectName("sidebar")
    sidebar.setFixedWidth(140)
    sidebar.setFixedHeight(540)

    # Sidebar logo
    logo_label = QLabel("      SMR", parent=sidebar)
    logo_label.setObjectName("sidebar")
    logo_label.setGeometry(0,0,140,50)

    # Sidebar menu items
    items = ["home", "scans", "history", "settings"]
    i = 50
    for item in items:
        item_button = QPushButton(item, objectName='sidebar',parent=sidebar)
        item_button.setGeometry(0,i,140,50)
        i += 50


        



#set up the gui
def main():
    app = QApplication(sys.argv)


    #load stylesheet
    style_path = f'{os.path.dirname(os.path.abspath(__file__))}\\Design\style.qss'
    app.setStyleSheet(load_stylesheet(style_path))

    win = QWidget()
    win.setWindowTitle("SpywareDetection")
    win.setFixedSize(960,540)
    
    layout = QVBoxLayout()
    win.setLayout(layout)

    
    output = QLabel()
    output.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    output.setFont(QFont('Arial', 35))
    output.setStyleSheet('color: black')
    layout.addWidget(output)
    

    #add sidebar
    sidebar(win)
    
    
    #buttons functions
    
    

    #open and close the window
    win.show()
    sys.exit(app.exec())
    

    
if __name__ == "__main__":
    main()
    