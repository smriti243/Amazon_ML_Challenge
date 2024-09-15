import os
from PIL import Image
import numpy as np

# Directory paths
input_dir = '../images'
output_dir = '../processed_images'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

def preprocess_image(image_path, output_path):
    try:
        with Image.open(image_path) as img:
            # Resize the image (example size: 224x224)
            img = img.resize((224, 224))
            
            # Normalize the image (example normalization)
            img_array = np.array(img) / 255.0
            
            # Convert back to image
            img = Image.fromarray((img_array * 255).astype(np.uint8))
            
            # Save the processed image
            img.save(output_path)
            print(f"Processed and saved: {output_path}")
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

# Process all images in the input directory
for filename in sorted(os.listdir(input_dir)):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Adjust based on your image formats
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        preprocess_image(input_path, output_path)

print("Preprocessing complete.")
