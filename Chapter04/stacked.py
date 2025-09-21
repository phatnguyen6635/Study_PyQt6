import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                             QTextEdit, QComboBox, QSpinBox, QDoubleSpinBox,
                             QStackedLayout, QFormLayout, QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        """ Set up the application's GUI."""
        self.setFixedSize(300, 340)
        self.setWindowTitle("QStackedLayout Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""

        page_combo = QComboBox()
        items = ["Image", "Description", "Addition Infor"]
        page_combo.addItems(items)
        page_combo.activated.connect(self.switchPage)

        profile_image = QLabel()
        pixel_map = QPixmap("./images/norwegian.jpg")
        profile_image.setPixmap(pixel_map)
        profile_image.setScaledContents(True)

        pg2_form = QFormLayout()
        pg2_form.setFieldGrowthPolicy(pg2_form.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        pg2_form.setFormAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        pg2_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        pg2_form.addRow("Breed:", QLabel("Norwegian Forest cat"))
        pg2_form.addRow("Origin:", QLabel("Norway"))
        pg2_form.addRow(QLabel("Description"))
        default_text = """Have a long, sturdy body, long legs
        and a bushy tail. They are friendly, intelligent,
        and generally good with people."""
        pg2_form.addRow(QTextEdit(default_text))
        pg2_container = QWidget()
        pg2_container.setLayout(pg2_form)

        pg3_form = QFormLayout()
        pg3_form.setFieldGrowthPolicy(pg3_form.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        pg3_form.setFormAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        pg3_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        pg3_form.addRow(QLabel("Enter your cat's info."))
        pg3_form.addRow("Name:", QLineEdit())
        pg3_form.addRow("Color:", QLineEdit())
        age_sb = QSpinBox() # For interger
        age_sb.setRange(0, 30)
        pg3_form.addRow("Age:", age_sb)
        weight_dsb = QDoubleSpinBox() # For floating
        weight_dsb.setRange(0.0, 30.0)
        pg3_form.addRow("Weight (kg):", weight_dsb)
        pg3_container = QWidget()
        pg3_container.setLayout(pg3_form)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(profile_image)
        self.stacked_layout.addWidget(pg2_container)
        self.stacked_layout.addWidget(pg3_container)
        
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(page_combo)
        main_v_box.addLayout(self.stacked_layout)

        self.setLayout(main_v_box)

    def switchPage(self, index):
        """Slot for switch between tabs. """
        self.stacked_layout.setCurrentIndex(index)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)                         
    window = MainWindow()
    sys.exit(app.exec())
