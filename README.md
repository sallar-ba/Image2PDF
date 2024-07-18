# Image2PDF Converter

## Overview
Image2PDF Converter is a user-friendly desktop application designed to convert multiple image formats (JPG, JPEG, PNG, BMP, GIF, TIFF) into individual PDF files. The application dynamically organizes the converted PDFs into date-specific folders, ensuring efficient file management.

## Features
- **Image to PDF Conversion**: Supports multiple image formats and converts each image to a separate PDF file.
- **Dynamic Folder Creation**: Automatically creates folders named with the current date to store converted PDFs.
- **Progress Bar**: Provides visual feedback on the conversion process.
- **Modern User Interface**: Clean and simple UI with a custom application icon.

## Requirements
- Python 3.x
- PyQt6
- Pillow (PIL)

## Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required packages using pip:
    ```bash
    pip install PyQt6 Pillow
    ```

## Usage
1. Run the application:
    ```bash
    python main.py
    ```
2. Click the "Select Folder with Images" button to choose the folder containing images you want to convert.
3. The application will convert the images to PDFs and save them in a folder named with the current date within the selected folder.
4. The progress bar will indicate the conversion progress.

## Project Structure
```
image2pdf_converter/
├── image2pdf_converter.py   # Main application script
├── README.md                # Readme file
└── path/to/logo.png         # Application logo (replace with actual path)
```

