import sys
import os
import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox, QVBoxLayout, QWidget, QProgressBar
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
from PIL import Image

class ImageToPDFConverter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image2PDF Converter")
        self.setGeometry(100, 100, 400, 200)
        
        # Set window icon
        self.setWindowIcon(QIcon("assets/I2P.png"))

        layout = QVBoxLayout()

        self.button = QPushButton("Select Folder with Images")
        self.button.clicked.connect(self.convert_images_to_pdfs)
        self.button.setFont(QFont("Arial", 12))
        self.button.setStyleSheet("QPushButton {background-color: #4CAF50; color: white; border-radius: 5px; padding: 10px 20px;} QPushButton:hover {background-color: #45a049;}")
        layout.addWidget(self.button)

        self.progress_bar = QProgressBar()
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                width: 20px;
            }
        """)
        layout.addWidget(self.progress_bar)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def convert_images_to_pdfs(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if not folder_path:
            return

        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        output_folder = os.path.join(folder_path, current_date)
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")

        images = [filename for filename in os.listdir(folder_path) if filename.lower().endswith(image_extensions)]

        if not images:
            QMessageBox.information(self, "No Images Found", "No images were found in the selected folder.")
            return

        self.progress_bar.setMaximum(len(images))
        self.progress_bar.setValue(0)

        for index, filename in enumerate(images):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            pdf_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.pdf")
            image.convert("RGB").save(pdf_path, "PDF")
            self.progress_bar.setValue(index + 1)
        
        QMessageBox.information(self, "Success", f"Images have been converted to PDFs and saved in {output_folder}")

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Use Fusion style for a modern look
    window = ImageToPDFConverter()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
