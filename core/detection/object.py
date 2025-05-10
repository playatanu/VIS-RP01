import os
import cv2
import numpy as np
import onnxruntime as ort
from core.capture import capture, store_image
from core.speech import speak

class_names = [
    "bg",
    "ac",
    "board",
    "chair",
    "clock",
    "door",
    "fan",
    "light",
    "switch board",
    "window",
]


class Detection:
    def __init__(self, onnx_model_path):
        self.session = ort.InferenceSession(onnx_model_path)

    def __call__(self, image):

        input_image = self.preprocessor(image)

        inputs = {self.session.get_inputs()[0].name: input_image}
        output = self.session.run(None, inputs)
        bboxes, scores, labels = output[0], output[1], output[2]
        return bboxes, scores, labels

    def preprocessor(self, image):
        input_image = cv2.resize(image, (640, 640))
        input_image = input_image.astype(np.float32)
        input_image = np.transpose(input_image, (2, 0, 1))
        input_image = np.expand_dims(input_image, axis=0)
        input_image /= 255.0

        return input_image


model_path = os.path.abspath("models/model_lite.onnx")
model = Detection(model_path)


def detect():
    text = ""
    image = capture()
    bboxes, scores, labels = model(image)

    for box, score, class_id in zip(bboxes, scores, labels):
        if score > 0.7:
            x1, y1, x2, y2 = box.astype(int)
            label = class_names[class_id]
            color = (0, 0, 255)
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)

            _text = f"{label}: {score:.2f}"
            (tw, th), _ = cv2.getTextSize(_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            cv2.rectangle(image, (x1, y1 - th - 4), (x1 + tw, y1), color, -1)
            cv2.putText(
                image,
                _text,
                (x1, y1 - 2),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                1,
            )

            text = str(label) + " " + text

    if text != "":
        speak(text)
    else:
        text = "no detection!"
        speak(text)

    store_image(image)
