import pandas as pd
import os

def convert_to_yolo_format(df, output_dir):
    for idx, row in df.iterrows():
        filename = row['filename']
        width, height = row['width'], row['height']
        class_name = row['class']
        xmin, ymin, xmax, ymax = row['xmin'], row['ymin'], row['xmax'], row['ymax']
        if class_name == '.':
            class_name = '10'
        # Calculate YOLO format coordinates (normalized)
        x_center = (xmin + xmax) / (2 * width)
        y_center = (ymin + ymax) / (2 * height)
        bbox_width = (xmax - xmin) / width
        bbox_height = (ymax - ymin) / height

        # Create YOLO format string
        yolo_line = f"{class_name} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}"

        # Write to YOLO text file
        yolo_filename = os.path.join(output_dir, filename.replace('.jpg', '.txt'))

        # Check if the file already exists
        if os.path.exists(yolo_filename):
            with open(yolo_filename, 'a') as yolo_file:
                yolo_file.write('\n' + yolo_line)
        else:
            with open(yolo_filename, 'w') as yolo_file:
                yolo_file.write(yolo_line)

# Load CSV file into a pandas DataFrame
csv_file_path = 'Data/valid/labels/valid_annotations.csv'
df = pd.read_csv(csv_file_path)

# Specify the output directory for YOLO files
output_directory = 'Data/valid/labels'

# Create YOLO-compatible text files
convert_to_yolo_format(df, output_directory)