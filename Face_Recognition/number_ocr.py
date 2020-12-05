import pytesseract as pt
import cv2
from PIL import Image

# 生成图片实例
# Get a reference to webcam #0 (the default one)
#video_capture = cv2.VideoCapture(0)

image = Image.open('number.jpg')

text = pt.image_to_string(image)

print(text)

