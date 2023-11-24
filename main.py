from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (change this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open an image file
image_path = 'C://Users//inter//Downloads//text reg//IMG5.png'

image = Image.open(image_path)

language = 'eng'

# Use pytesseract to do OCR on the image with the specified language
text = pytesseract.image_to_string(Image.open(image_path), lang=language)
# Print the extracted text
print(text)
print(image)
