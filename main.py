from ultralytics import YOLO
import cv2

model = YOLO('yolo11n.pt')

cap = cv2.VideoCapture(1)
cv2.namedWindow('YOLOv11 Detection', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('YOLOv11 Detection', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while cap.isOpened():
    success, frame = cap.read()

    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow('YOLOv11 Detection', annotated_frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('f'):
            fullscreen = cv2.getWindowProperty('YOLO11 Detection', cv2.WND_PROP_FULLSCREEN)
            if fullscreen == 1:
                cv2.setWindowProperty('YOLOv11 Detection', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
            else:
                cv2.setWindowProperty('YOLOv11 Detection', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cap.release()
cv2.destroyAllWindows()
