import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QDateEdit, QTextEdit, QComboBox, QFormLayout,
                             QLineEdit, QHBoxLayout)
from PyQt6.QtCore import Qt, QRegularExpression, QDate
from PyQt6.QtGui import QFont, QRegularExpressionValidator

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        """ Set up the application's GUI."""
        self.setMinimumSize(500, 400)
        self.setWindowTitle("QFormLayout Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        header_label = QLabel("Appointment Form")
        header_label.setFont(QFont("Arial", 18))
        header_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.first_name_edit = QLineEdit()
        self.first_name_edit.setPlaceholderText("First")
        self.first_name_edit.textEdited.connect(self.clearText)
        
        self.last_name_edit = QLineEdit()
        self.last_name_edit.setPlaceholderText("Last")
        self.last_name_edit.textEdited.connect(self.clearText)

        name_h_box = QHBoxLayout()
        name_h_box.addWidget(self.first_name_edit)
        name_h_box.addWidget(self.last_name_edit)

        gender_combo = QComboBox()
        items = ["Male", "Female"]
        gender_combo.addItems(items)

        self.phone_edit = QLineEdit()
        self.phone_edit.setInputMask("(999) 999-9999;_") # Search on ChatGPT for details
        self.phone_edit.textEdited.connect(self.clearText)

        self.birthdate_edit = QDateEdit()
        self.birthdate_edit.setDisplayFormat("MM/dd/yyyy")
        self.birthdate_edit.setMaximumDate(QDate.currentDate())
        self.birthdate_edit.setCalendarPopup(True) # Open a calendar and select the date directly
        self.birthdate_edit.setDate(QDate.currentDate())

        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("<username>@<domain>.com")
        reg_opt = QRegularExpression()
        regex = QRegularExpression(
            "\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[com]{3}\\b",
            reg_opt.PatternOption.CaseInsensitiveOption)
        self.email_edit.setValidator(QRegularExpressionValidator(regex))
        self.email_edit.textEdited.connect(self.clearText)
        
        extra_info_edit = QTextEdit()

        self.feedback_label = QLabel()
        submit_button = QPushButton("SUBMIT")
        submit_button.setMaximumWidth(140)
        submit_button.clicked.connect(self.checkFormInformation)

        submit_h_box = QHBoxLayout()
        submit_h_box.addWidget(self.feedback_label)
        submit_h_box.addWidget(submit_button)

        main_form = QFormLayout()
        main_form.setFieldGrowthPolicy(main_form.FieldGrowthPolicy.AllNonFixedFieldsGrow) # Widgets will stretch when stretching the window
        main_form.setFormAlignment(Qt.AlignmentFlag.AlignHCenter |\
                                   Qt.AlignmentFlag.AlignTop)
        main_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        main_form.addRow(header_label)
        main_form.addRow("Name", name_h_box)
        main_form.addRow("Gender", gender_combo)
        main_form.addRow("Date of Birth", self.birthdate_edit)
        main_form.addRow("Phone", self.phone_edit)
        main_form.addRow("Email", self.email_edit)
        main_form.addRow(QLabel("Comments or Messages"))
        main_form.addRow(extra_info_edit)
        main_form.addRow(submit_h_box)

        self.setLayout(main_form)

    def clearText(self, text):
        """Clear the text for QLabel that provides feedback. """
        self.feedback_label.clear()

    def checkFormInformation(self):
        """Demonstrates a few cases for validating user input. """
        if self.first_name_edit.text() == "" or self.last_name_edit.text() == "":
            self.feedback_label.setText("[INFO] Missing names.")
        elif self.phone_edit.hasAcceptableInput() == False:
            self.feedback_label.setText("[INFO] Phone number entered incorrectly.")
        elif self.email_edit.hasAcceptableInput() == False:
            self.feedback_label.setText("[INFO] Email entered incorrectly.")

if __name__ == "__main__":
    app = QApplication(sys.argv)                         
    window = MainWindow()
    sys.exit(app.exec())
