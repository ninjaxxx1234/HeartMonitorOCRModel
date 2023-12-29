import cv2

# Load the image
 # Replace with your image path


# Read the file with the bounding box information
image_path = 'dulled_screen2.jpg'# Replace with the path to your output file
image = cv2.imread(image_path)
file_path = "output_dulled.txt"
with open(file_path, 'r') as file:
    lines = file.readlines()

# Iterate through each line and draw boxes on the image
for line in lines:
    # Parse the values from the line
    x1, y1, x2, y2, score, class_id = map(float, line.split())

    # Convert float coordinates to integers
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    # Draw the bounding box on the image
    color = (0, 255, 0)  # Green color
    thickness = 2
    cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)

    # Label the class on the image
    label = f"Class: {int(class_id)} Score: {score:.2f}"
    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

# Save the image with bounding boxes and labels
output_image_path = "output_image.jpg"  # Replace with your preferred output image path
cv2.imwrite(output_image_path, image)