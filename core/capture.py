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
    cmd = [
        "gst-launch-1.0", "-e",
        "v4l2src", f"device=/dev/video{CAMERA_ID}", "num-buffers=1",
        "!", f"video/x-raw,width={WIDTH},height={HEIGHT}",
        "!", "videoconvert",
        "!", "jpegenc",
        "!", "filesink", "location=image.jpg"
    ]

    try:
        subprocess.run(cmd, check=True)
        print("Photo captured successfully.")
        cwd = os.getcwd()
        image_path = os.path.join(cwd, "image.jpg")
        image = cv2.imread(image_path)
        return image
    except subprocess.CalledProcessError as e:
        print(f"Error capturing photo: {e}")




