import cv2
from detection import Detection

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


def run(video_source=0):

    model = Detection("model_lite.onnx")
    cap = cv2.VideoCapture(video_source)

    frame_size = (640, 640)
    # fps = 20
    # fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    # out = cv2.VideoWriter("output_video.mp4", fourcc, fps, frame_size)

    while True:
        ret, frame = cap.read()

        frame = cv2.resize(frame, frame_size)

        bboxes, scores, labels = model(frame)

        for box, score, class_id in zip(bboxes, scores, labels):
            if score > 0.7:
                x1, y1, x2, y2 = box.astype(int)
                label = class_names[class_id]
                color = (0, 0, 255)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

                text = f"{label}: {score:.2f}"
                (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                cv2.rectangle(frame, (x1, y1 - th - 4), (x1 + tw, y1), color, -1)
                cv2.putText(
                    frame,
                    text,
                    (x1, y1 - 2),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    1,
                )

        if not ret:
            break

        cv2.imshow("Video", frame)
        # out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    # out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run("ku_hall_2.mp4")
    pass
