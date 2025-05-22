import os
import cv2
import subprocess
from core.config import config

CAMERA_ID = config["camera"]["id"]
WIDTH = config["camera"]["width"]
HEIGHT = config["camera"]["height"]
OUTPUT_FILENAME = config["camera"]["output_filename"]


def store_image(image):
    cv2.imwrite(OUTPUT_FILENAME, image)


def capture():
    subprocess.run(
        [
            "fswebcam",
            "-r",
            f"{WIDTH}x{HEIGHT}",
            "-d" f"/dev/video{CAMERA_ID}",
            "--no-banner",
            "image.jpg",
        ]
    )

    cwd = os.getcwd()
    image_path = os.path.join(cwd, "image.jpg")
    image = cv2.imread(image_path)
    return image


# def capture():
#     cap = cv2.VideoCapture(CAMERA_ID)

#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

#     if not cap.isOpened():
#         print("Error: Cannot open camera")
#         exit()

#     ret, frame = cap.read()

#     if ret:
#         height, width = frame.shape[:2]

#         crop_size = min(height, width, CROP)

#         start_x = (width - crop_size) // 2
#         start_y = (height - crop_size) // 2

#         cropped_image = frame[
#             start_y : start_y + crop_size, start_x : start_x + crop_size
#         ]

#         cap.release()
#         return cropped_image

#     else:
#         print("Error: Failed to capture image.")

#     cap.release()
#     return frame
