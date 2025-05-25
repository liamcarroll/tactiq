import cv2
import torch
from ultralytics import YOLO

def detect_players(video_path):
    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(video_path)

    frame_num = 0
    positions = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        boxes = results[0].boxes
        persons = [box.xyxy.cpu().numpy() for box in boxes if int(box.cls) == 0]

        centers = []
        for box in persons:
            x1, y1, x2, y2 = box[0]
            cx = (x1 + x2) / 2
            cy = (y1 + y2) / 2
            centers.append((cx, cy))

        positions.append({'frame': frame_num, 'centers': centers})
        frame_num += 1

    cap.release()
    return positions

if __name__ == "__main__":
    video_file = "../data/sample_match.mp4"
    positions = detect_players(video_file)
    print(f"Detected players in {len(positions)} frames.")
