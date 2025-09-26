import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                             QPushButton, QDockWidget, QDialog, QFileDialog,
                             QMessageBox, QToolBar, QStatusBar, QVBoxLayout)
from PyQt6.QtCore import Qt, QSize, QRect
from PyQt6.QtGui import QIcon, QAction, QPixmap, QTransform, QPainter
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        """ Set up the application's GUI."""
        self.setFixedSize(650, 650)
        self.setWindowTitle("5.2 - Photo Editor GUI")
        
        self.setUpMainWindow()
        self.createToolsDockWidget()
        self.createActions()
        self.createMenu()
        self.createToolBar()
        self.show()
    
    def setUpMainWindow(self):
        """Create and arange widgets in the main window."""
        self.image = QPixmap()
        
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.image_label)
        
        self.setStatusBar(QStatusBar())
    
    def createActions(self):
        """Create the application's menu actions."""
        self.open_act = QAction(QIcon("./images/open_file.png"), "Open")
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.setStatusTip("Open a new image")
        self.open_act.triggered.connect(self.openImage)
        
        self.save_act = QAction(QIcon("./images/save_file.png"), "Save")
        self.save_act.setShortcut("Ctrl+S")
        self.save_act.setStatusTip("Save image")
        self.save_act.triggered.connect(self.saveImage)
        
        self.print_act = QAction(QIcon("./images/print.png"), "Print")
        self.print_act.setShortcut("Ctrl+P")
        self.print_act.setStatusTip("Print image")
        self.print_act.triggered.connect(self.printImage)
        self.print_act.setEnabled(False)
        
        self.quit_act = QAction(QIcon("./images/exit.png"), "Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.setStatusTip("Quit program")
        self.quit_act.triggered.connect(self.close)        
        
        self.rotate90_act = QAction("Rotate 90°")
        self.rotate90_act.setStatusTip("Rotate image 90° clockwise")
        self.rotate90_act.triggered.connect(self.rotateImage90)
        
        self.rotate180_act = QAction("Rotate 180°")
        self.rotate180_act.setStatusTip("Rotate image 180° clockwise")
        self.rotate180_act.triggered.connect(self.rotateImage180)
        
        self.flip_hor_act = QAction("Filp Horizontal°")
        self.flip_hor_act.setStatusTip("Flip image across horizontal image axis")
        self.flip_hor_act.triggered.connect(self.flipImageHorizontal)
        
        self.flip_ver_act = QAction("Filp Vertical")
        self.flip_ver_act.setStatusTip("Flip image across vertical image axis")
        self.flip_ver_act.triggered.connect(self.flipImageVertical)
        
        self.resize_act = QAction("Resize Half")
        self.resize_act.setStatusTip("Resize image to half original size")
        self.resize_act.triggered.connect(self.resizeImageHalf)
        
        self.clear_act = QAction(QIcon("./images/clear.png"), "Clear Image")
        self.clear_act.setShortcut("Ctrl+D")
        self.clear_act.setStatusTip("Clear the current image")
        self.clear_act.triggered.connect(self.clearImage)
        
    def createMenu(self):
        """Create the application's menu bar. """
        self.menuBar().setNativeMenuBar(False) # Enable native bar default from systems
        
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.print_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)
        
        edit_menu = self.menuBar().addMenu("Edit")
        edit_menu.addAction(self.rotate90_act)
        edit_menu.addAction(self.rotate180_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.flip_hor_act)
        edit_menu.addAction(self.flip_ver_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.clear_act)
        
        view_menu = self.menuBar().addMenu("View")
        view_menu.addAction(self.toggle_dock_tools_act)
        
    def createToolsDockWidget(self):
        """Create the application's dock widget. Use view -> 
        Edit Image Tool menu to show/hide the dock. """
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Edit Image Tools")
        dock_widget.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea |
                                    Qt.DockWidgetArea.RightDockWidgetArea)
        
        self.rotate90 = QPushButton("Rotate 90°")
        self.rotate90.setMinimumSize(QSize(130, 40))
        self.rotate90.setStatusTip("Rotate image 90° clockwise")
        self.rotate90.clicked.connect(self.rotateImage90)
        
        self.rotate180 = QPushButton("Rotate 180°")
        self.rotate180.setMinimumSize(QSize(130, 40))
        self.rotate180.setStatusTip("Rotate image 180° clockwise")
        self.rotate180.clicked.connect(self.rotateImage180)
        
        self.flip_horizontal = QPushButton("Flip Horizontal")
        self.flip_horizontal.setMinimumSize(QSize(130, 40))
        self.flip_horizontal.setStatusTip("Flip image across horizontal image axis")
        self.flip_horizontal.clicked.connect(self.flipImageHorizontal)
        
        self.flip_vertical = QPushButton("Flip Vertical")
        self.flip_vertical.setMinimumSize(QSize(130, 40))
        self.flip_vertical.setStatusTip("Flip image across vertical image axis")
        self.flip_vertical.clicked.connect(self.flipImageVertical)
        
        self.resize_half = QPushButton("Resize Half")
        self.resize_half.setMinimumSize(QSize(130, 40))
        self.resize_half.setStatusTip("Resize image to half original size")
        self.resize_half.clicked.connect(self.resizeImageHalf)
        
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.rotate90)
        dock_v_box.addWidget(self.rotate180)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.flip_horizontal)
        dock_v_box.addWidget(self.flip_vertical)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.resize_half)
        dock_v_box.addStretch(10)

        tools_container = QWidget()
        tools_container.setLayout(dock_v_box)
        dock_widget.setWidget(tools_container)
        
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock_widget)
        
        self.toggle_dock_tools_act = dock_widget.toggleViewAction() # Turn on/off view docwidget

    def createToolBar(self):
        """Create the application's toolbar. """
        tool_bar = QToolBar("Photo Editor Toolbar")
        tool_bar.setIconSize(QSize(24, 24))
        self.addToolBar(tool_bar)
        
        tool_bar.addAction(self.open_act)
        tool_bar.addAction(self.save_act)
        tool_bar.addAction(self.print_act)
        tool_bar.addAction(self.clear_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.quit_act)
            
    def openImage(self):
        """Open an image file and display its contents on the QLabel widget. """
        image_file, _ = QFileDialog.getOpenFileName(
                                                    self, "Open Image", "",
                                                    "JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files (*.bmp);;GIF Files (*.gif)")
        if image_file:
            self.image = QPixmap(image_file)

            self.image_label.setPixmap(self.image.scaled(self.image_label.size(),
                                       Qt.AspectRatioMode.KeepAspectRatio,
                                       Qt.TransformationMode.SmoothTransformation))
        else:
            QMessageBox.information(self, "No Image",
                                    "No Image Selected.",
                                    QMessageBox.StandardButton.Ok)
        
        self.print_act.setEnabled(True)

    def saveImage(self):
        """Display QFileDialog to select image location and save the image. """
        
        image_file, _ = QFileDialog.getSaveFileName(
                                            self, "Save Image", "",
                                            "JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;\
                                            Bitmap Files (*.bmp);;GIF Files (*.gif)")
        
        if image_file and self.image.isNull() == False:
            self.image.save(image_file)
        else:
            QMessageBox.information(self, "Not Saved", "Image not saved.",
                                    QMessageBox.StandardButton.Ok)
    
    def rotateImage90(self):
        """Rotate image 90° clockwise."""
        if self.image.isNull() == False:
            transform90 = QTransform().rotate(90)
            pixmap = QPixmap(self.image)
            mode = Qt.TransformationMode.SmoothTransformation
            rotated = pixmap.transformed(transform90, mode=mode)
            
            self.image_label.setPixmap(rotated.scaled(self.image_label.size(),
                                       Qt.AspectRatioMode.KeepAspectRatio,
                                       Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(rotated)
            self.image_label.repaint()

    def rotateImage180(self):
        """Rotate image 180° clockwise."""
        if self.image.isNull() == False:
            transform180 = QTransform().rotate(180)
            pixmap = QPixmap(self.image)
            mode = Qt.TransformationMode.SmoothTransformation
            rotated = pixmap.transformed(transform180, mode=mode)
            
            self.image_label.setPixmap(rotated.scaled(self.image_label.size(),
                                       Qt.AspectRatioMode.KeepAspectRatio,
                                       Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(rotated)
            self.image_label.repaint()

    def flipImageHorizontal(self):
        """Mirror the image across the horizontal axis. """
        if self.image.isNull() == False:
            flip_h = QTransform().scale(-1, 1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_h)
            
            self.image_label.setPixmap(flipped.scaled(self.image_label.size(),
                                        Qt.AspectRatioMode.KeepAspectRatio,
                                        Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(flipped)
            self.image_label.repaint()
            
    def flipImageVertical(self):
        """Mirror the image across the vertical axis. """
        if self.image.isNull() == False:
            flip_v = QTransform().scale(1, -1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_v)
            
            self.image_label.setPixmap(flipped.scaled(self.image_label.size(),
                                        Qt.AspectRatioMode.KeepAspectRatio,
                                        Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(flipped)
            self.image_label.repaint()
    
    def resizeImageHalf(self):
        """Resize the image to half its current size. """
        if self.image.isNull() == False:
            resize = QTransform().scale(0.5, 0.5)
            pixmap = QPixmap(self.image)
            resized = pixmap.transformed(resize)
            
            self.image_label.setPixmap(resized.scaled(self.image_label.size(),
                                        Qt.AspectRatioMode.KeepAspectRatio,
                                        Qt.TransformationMode.SmoothTransformation))
            self.image = QPixmap(resized)
            self.image_label.repaint()
    
    def clearImage(self):
        """Clear current image in the QLabel widget. """
        self.image_label.clear()
        self.image = QPixmap()
        self.print_act.setEnabled(False)
    
    def printImage(self):
        """Print image and use QPrinter to select the native system format for
        printer dialog. """
        printer = QPrinter()
        print_dialog = QPrintDialog(printer)
        
        if print_dialog.exec() == QDialog.DialogCode.Accepted:
            
            painter = QPainter()
            painter.begin(printer)
            
            rect = QRect(painter.viewport())
            size = QSize(self.image_label.pixmap().size())
            size.scale(rect.size(),
                       Qt.AspectRatioMode.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(),
                                size.width(), size.height())
            painter.setWindow(self.image_label.pixmap().rect())
            
            painter.drawPixmap(0, 0, self.image_label.pixmap())
            painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(Qt.ApplicationAttribute.AA_DontShowIconsInMenus, True)                       
    window = MainWindow()
    sys.exit(app.exec())
