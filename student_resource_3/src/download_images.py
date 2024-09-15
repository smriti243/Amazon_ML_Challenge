import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import os

# Load the dataset
df = pd.read_csv('dataset/train.csv')

# Sample function to download images from URLs
def download_image(url, save_path):
    try:
        response = requests.get(url, timeout=10)  # Add timeout to handle slow servers
        response.raise_for_status()  # Raise an exception for HTTP errors
        img = Image.open(BytesIO(response.content))
        img.save(save_path)
    except requests.exceptions.RequestException as e:
        print(f"Request error for URL {url}: {e}")
        return False
    except Image.UnidentifiedImageError:
        print(f"UnidentifiedImageError: Could not identify image file from URL {url}")
        return False
    except Exception as e:
        print(f"Error processing image from URL {url}: {e}")
        return False
    return True

# Ensure the images directory exists
os.makedirs('images', exist_ok=True)

# Iterate over the dataframe and use the DataFrame's index for the file name
for i, row in df.iterrows():
    image_url = row['image_link']  # Assuming 'image_link' is the column for image URLs
    save_path = f'images/{i}.jpg'  # Using the DataFrame index as the file name
    if not download_image(image_url, save_path):
        print(f"Skipping index {i} due to an error.")
