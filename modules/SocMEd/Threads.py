import os
import yt_dlp
import requests
from bs4 import BeautifulSoup
import base64

# Define the output directories
VIDEO_OUTPUT_DIR = './Out/Threads/videos/'
PHOTO_OUTPUT_DIR = './Out/Threads/images/'

# Ensure output directories exist
os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)
os.makedirs(PHOTO_OUTPUT_DIR, exist_ok=True)

def download_threads_video(url):
    """Download Threads video using yt-dlp."""
    print(f"Downloading Threads video: {url}")
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(VIDEO_OUTPUT_DIR, '%(title)s.%(ext)s')
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Threads video download complete!")

def download_threads_photos(url):
    """Download all images from a Threads post containing multiple photos."""
    print(f"Downloading photos from: {url}")

    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the picture tags with the specific class
        picture_tags = soup.find_all('picture', class_='x87ps6o')

        # Find all image tags nested within the picture tags
        img_tags = []
        for picture in picture_tags:
            img = picture.find('img', class_='xmz0i5r')
            if img:
                img_tags.append(img)

        if not img_tags:
            print("No images found on this page.")
            return

        # Download each image
        for idx, img in enumerate(img_tags):
            img_src = img.get('src')

            if img_src.startswith('data:image/'):
                # Handle base64 encoded images
                header, base64_data = img_src.split(',', 1)
                img_data = base64.b64decode(base64_data)

                img_output = os.path.join(PHOTO_OUTPUT_DIR, f'thread_image_{idx+1}.jpg')
                with open(img_output, 'wb') as f:
                    f.write(img_data)
                print(f"Downloaded base64 image {idx+1}: {img_output}")
            else:
                # Regular image URL
                img_response = requests.get(img_src, stream=True)

                if img_response.status_code == 200:
                    img_output = os.path.join(PHOTO_OUTPUT_DIR, f'thread_image_{idx+1}.jpg')
                    with open(img_output, 'wb') as f:
                        for chunk in img_response:
                            f.write(chunk)
                    print(f"Downloaded image {idx+1}: {img_src}")
                else:
                    print(f"Failed to download image {idx+1}: {img_src}")

        print("All photos downloaded!")
    except Exception as e:
        print(f"Error downloading photos: {e}")
