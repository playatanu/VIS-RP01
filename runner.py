import cv2
from core.capture import capture
from core.detection import color, text, object


def mode(option):
    match option:
        case 0:
            return color.detect(image)
        case 1:
            return text.detect(image)
        case 2:
            return object.detect(image)
        case _:
            return color.detect(image)


if __name__ == "__main__":
    while True:
        option = input("key: ")

        if option == "exit":
            exit()

        image = capture(camera_id=0)
        image = mode(int(option))
        cv2.imwrite("capure_image.jpg", image)
