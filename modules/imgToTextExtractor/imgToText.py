from PIL import Image
import pytesseract

# extraer texto

img = Image.open('01.jpg')

texto = pytesseract.image_to_string( img, lang='esp' )
print(texto)

# todo no funciona