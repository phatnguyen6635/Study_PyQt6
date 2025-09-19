import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QCheckBox,
                             QPushButton, QButtonGroup, QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        """ Set up the application's GUI."""
        self.setMinimumSize(350, 200)
        self.setWindowTitle("QVBoxLayout Example")
        
        self.setUpMainWindow()
        self.show()
        
    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        
        header_label = QLabel("Chez PyQt6")
        header_label.setFont(QFont("Arial", 18))
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        question_label = QLabel("How would you rate my service?")
        question_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        ratings = ["Satisfied", "Average", "Not Satisfied"]
        ratings_group = QButtonGroup(self) # QButtonGroup must be a member of class to communicate to other wigets
        ratings_group.buttonClicked.connect(self.checkboxClicked)
        
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setEnabled(False)
        self.confirm_button.clicked.connect(self.print)
        
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(header_label)
        main_v_box.addWidget(question_label)
        
        for cb in ratings:
            ratings_cb = QCheckBox(cb)
            ratings_group.addButton(ratings_cb)
            main_v_box.addWidget(ratings_cb)
            
        main_v_box.addWidget(self.confirm_button)
        self.setLayout(main_v_box)
        
    def checkboxClicked(self, button):
        """Check if a QCheckBox in the button group has been cliked. """
        print(button.text())
        self.confirm_button.setEnabled(True)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())