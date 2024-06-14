import cv2
import pytesseract
import gradio as gr
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as needed

def ocr_image(image):
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray_image)

    return text


demo = gr.Interface(ocr_image, gr.Image(), "text", title="OCR")
demo.launch()
