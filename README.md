# Document Capture Coding Prototype

### Overview
This project is a technical assessment for an intern position at Docuville.ai. The objective is to capture and extract key details from important documents like passports and driver’s licenses. Using OCR and text processing, the prototype identifies three primary details: the **Name**, **Document Number**, and **Expiration Date**. 

### Features
- **OCR Processing**: Extracts text from images using EasyOCR.
- **Image Preprocessing**: Enhances images for better OCR accuracy.
- **Text Cleaning**: Standardizes OCR output to minimize errors.
- **Detail Extraction**: Uses regular expressions to locate specific details.

### Technologies Used
- **Python**: Programming language for development.
- **EasyOCR**: Library used for Optical Character Recognition.
- **PIL (Pillow)**: Used for image processing and enhancement.
- **Regular Expressions**: Extracts specific details from text.

### Folder Structure
- **main.py**: Main script that runs the extraction process.
- **preprocess_image.py**: Contains functions to enhance images.
- **extract_text.py**: Handles text extraction and cleaning.
- **images/**: Folder for sample images (for demonstration only).
- **screenshots/**: Includes example outputs.

### Getting Started

1. **Prerequisites**:
   - Python 3.x installed on your system.
   - Install required libraries using:
     ```bash
     pip install easyocr pillow
     ```

2. **Running the Project**:
   - Place a sample image in the images folder.
   - Update the image path in `main.py` (variable `image_path`) with the path to your document image.
   - Run the script:
     ```bash
     python main.py
     ```
   - The output will display the extracted details, or any error messages if the process encounters issues.

### Limitations
- Accuracy may vary based on image quality.
- Currently optimized for English-language documents.
- Regular expressions may need adjustment for different document layouts or formats.

### Project Feedback
This project allowed for hands-on experience with OCR and document processing. It was rewarding to see the text extraction and data structuring aspects come together. Future iterations could focus on handling more diverse document formats and expanding language support.
