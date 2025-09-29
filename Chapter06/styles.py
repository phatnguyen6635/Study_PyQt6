import sys
from PyQt6.QtWidgets import QApplication, QStyleFactory

print(f"Keys: {QStyleFactory.keys()}")

app = QApplication(sys.argv)
print(f"Default style: {app.style().name()}")