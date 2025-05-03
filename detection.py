import cv2
import numpy as np
import onnxruntime as ort


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


if __name__ == "__main__":
    pass
