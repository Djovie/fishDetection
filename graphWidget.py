from PyQt5.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

class graphWidget(QWidget):
    def __init__(self, rgb_data, hsv_data):
        super().__init__()

        self.rgb_data = rgb_data
        self.hsv_data = hsv_data
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Configurations for RGB and HSV
        configs = {
            "rgb": (self.rgb_data, ["#f04135", "#348c44", "#2d82fa"], ["R", "G", "B"]),
            "hsv": (self.hsv_data, ["#8a2be2", "#ff69b4", "#00bfff"], ["H", "S", "V"]),
        }

        # Generate layouts and bars
        bar_layouts, bar_groups = self.create_bar_layouts(configs)
        self.rgb_bars, self.hsv_bars = bar_groups["rgb"], bar_groups["hsv"]

        # Add to main layout
        main_layout = QVBoxLayout()

        for label_text, bar_layout in zip(["RGB Intensity", "HSV Intensity"], [bar_layouts["rgb"], bar_layouts["hsv"]]):
            label = QLabel(label_text)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("""
                                color: #D3D3D3; 
                                font-size: 12pt;
                                padding-bottom: 30px;
                                font-weight: bold; 
                                font-family: 'Roboto';
                                """)       
            main_layout.addStretch()
            main_layout.addWidget(label)
            main_layout.addLayout(bar_layout)

        main_layout.addStretch()
        layout.addLayout(main_layout)
        self.setLayout(layout)
    
    def create_bar_layouts(self, configs):
        """Helper function to create multiple bar layouts."""
        bars = {}
        layouts = {}
        for key, (data, colors, labels) in configs.items():
            bar_layout = QHBoxLayout()
            bar_group_layouts, bar_group = self.barGraph(data=data, color=colors, labels=labels)
            [bar_layout.addLayout(layout) for layout in bar_group_layouts]
            layouts[key] = bar_layout
            bars[key] = bar_group
        return layouts, bars

    def barGraph(self, data, color, labels):
        self.data = data
        colorModelBar = []  # List untuk menyimpan QProgressBar
        bar_layouts = []    # List untuk menyimpan layout (bar + label)

        for i, value in enumerate(self.data):
            # Progress bar
            color_bar = QProgressBar()
            color_bar.setOrientation(Qt.Vertical)
            color_bar.setMaximum(255)
            color_bar.setFixedSize(50, 300)
            color_bar.setValue(value)
            color_bar.setFormat(f"{value}")
            color_bar.setStyleSheet(f"""
                QProgressBar {{
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                    background: #2e2e2e;
                    color: 'white';
                    font-weight: bold;
                }}
                QProgressBar::chunk {{
                    background-color: {color[i]};
                    border-radius: 20px;
                    margin: 2px;
                }}
            """)

            # Label di bawah progress bar
            bar_label = QLabel(labels[i])
            bar_label.setAlignment(Qt.AlignCenter)
            bar_label.setStyleSheet("""
                color: white;
                font-weight: bold;
                font-family: 'Roboto';
            """)

            # Layout untuk menggabungkan bar dan label
            bar_layout = QVBoxLayout()
            bar_layout.addWidget(color_bar, alignment=Qt.AlignCenter)
            bar_layout.addWidget(bar_label)

            # Simpan layout dan QProgressBar
            bar_layouts.append(bar_layout)
            colorModelBar.append(color_bar)

        # Return layout untuk tampilan dan progress bar untuk manipulasi nilai
        return bar_layouts, colorModelBar

    def update_data(self, rgb_data, hsv_data):
        """Method to update the RGB and HSV data dynamically."""
        self.rgb_data = rgb_data
        self.hsv_data = hsv_data

        # Update the progress bars for RGB
        for i, value in enumerate(self.rgb_data):
           self.rgb_bars[i].setValue(value)
           self.rgb_bars[i].setFormat(f"{value}")

        # Update the progress bars for HSV
        for i, value in enumerate(self.hsv_data):
            self.hsv_bars[i].setValue(value)
            self.hsv_bars[i].setFormat(f"{value}")
