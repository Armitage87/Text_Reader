import pytesseract
import os
import numpy as np
from PIL import Image
import cv2
import argparse

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image to be scanned")
args = vars(ap.parse_args())

image = args["image"]
text = pytesseract.image_to_string(Image.open(image))
print(text)
