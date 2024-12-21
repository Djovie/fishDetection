# import sys
import os
from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtMultimedia import QCamera, QCameraInfo
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtWidgets import QFrame, QGraphicsDropShadowEffect, QLabel

class CameraWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.camera = None
        self.camera_on = False

        self.setFixedSize(1280, 720)
        self.setStyleSheet("background-color: black;")

        # Membuat viewfinder sebagai bagian dari frame
        self.viewfinder = QCameraViewfinder(self)
        self.viewfinder.setGeometry(5, 5, 1280, 720)

        # Menambahkan frame dan shadow effect
        self.createFrame()

        # Menyiapkan ikon kamera
        current_directory = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_directory, "icon", "cameraIcon.png")
        self.camera_icon = QPixmap(icon_path)

        self.camera_icon = self.camera_icon.scaled(600, 320, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Membuat QLabel untuk menampilkan ikon kamera
        self.camera_icon_label = QLabel(self)
        self.camera_icon_label.setPixmap(self.camera_icon)
        self.camera_icon_label.setGeometry(5, 5, 1280, 720)
        self.camera_icon_label.setAlignment(Qt.AlignCenter)

        # Sembunyikan ikon kamera di awal
        self.camera_icon_label.hide()

    def createFrame(self):
        """Menambahkan frame dan efek bayangan ke viewfinder."""
        self.setStyleSheet(f"""QFrame {{ 
                           border: 5px solid black; 
                           background: #000000;   
                           border-radius: 25px;         
                           }}"""
                        )
        
        # Menambahkan efek bayangan untuk frame
        shadow_effect = QGraphicsDropShadowEffect(self)
        # shadow_effect.setBlurRadius(15)
        shadow_effect.setXOffset(10)
        shadow_effect.setYOffset(10)
        shadow_effect.setColor(Qt.black)
        self.setGraphicsEffect(shadow_effect)

    def setupCamera(self, camera_index=0):
        """Menyiapkan kamera berdasarkan index yang diberikan."""
        cameras = QCameraInfo.availableCameras()
        if not cameras:
            raise RuntimeError("No cameras found.")
        
        self.camera = QCamera(cameras[camera_index])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()
        self.camera_on = True

    def changeCamera(self, index):
        """Mengubah kamera berdasarkan index yang dipilih."""
        if self.camera_on:
            self.camera.stop()
        self.setupCamera(index)

    def toggleCamera(self, state):
        """Menyalakan atau mematikan kamera berdasarkan status toggle switch."""
        if state == Qt.Checked:
            if not self.camera_on:
                self.camera.start()
                self.camera_on = True
                self.viewfinder.show()
                self.camera_icon_label.hide()
        else:
            if self.camera_on:
                self.camera.stop()
                self.camera_on = False
                self.viewfinder.hide()
                self.camera_icon_label.show()

    def getCenterColor(self):
        """Mengambil warna piksel di tengah viewfinder dan menghitung nilai RGB dan HSV."""
        image = self.viewfinder.grab().toImage()
        
        # Menghitung posisi piksel tengah
        width, height = image.width(), image.height()
        center_color = image.pixel(width // 2, height // 2)

        # Menghitung nilai RGB
        rgb = QColor(center_color).getRgb()

        # Menghitung nilai HSV
        hsv = QColor(center_color).toHsv()

        # Kembalikan nilai RGB dan HSV
        if self.camera_on:
            return (rgb[0], rgb[1], rgb[2]), (hsv.hue(), hsv.saturation(), hsv.value())
        else : 
            return (0, 0, 0), (0, 0, 0)

