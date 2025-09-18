from PyQt6.QtWidgets import QApplication, QLabel
import sys

app = QApplication(sys.argv)

label = QLabel("Hello world")
print(label.font().family())  # In ra tên font đang dùng