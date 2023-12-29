from PIL import Image
import cv2
import matplotlib.pyplot as plt
import torch
from ultralytics import YOLO
# Load the YOLO model
model_path = 'runs/detect/train9/weights/last.pt'
model = YOLO(model_path)

# Load the image you want to make predictions on
image_path = '0f8e6744ed8b322bbeb54599b309ecf2e0de4945_jpg.rf.627c93499696b4cac9430d16bed331fb.jpg'
img = cv2.imread(image_path)

# Perform inference
results = model(img)[0]
#print(results)
for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result
    print(x1, y1, x2, y2, score, class_id)
    cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
    cv2.putText(img, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow("image", img)

