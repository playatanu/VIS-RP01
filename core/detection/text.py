import cv2
import pytesseract
from core.capture import capture, store_image
from core.speech import speak


def detect():
    image = capture()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
    text = pytesseract.image_to_string(thresh)

    (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 5)
    cv2.rectangle(image, (10, 50 - th - 1), (10 + tw, 50), (0, 0, 255), -1)

    cv2.putText(
        image,
        text,
        (10, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 255, 255),
        2,
    )

    if text != "":
        speak(text)
    else:
        text = "no detection!"
        speak(text)

    store_image(image)
