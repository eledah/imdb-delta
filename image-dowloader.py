import csv
import os
import requests
import time
from urllib.parse import urlparse
from io import StringIO, BytesIO
from PIL import Image

def extract_imdb_id(url):
    path = urlparse(url).path
    return path.split('/')[2]

def download_image(url, max_retries=5, delay=1):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return BytesIO(response.content)
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(delay)
    print(f"Failed to download after {max_retries} attempts: {url}")
    return None

def resize_and_save_image(image_data, filename, width=100):
    try:
        with Image.open(image_data) as img:
            # Calculate the new height to maintain the aspect ratio
            aspect_ratio = img.height / img.width
            new_height = int(width * aspect_ratio)
            
            # Resize the image
            resized_img = img.resize((width, new_height), Image.LANCZOS)
            
            # Save the resized image
            resized_img.save(filename, 'JPEG')
        print(f"Resized and saved: {filename}")
        return True
    except Exception as e:
        print(f"Error processing image: {e}")
        return False

def download_csv(url):
    response = requests.get(url)
    response.raise_for_status()
    return StringIO(response.text)

def main():
    csv_url = 'https://raw.githubusercontent.com/eledah/imdb-delta/main/output_movie_data.csv'
    output_folder = 'thumbnails'

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    try:
        csv_file = download_csv(csv_url)
    except requests.RequestException as e:
        print(f"Failed to download CSV file: {e}")
        return

    reader = csv.DictReader(csv_file)
    for row in reader:
        imdb_id = extract_imdb_id(row['Link'])
        poster_url = row['poster']
        output_filename = os.path.join(output_folder, f"{imdb_id}.jpg")
        
        if not os.path.exists(output_filename):
            image_data = download_image(poster_url)
            if image_data:
                success = resize_and_save_image(image_data, output_filename)
                if not success:
                    print(f"Skipping {imdb_id} due to image processing failure.")
            else:
                print(f"Skipping {imdb_id} due to download failure.")
        else:
            print(f"Skipping {imdb_id}, image already exists.")

if __name__ == "__main__":
    main()