import cv2
import gradio


def detect_faces(input_image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray_img = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(input_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return input_image


demo = gradio.Interface(fn=detect_faces, inputs=gradio.Image(), outputs="image", title="Face Detection")
demo.launch()

