from utils import get_soup
from PIL import Image
import pytesseract
from config import BASE_URL
from urllib.request import urlopen
import ssl
import certifi

context = ssl.create_default_context(cafile=certifi.where())

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

soup = get_soup("/fish")


def get_image_text(image_url):
    image = Image.open(urlopen(f"{BASE_URL}{image_url}", context=context))
    text = pytesseract.image_to_string(image)
    return text


images_links = [get_image_text(image["src"]) for image in soup.select("img")]

print(images_links)
