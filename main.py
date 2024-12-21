from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer

from CameraWidget import CameraWidget
from switches import *
from graphWidget import graphWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Inisialisasi antarmuka pengguna."""
        self.setWindowTitle("Camera Layout")
        self.setStyleSheet("background-color: #2E2E2E;")

        # Membuat widget kamera dan meletakkannya di main window
        self.camera_widget = CameraWidget(self)
        self.camera_selector = CameraSelector(self)
        self.toggle_switch = SlideSwitch(self)
        self.graph_widget = graphWidget(rgb_data=[0, 0, 0], hsv_data=[0, 0, 0])

        # Membuat label untuk judul
        self.title_label = QLabel("FISH DETECTION", self)
        self.title_label.setStyleSheet("""
                                        color: #D3D3D3; 
                                        font-size: 50px; 
                                        font-weight: bold; 
                                        padding-top:30px;
                                        font-family: 'Roboto';
                                        """)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFixedHeight(80) 

        self.layouting()

        # Menghubungkan sinyal dan slot
        self.camera_selector.currentIndexChanged.connect(
            lambda index: self.camera_widget.changeCamera(index)  # Memasukkan logika changeCamera langsung
        )
        
        self.toggle_switch.stateChanged.connect(
            lambda state: self.camera_widget.toggleCamera(state)  # Memasukkan logika toggleCamera langsung
        )

        # Setup kamera pertama kali
        self.camera_widget.setupCamera()

        self.showFullScreen()  # Menampilkan aplikasi dalam mode full screen

        # Timer untuk menampilkan RGB dan HSV secara berkala
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(10)  
    
    def layouting(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        central_widget = QWidget(self)
        central_layout = QHBoxLayout(central_widget)

        # Buat widget untuk membungkus camera_layout
        camera_widget_container = QWidget(self)
        camera_layout = QVBoxLayout(camera_widget_container)
        camera_layout.addWidget(self.camera_widget)

        # Buat widget untuk membungkus button_layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.camera_selector)
        button_layout.addWidget(self.toggle_switch)

        # Tambahkan widget ke dalam layout
        camera_layout.addLayout(button_layout)

        # Tambahkan layout ke dalam central_layout
        central_layout.addWidget(camera_widget_container)
        central_layout.addWidget(self.graph_widget)

        # Bungkus central_layout ke dalam QWidget
        central_widget_container = QWidget(self)
        central_widget_container.setLayout(central_layout)

        main_layout.addWidget(self.title_label)
        main_layout.addWidget(central_widget_container)

        self.setCentralWidget(main_widget)

    def update_graph(self):
        """Mengambil nilai RGB dan HSV terbaru dan memperbarui grafik."""
        rgb, hsv = self.camera_widget.getCenterColor()
        # if rgb and hsv:
        self.graph_widget.update_data(rgb, hsv)

    def resizeEvent(self, event):
        """Mengatur ulang posisi elemen-elemen jika ukuran window berubah."""
        self.camera_widget.setGeometry(5, 55, 650, 480)
        self.toggle_switch.setGeometry(665, 55, 200, 30)
        self.camera_selector.setGeometry(665, 95, 200, 30)
        self.graph_widget.setGeometry(665, 135, 300, 480)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
