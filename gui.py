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

        
        # Load the pages
        self.scans = self.make_scans()
        self.history = self.make_history()

         # Add pages to container layout
        container_layout.addWidget(self.scans, 0, 1)
        container_layout.addWidget(self.history, 0, 1)
        
        # Hide page 2 initially
        self.history.hide()
        
        # Connect button signals to page switching function
        self.sidebar_buttons[0].clicked.connect(self.show_scans)
        self.sidebar_buttons[1].clicked.connect(self.show_history)



    def add_sidebar(self, container_layout):
         # Create sidebar widget
        self.sidebar = QWidget()
        self.sidebar.setObjectName("sidebar")  # Set object name for styling
        sidebar_layout = QGridLayout(self.sidebar)
        
        # Sidebar content
        i = 0
        sidebar_layout.addWidget(QLabel("MalwareLab"), i, 0)
        
        self.sidebar_buttons = []
        for name in ["SCANS", 'HISTORY']:
            i += 1
            button = QPushButton(name)
            sidebar_layout.addWidget(button, i, 0)
            self.sidebar_buttons.append(button)
            
        
        # Set fixed size for sidebar
        self.sidebar.setFixedWidth(int(self.width() * 0.2))
        
        # Set the grid formation
        sidebar_layout.setRowStretch(0, 1)
        sidebar_layout.setRowStretch(1, 1)
        sidebar_layout.setRowStretch(2, 1)
        sidebar_layout.setRowStretch(3, 7)
        
        # Add sidebar to container layout
        container_layout.addWidget(self.sidebar, 0, 0)
        
    # Create the pages
    #scans page
    def make_scans(self):
        page = QWidget()

        # Create layout for the page
        layout = QVBoxLayout(page)

        # Create top bar with page name
        top_bar_layout = QHBoxLayout()
        page_name_label = QLabel("Scans")
        page_name_label.setFixedHeight(50)
        top_bar_layout.addWidget(page_name_label)
        top_bar_layout.addStretch(1)  # Add stretch to push line edit and button to the right
        layout.addLayout(top_bar_layout)

        # Create line edit for path input
        path_line_edit = QLineEdit()
        path_line_edit.setPlaceholderText("Enter path...")
        layout.addWidget(path_line_edit)

        # Create horizontal layout for browse and scan button
        browse_layout = QHBoxLayout()

        # Create browse button
        browse_button = QPushButton("Browse")
        browse_button.setObjectName('browse')
        browse_button.setFixedWidth(120)  # Make the browse button smaller
        browse_layout.addWidget(browse_button)
        layout.addLayout(browse_layout)

        # Create scan button
        scan_button = QPushButton("Scan")
        scan_button.setFixedWidth(150)  # Make the scan button smaller
        layout.addWidget(scan_button)

        # Create text edit to display scan result
        scan_result_text_edit = QTextEdit()
        scan_result_text_edit.setReadOnly(True)  # Make it read-only
        layout.addWidget(scan_result_text_edit)

        # Function to handle browse button click
        def browse():
            file_path, _ = QFileDialog.getOpenFileName(self, 'Select File', QDir.rootPath(), 'All Files (*);;Python Files (*.py)')
            if file_path:
                path_line_edit.setText(file_path)

        # Connect functions
        browse_button.clicked.connect(browse)
        scan_button.clicked.connect(lambda: self.scan_func(path_line_edit.text(), scan_result_text_edit))

        return page
    
    #history page
    def make_history(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel()
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        return page
    
    
    #BUTTONS FUNCTIONS
    
    # Swap the pages
    def show_scans(self):
        self.scans.show()
        self.history.hide()
    def show_history(self):
        self.scans.hide()
        self.history.show()
        
    def scan_func(self,path, label: QLabel) -> None:
        label.setText("Loading...")
        
        
        #check path
        if not os.path.exists(path):
            label.setText("Path doesnt exist please put a valid one")
        else:
            analyze = manager.Analysis(path)
            results = analyze.run_analysis()
            label.setText(results)
        

        
def start():
    
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    start()
    