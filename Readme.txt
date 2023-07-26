**Requirements:**
- Python 3.x
- Tesseract OCR installed on your machine. Make sure to set the Tesseract path in the script (`pytesseract.pytesseract.tesseract_cmd`).
- Required Python libraries: PIL (Python Imaging Library), pytesseract, googletrans

**Installation:**
1. Install Python (https://www.python.org/downloads/) if you haven't already.
2. Install required Python libraries by running the following commands in your terminal or command prompt:
   ```
   pip install pillow pytesseract googletrans==4.0.0-rc1
   ```
3. Install Tesseract OCR on your machine. You can download the installer from the official GitHub repository: https://github.com/tesseract-ocr/tesseract

4. After installing Tesseract OCR, set the Tesseract path in the script by modifying the line `pytesseract.pytesseract.tesseract_cmd` to point to the location where Tesseract is installed on your machine. 
  For example:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```
   Replace `'C:\Program Files\Tesseract-OCR\tesseract.exe'` with the actual path where Tesseract is installed on your system.
