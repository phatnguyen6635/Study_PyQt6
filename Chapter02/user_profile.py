import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        """ Set up the application's GUI."""
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("User Profile")
        
        self.setUpMainWindow()
        self.show()
        
    def createImageLabels(self):
        """ Open image files and create image labels."""
        images = ["./images/skyblue.png", "./images/profile_image.png"]
        
        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if "profile" in image:
                        label.move(80,20)
            except FileNotFoundError as error:
                print(f"Image file not found: {error}")

    def setUpMainWindow(self):
        """Create the labels to be displayed in the main window."""
        self.createImageLabels()
        
        name_label = QLabel(self)
        name_label.setText("Phat Nguyen Tan")
        name_label.setFont(QFont("Arial", 20))
        name_label.move(20, 140)
        
        bio_label = QLabel(self)
        bio_label.setText("CV Engineer")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(20, 180)
        
        about_label = QLabel(self)
        about_label.setText("I'm a Computer Vision Researcher\
                            Engineer with 2 years experience")
        about_label.setWordWrap(True) # Enable word wrapping
        about_label.move(20, 210)
        
        skills_label = QLabel(self)
        skills_label.setText("Skills")
        skills_label.setFont(QFont("Arial", 17))
        skills_label.move(20, 250)
        
        languages_label = QLabel(self)
        languages_label.setText("Python  |  C++  |  C")
        languages_label.move(20, 280)
        
        experience_label = QLabel(self)
        experience_label.setText("Experience")
        experience_label.setFont(QFont("Arial", 17))
        experience_label.move(20, 320)
        
        deverloper_label = QLabel(self)
        deverloper_label.setText("AI Developer at MVP Vietnam")
        deverloper_label.move(20, 350)
        
        dev_dates_label = QLabel(self)
        dev_dates_label.setText("May 2025 - Present")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(20, 380)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())