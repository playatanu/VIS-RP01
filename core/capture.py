import cv2


def capture(camera_id=0):
    cap = cv2.VideoCapture(camera_id)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("Error: Cannot open camera")
        exit()

    ret, frame = cap.read()

    if ret:
        height, width = frame.shape[:2]

        crop_size = min(height, width, 640)

        start_x = (width - crop_size) // 2
        start_y = (height - crop_size) // 2

        cropped_image = frame[
            start_y : start_y + crop_size, start_x : start_x + crop_size
        ]

        cap.release()
        return cropped_image

    else:
        print("Error: Failed to capture image.")

    cap.release()
    return frame
