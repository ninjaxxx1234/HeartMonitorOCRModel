
import cv2
import matplotlib.pyplot as plt
import torch
from ultralytics import YOLO
# Load the YOLO model
model_path = 'runs/detect/train11/weights/last.pt'
model = YOLO(model_path)

# Load the image you want to make predictions on
image_path = 'dulled_screen2.jpg'
img = cv2.imread(image_path)
results = model(img)[0]


'''x1, y1, x2, y2 = 205.41024780273438, 170.9076385498047, 320.2577819824219, 460.08575439453125
score = 0.4237764775753021
class_id = 0  # Replace with the actual class ID'''

# Load the image (replace "path/to/your/image.jpg" with your actual image path)
image = cv2.imread(image_path)

results_list = results.boxes.data.tolist()

# Specify the file path where you want to store the data
file_path = "output_dulled.txt"

# Open the file in write mode
with open(file_path, 'w') as file:
    # Iterate through each result and write the variables to the file
    for result in results_list:
        x1, y1, x2, y2, score, class_id = result
        line = f"{x1} {y1} {x2} {y2} {score} {class_id}\n"
        file.write(line)

print(f"Data has been successfully written to {file_path}")