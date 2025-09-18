import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        """ Set up the application's GUI."""
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle("QPushButton Example")
        
        self.setUpMainWindow()
        self.show()
        
    def setUpMainWindow(self):
        """ Create and arrange widgets in the main window."""
        self.times_pressed = 0
        
        self.name_label = QLabel("Don't push the button",self)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter) # Combination of AlignVCenter and AlignHCenter, this is for text inside the label
        self.name_label.move(60, 30) # This is for the label position in the window

        self.button = QPushButton("Push me!", self)
        self.button.move(80, 70)
        self.button.clicked.connect(self.buttonClicked)
        
    def buttonClicked(self):
        """Handle when the button is clicked.
        Demonstrates how to change text for widgets,
        update their sizes and locations, and how to
        close the window due to events."""
        self.times_pressed += 1
        if self.times_pressed == 1:
            self.name_label.setText("Why did you push me?")
        elif self.times_pressed == 2:
            self.name_label.setText("I'm warning you")
            self.button.setText("Feelin' Lucky?")
            self.button.adjustSize() # Adjust button size to fit new text
            self.button.move(70, 70)
        elif self.times_pressed == 3:
            print("The window has been closed")
            self.close()
    
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
