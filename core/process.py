import cv2


def frame_process(frame):
    cv2.putText(
        frame,
        "Hola",
        (10, 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2,
        cv2.LINE_AA,
    )
    cv2.imshow("Resized Camera Feed", frame)
    return frame
