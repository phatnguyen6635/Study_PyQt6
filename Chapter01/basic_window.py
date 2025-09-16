import sys
from PyQt6.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
    def __init__(self):
        """ Constructor for Empty Window Class."""
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        """ Set up the application."""
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Empty Window in PyQt6")
        self.show() # Display the window
        
if __name__ == "__main__":
    app = QApplication(sys.argv) # Pass command line arguments to the application
    # app: all application level settings and control flow                            
    window = EmptyWindow()
    sys.exit(app.exec()) # Start the event loop and wait the exit status to exit the application
