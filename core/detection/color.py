import cv2
import numpy as np
from core.capture import capture, store_image
from core.speech import speak
from core.config import config

colors_hsv = {
    "Red": [(0, 120, 70), (10, 255, 255)],
    "Red2": [(170, 120, 70), (180, 255, 255)],  # second red range
    "Green": [(36, 25, 25), (86, 255, 255)],
    "Blue": [(94, 80, 2), (126, 255, 255)],
    "Yellow": [(15, 150, 150), (35, 255, 255)],
    "Orange": [(10, 100, 20), (25, 255, 255)],
    "Purple": [(129, 50, 70), (158, 255, 255)],
    "Pink": [(160, 100, 100), (179, 255, 255)],
}


def detect():
    image = capture()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    color_found = None

    for color_name, (lower, upper) in colors_hsv.items():
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))

        if cv2.countNonZero(mask) > 500:
            color_found = color_name if color_name != "Red2" else "Red"
            break

    speak(f"{color_found}")

    (tw, th), _ = cv2.getTextSize(color_found, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 5)
    cv2.rectangle(image, (10, 50 - th - 1), (10 + tw, 50), (0, 0, 255), -1)

    cv2.putText(
        image,
        color_found,
        (10, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 255, 255),
        2,
    )

    store_image(image)
