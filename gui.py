# THIS FILE WILL HANDLE THE GUI
import sys,os
import threading
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

#import the scrypt manager
from Spyware_Manager.manager import Analysis


#get stylesheet
def load_stylesheet(path):
    with open(path, "r") as file:
        return file.read()


class MainWindow(QMainWindow):
    #setup the main window
    def __init__(self):
        super().__init__()
        
        # Set up the analysis manager
        self.analysis = Analysis()
        
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

        # Create horizontal layout for scan button and checkbox
        scan_checkbox_layout = QHBoxLayout()

        # Create scan button
        scan_button = QPushButton("Scan")
        scan_button.setFixedWidth(150)  # Make the scan button smaller
        scan_checkbox_layout.addWidget(scan_button)

        # Create checkbox to save local sandbox data
        save_checkbox = QCheckBox("Save Local Sandbox Data")
        scan_checkbox_layout.addWidget(save_checkbox)

        layout.addLayout(scan_checkbox_layout)

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
        scan_button.clicked.connect(lambda: self.scan_func(path_line_edit.text(), scan_result_text_edit, save_checkbox.isChecked()))

        return page
    
    #history page
    def make_history(self):
        page = QWidget()

        # Create layout for the page
        layout = QVBoxLayout(page)

        # Create top bar with page name
        top_bar_layout = QHBoxLayout()
        page_name_label = QLabel("History")
        page_name_label.setFixedHeight(50)
        top_bar_layout.addWidget(page_name_label)
        top_bar_layout.addStretch(1)  # Add stretch to push line edit and button to the right
        layout.addLayout(top_bar_layout)

        # Create table for displaying history
        self.history_table = QTableWidget()
        layout.addWidget(self.history_table)

        return page

    

    
    
    #BUTTONS FUNCTIONS
    
    # Swap the pages
    def show_scans(self):
        self.scans.show()
        self.history.hide()
    def show_history(self):
        self.update_table(self.history_table)
        self.scans.hide()
        self.history.show()
        
    def scan_func(self,path, label: QLabel, sandbox) -> None:
        label.setText("Loading...")
        
        print(sandbox)
        #check path
        if not os.path.exists(path):
            label.setText("Path doesnt exist please put a valid one")
        else:
            results = self.analysis.run_analysis(path, sandbox)
            label.setText(results)

        
    
    def update_table(self, history_table: QTableWidget):
        data_list = self.analysis.load_data()
        if not data_list:
            history_table.setRowCount(0)
            history_table.setColumnCount(1)
            history_table.setHorizontalHeaderLabels(['No data found'])
            return 

        headers = list(data_list[0].keys())
        history_table.setColumnCount(len(headers))
        history_table.setHorizontalHeaderLabels(headers)
        
        history_table.setRowCount(len(data_list))
        for row, data in enumerate(data_list):
            for col, key in enumerate(headers):
                item = QTableWidgetItem(str(data[key]))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Make item read-only
                history_table.setItem(row, col, item)
        history_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        
        
def start():
    
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    start()
    