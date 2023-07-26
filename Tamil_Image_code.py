import os
from PIL import Image, ImageDraw, ImageFont
import pytesseract
from googletrans import Translator
# Install Tesseract OCR on your machine and set the path below accordingly
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        # Load the image
        image = Image.open(image_path)
        # Extract text from the image
        extracted_text = pytesseract.image_to_string(image, lang='eng')
        return extracted_text
    except Exception as e:
        print(f"Error: {e}")
        return None

def translate_to_tamil(text):
    try:
        translator = Translator()
        translated_text = translator.translate(text, src='en', dest='ta')
        return translated_text.text
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_text_as_image(text, output_path):
    try:
        image = Image.new('RGB', (500, 300), color='white')
        image_draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 20)
        image_draw.text((10, 10), text, fill='black', font=font)
        image.save(output_path)
        print("Output image saved successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_file = input("Enter the path of the input image: ")
    if not os.path.exists(input_file):
        print("Error: Input image not found.")
    else:
        # Extract text from the input image
        extracted_text = extract_text_from_image(input_file)
        if extracted_text:
            # Translate the extracted text to Tamil
            translated_text = translate_to_tamil(extracted_text)
            if translated_text:
                # Save the translated text as an image
                output_file = os.path.splitext(os.path.basename(input_file))[0] + "_translated.png"
                save_text_as_image(translated_text, output_file)
            else:
                print("Translation failed.")
        else:
            print("Text extraction failed.")
