import sys, json
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QCheckBox, QTextEdit, QGridLayout)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        """ Set up the application's GUI."""
        self.setMinimumSize(500, 300)
        self.setWindowTitle("QGridLayout Example")
        
        self.steUpMainWindow()
        self.loadWidgetValuesFromFile()
        self.show()
    
    def steUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        header_label = QLabel("Simple Daily Planner")
        header_label.setFont(QFont("Arial", 20))
        header_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        today_label = QLabel("· Today's Focus")
        today_label.setFont(QFont("Arial", 14))
        self.today_tedit = QTextEdit()
        
        notes_label = QLabel("· Notes")
        notes_label.setFont(QFont("Arial", 14))
        self.notes_tedit = QTextEdit()
        
        self.main_grid = QGridLayout()
        self.main_grid.addWidget(header_label, 0, 0)
        self.main_grid.addWidget(today_label, 1, 0)
        self.main_grid.addWidget(self.today_tedit, 2, 0, 3, 1)
        self.main_grid.addWidget(notes_label, 5, 0)
        self.main_grid.addWidget(self.notes_tedit, 6, 0, 3, 1)
        
        today = QDate.currentDate().toString(Qt.DateFormat.ISODate)
        date_label = QLabel(today)
        date_label.setFont(QFont("Arial", 18))
        date_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        todo_label = QLabel("· To do")
        todo_label.setFont(QFont("Arial", 14))
        
        self.main_grid.addWidget(date_label, 0, 2)
        self.main_grid.addWidget(todo_label, 1, 1, 1, 2)
        
        for row in range(2, 9):
            item_cb = QCheckBox()
            item_edit = QLineEdit()
            self.main_grid.addWidget(item_cb, row, 1)
            self.main_grid.addWidget(item_edit, row, 2)
        
        self.setLayout(self.main_grid)
    
    def saveWidgetValues(self):
        """Collect and save the widget values."""
        details = {"focus":self.today_tedit.toPlainText(),
                   "notes":self.notes_tedit.toPlainText()}
        
        remaining_todo = []
        
        for row in range(2, 9):
            item = self.main_grid.itemAtPosition(row, 1)
            widget = item.widget()
            
            if widget.isChecked() == False:
                item = self.main_grid.itemAtPosition(row, 2)
                
                widget = item.widget()
                text = widget.text()
                if text != "":
                    remaining_todo.append(text)
                
        details["todo"] = remaining_todo
        with open("details.txt", "w") as f:
            f.write(json.dumps(details))
            
    def closeEvent(self, event):
        """Save widget values when closing the window. """
        self.saveWidgetValues()
        
    def loadWidgetValuesFromFile(self):
        """Retrieve previos values from the last session. """
        try:
            with open("details.txt", "r") as f:
                details = json.load(f)
                
                self.today_tedit.setText(details["focus"])
                self.notes_tedit.setText(details["notes"])
                
                for row in range(len(details["todo"])):
                    item = self.main_grid.itemAtPosition(row+2, 2)
                    widget = item.widget()
                    widget.setText(details["todo"][row])
        
        except FileNotFoundError as error:
            f = open("details.txt", "w")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)                    
    window = MainWindow()
    sys.exit(app.exec())