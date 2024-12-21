import os
from PyQt5.QtWidgets import QCheckBox, QComboBox, QLabel, QPushButton, QApplication, QGraphicsDropShadowEffect
from PyQt5.QtMultimedia import QCameraInfo
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QRect, QTimer


class SlideSwitch(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(220, 50)
        self.setChecked(True)  # Default is ON
        self.setStyleSheet("""
            QCheckBox {
                background-color: #444;
                border: 1px solid #888;
                border-radius: 25px;
                padding: 2px;
            }
            QCheckBox::indicator {
                width: 110px;
                height: 40px;
                border-radius: 20px;
                background-color: #CCCCCC;
                position: absolute;
                left: 2px;
                
            }
            QCheckBox::indicator:unchecked {
                background-color: #CCCCCC;
                left: 102px;
            }
            QCheckBox::indicator:pressed {
                background-color: #3E8E41;
            }
            QCheckBox::indicator:hover {
                background-color: #50D050;
            }
        """)

        # Create labels for "ON" and "OFF"
        self.on_label = QLabel("ON", self)
        self.off_label = QLabel("OFF", self)

        # Style for labels
        label_style = """
            QLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
                background: transparent;
            }
        """
        self.on_label.setStyleSheet(label_style)
        self.off_label.setStyleSheet(label_style)

        self.on_label.setGeometry(QRect(120, 10, 100, 30))
        self.on_label.setAlignment(Qt.AlignCenter)

        # Position 'OFF' label in the center of the right half
        self.off_label.setGeometry(QRect(10, 10, 100, 30))
        self.off_label.setAlignment(Qt.AlignCenter)

        # Position labels dynamically
        self.updateLabelPositions()

        # Connect state change to update labels
        self.stateChanged.connect(self.updateLabelPositions)
    
    def updateLabelPositions(self):
        """Update the position of 'ON' and 'OFF' labels."""
        if self.isChecked():
            self.on_label.show()
            self.off_label.hide()
        else:
            self.on_label.hide()
            self.off_label.show()

class CameraSelector(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_directory, "icon", "arrowIcon.png").replace("\\", "/")
        # self.arrow_icon = QPixmap(icon_path)

        self.setFixedSize(220, 50)
        self.setStyleSheet(f"""
            QComboBox {{
                background-color: #4A4A4A;
                color: white;
                border: 1px solid #888;
                font-size: 14px;
                font-weight: bold;
                border-radius: 25px;
                padding: 5px;
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 50px;
                border-left: 1px solid gray;
            }}          
            QComboBox::down-arrow {{
                image: url({icon_path}); 
                width: 30px;
                height: 30px; 
            }}
            QComboBox::item {{
                background-color: #4A4A4A;
                color: white;
            }}
            QComboBox::item:selected {{
                background-color: #5A5A5A;
            }}
        """)
        self.populateCameras()

    def populateCameras(self):
        """Populate the dropdown with available cameras."""
        cameras = QCameraInfo.availableCameras()
        if not cameras:
            raise RuntimeError("No cameras found.")
        
        for camera in cameras:
            self.addItem(camera.description())