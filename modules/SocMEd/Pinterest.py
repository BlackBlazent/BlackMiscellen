import os
import yt_dlp
import requests
from bs4 import BeautifulSoup

# Define the output directories
VIDEO_OUTPUT_DIR = './Out/Pinterest/videos/'
PHOTO_OUTPUT_DIR = './Out/pinterest/image/'

# Define the path to ffmpeg
FFMPEG_PATH = './App/embedded/ffmpeg/Windows/bin/ffmpeg.exe'

# Ensure output directories exist
os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)
os.makedirs(PHOTO_OUTPUT_DIR, exist_ok=True)

def download_pinterest_video(url):
    """Download Pinterest video."""
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(VIDEO_OUTPUT_DIR, '%(title)s.%(ext)s'),
        'ffmpeg_location': FFMPEG_PATH  # Specify the ffmpeg path here
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading Pinterest video from: {url}")
        ydl.download([url])
        print("Pinterest video download complete!")


def download_pinterest_photos(url):
    """Download photos from Pinterest boards or individual posts."""
    print(f"Downloading Pinterest photos from: {url}")
    
    # Get the page content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the Pinterest page: {url}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image URLs (Pinterest images are usually inside <img> tags)
    images = soup.find_all('img')
    
    if not images:
        print("No images found on this page.")
        return

    for i, img in enumerate(images):
        img_url = img.get('src')
        if img_url:
            try:
                download_image(img_url, PHOTO_OUTPUT_DIR, f'pinterest_image_{i}.jpg')
            except Exception as e:
                print(f"Failed to download image {i}: {e}")

    print("Pinterest photo download complete!")


def download_image(url, output_dir, filename):
    """Download an image from a URL."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        image_path = os.path.join(output_dir, filename)
        with open(image_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded image: {filename}")
    else:
        print(f"Failed to download image from {url}")
