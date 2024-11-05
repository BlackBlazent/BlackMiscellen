import os
import yt_dlp
import ffmpeg
import requests
from bs4 import BeautifulSoup

# Define output directories
VIDEO_OUTPUT_DIR = './Out/Snapchat/videos/'
AUDIO_OUTPUT_DIR = './Out/Snapchat/audio/'
PHOTO_OUTPUT_DIR = './Out/Snapchat/images/'

# Ensure output directories exist
os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(PHOTO_OUTPUT_DIR, exist_ok=True)

def download_snapchat_video(url):
    """Download Snapchat video (including Reels and Spotlight)."""
    print(f"Downloading Snapchat video: {url}")
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(VIDEO_OUTPUT_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',  # Change to desired format
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Snapchat video download complete!")

def download_snapchat_audio(url):
    """Download audio from Snapchat video or Reels."""
    print(f"Downloading Snapchat audio: {url}")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(AUDIO_OUTPUT_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Snapchat audio download complete!")

def download_snapchat_photos(url):
    """Download all photos from Snapchat Story or Post."""
    print(f"Downloading Snapchat photos: {url}")
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all image URLs (assuming image URLs are in <img> tags)
        img_tags = soup.find_all('img')

        if not img_tags:
            print("No images found on this page.")
            return

        # Download each image
        for idx, img in enumerate(img_tags):
            img_url = img['src']
            img_response = requests.get(img_url, stream=True)

            if img_response.status_code == 200:
                img_output = os.path.join(PHOTO_OUTPUT_DIR, f'snapchat_image_{idx+1}.jpg')
                with open(img_output, 'wb') as f:
                    for chunk in img_response:
                        f.write(chunk)
                print(f"Downloaded image {idx+1}: {img_url}")
            else:
                print(f"Failed to download image {idx+1}: {img_url}")

        print("All Snapchat photos downloaded!")
    except Exception as e:
        print(f"Error downloading photos: {e}")

def remove_watermark(input_file, output_file):
    """Use ffmpeg to remove watermark from a video."""
    print(f"Removing watermark from {input_file}...")
    
    # Example coordinates for watermark removal, adjust as needed
    ffmpeg.input(input_file).output(output_file, vf='delogo=x=10:y=10:w=100:h=100').run()
    
    print(f"Watermark removed, saved to {output_file}")
