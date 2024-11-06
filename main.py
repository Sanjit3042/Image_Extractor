import easyocr
import re
from PIL import Image, ImageOps, ImageEnhance
import numpy as np

def preprocess_image(image_path):
    """Enhance the image for better OCR results."""
    image = Image.open(image_path)
    
    # Convert to grayscale
    grayscale_image = ImageOps.grayscale(image)
    
    # Increase contrast
    enhancer = ImageEnhance.Contrast(grayscale_image)
    contrast_image = enhancer.enhance(2)
    
    # Resize to enhance readability
    resized_image = contrast_image.resize((contrast_image.width * 2, contrast_image.height * 2))
    
    # Convert to binary image with thresholding
    binary_image = resized_image.point(lambda x: 0 if x < 140 else 255, '1')
    
    # Convert binary image to numpy array in uint8 format
    image_array = np.array(binary_image).astype(np.uint8) * 255
    return image_array

def extract_text_with_easyocr(image_path):
    """Perform OCR on the preprocessed image and return extracted text."""
    processed_image = preprocess_image(image_path)
    reader = easyocr.Reader(['en'])
    result = reader.readtext(processed_image, detail=0)
    text = " ".join(result)
    return text

def clean_text(text):
    """Remove excessive special characters and normalize whitespace."""
    # Replace common OCR mistakes
    text = text.replace("0", "O").replace("1", "I").replace("5", "S").replace("7", "T")
    
    # Remove unwanted characters and normalize spaces
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_details(text):
    """Extracts name, document number, and expiration date from OCR text."""
    # Updated regex patterns with more flexibility
    document_number_pattern = r'\b[A-Z0-9]{8,9}\b'  # Standard passport number format
    expiration_date_pattern = r'\b(\d{2}\s?[A-Z]{3,}\s?\d{2,4})\b'  # More flexible date format

    # Extract document number
    document_number = re.search(document_number_pattern, text)
    document_number = document_number.group(0) if document_number else None

    # Extract expiration date
    expiration_date = re.search(expiration_date_pattern, text)
    expiration_date = expiration_date.group(0) if expiration_date else None

    # Refine name extraction pattern, target names with at least two uppercase words
    name_pattern = r'\b([A-Z]{2,} [A-Z]{2,}(?: [A-Z]{2,})?)\b'
    possible_names = re.findall(name_pattern, text)
    
    # Filter names that may match non-name words, select a name if valid
    name = None
    for possible_name in possible_names:
        if "UNITED" not in possible_name and "KINGDOM" not in possible_name:  # Filter out irrelevant words
            name = possible_name
            break

    return {
        'name': name,
        'document_number': document_number,
        'expiration_date': expiration_date
    }

def main():
    image_path = r"C:\Users\user\Downloads\project\archive\passport2.jpeg"
    
    try:
        # Step 1: Extract text from the image
        raw_text = extract_text_with_easyocr(image_path)
        if not raw_text:
            print("Error: No text extracted from the image.")
            return
        
        print("OCR Output:", raw_text)
        
        # Step 2: Clean up the text
        cleaned_text = clean_text(raw_text)
        print("Cleaned Text:", cleaned_text)
        
        # Step 3: Extract specific details
        extracted_data = extract_details(cleaned_text)
        
        # Check if all required fields are captured
        if not all(extracted_data.values()):
            print("Warning: Some fields could not be extracted completely.")
        
        print("Extracted Data:", extracted_data)
        
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

