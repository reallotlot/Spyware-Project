# THIS FILE WILL HANDLE THE GUI
import sys,os
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

#import the scrypt manager
from Spyware_Manager import manager


#get stylesheet
def load_stylesheet(path):
    with open(path, "r") as file:
        return file.read()


class MainWindow(QMainWindow):
    #setup the main window
    def __init__(self):
        super().__init__()
        
        # Set up main window
        self.setWindowTitle("Main Window")
        self.setMinimumSize(960, 540)
        
        # Set maximum window size to 80% of screen size
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        self.setMaximumSize(int(screen.width() * 0.8), int(screen.height() * 0.8))
        
        # Create container widget for sidebar and main content
        container_widget = QWidget()
        self.setCentralWidget(container_widget)
        
        # Create main layout for container widget
        container_layout = QGridLayout(container_widget)
        # Set column stretch to ensure the sidebar remains at 20% width
        container_layout.setColumnStretch(0, 1)
        container_layout.setColumnStretch(1, 4)
        
        # Add sidebar
        self.add_sidebar(container_layout)
        
        # Apply style sheet
        self.setStyleSheet(load_stylesheet(f'{os.path.dirname(os.path.abspath(__file__))}\\Design\style.qss'))

        



    def add_sidebar(self, container_layout):
         # Create sidebar widget
        self.sidebar = QWidget()
        self.sidebar.setObjectName("sidebar")  # Set object name for styling
        sidebar_layout = QGridLayout(self.sidebar)
        
        # Sidebar content
        sidebar_layout.addWidget(QLabel("Sidebar"), 0, 0)
        sidebar_layout.addWidget(QPushButton("SCANS"), 1, 0)
        sidebar_layout.addWidget(QPushButton("HISTORY"), 2, 0)
        
        # Set fixed size for sidebar
        self.sidebar.setFixedWidth(int(self.width() * 0.2))
        
        # Set the grid formation
        sidebar_layout.setRowStretch(0, 1)
        sidebar_layout.setRowStretch(1, 1)
        sidebar_layout.setRowStretch(2, 1)
        sidebar_layout.setRowStretch(3, 7)
        
        # Add sidebar to container layout
        container_layout.addWidget(self.sidebar, 0, 0)
        
        
        
        
        
def start():
    
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    start()
    