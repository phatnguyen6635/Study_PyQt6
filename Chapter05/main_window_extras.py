import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QCheckBox, QTextEdit, QDockWidget,
                             QToolBar, QStatusBar, QVBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        """ Set up the application's GUI."""
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Adding More Window Features")
        
        self.setUpMainWindow()
        self.createDockWiget()
        self.createActions()
        self.createMenu()
        self.createToolBar()
        self.show()
    
    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.setStatusBar(QStatusBar())
    
    def createDockWiget(self):
        pass
    
    def createActions(self):
        pass
    
    def createMenu(self):
        pass
    
    def createToolBar(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)                
    window = MainWindow()
    sys.exit(app.exec())