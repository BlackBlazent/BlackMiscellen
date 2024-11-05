import os
import yt_dlp
import requests

# Define output directories
VIDEO_OUTPUT_DIR = './Out/Twitter/videos/'
AUDIO_OUTPUT_DIR = './Out/Twitter/audio/'
GIF_OUTPUT_DIR = './Out/Twitter/gifs/'
IMAGE_OUTPUT_DIR = './Out/Twitter/images/'

# Ensure output directories exist
os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(GIF_OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGE_OUTPUT_DIR, exist_ok=True)

def download_twitter_video(url):
    """Download Twitter video."""
    print(f"Downloading Twitter video: {url}")
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(VIDEO_OUTPUT_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',  # Change to desired format
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Twitter video download complete!")

def download_twitter_audio(url):
    """Download audio from Twitter video."""
    print(f"Downloading Twitter audio: {url}")
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
    print("Twitter audio download complete!")

def download_twitter_gifs(url):
    """Download GIFs from Twitter."""
    print(f"Downloading Twitter GIFs: {url}")
    # Assuming the GIF is embedded in the post or a video format
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(GIF_OUTPUT_DIR, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Twitter GIF download complete!")

def download_twitter_images(url):
    """Download images from Twitter."""
    print(f"Downloading Twitter images: {url}")
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()

        # Extract image URLs (this is a placeholder; implement your logic)
        # Here, you might want to use BeautifulSoup to parse the page content.

        # Example URLs, replace this logic with actual extraction
        image_urls = ['https://example.com/image1.jpg', 'https://example.com/image2.jpg']

        for idx, img_url in enumerate(image_urls):
            img_response = requests.get(img_url, stream=True)
            if img_response.status_code == 200:
                img_output = os.path.join(IMAGE_OUTPUT_DIR, f'twitter_image_{idx+1}.jpg')
                with open(img_output, 'wb') as f:
                    for chunk in img_response:
                        f.write(chunk)
                print(f"Downloaded image {idx+1}: {img_url}")
            else:
                print(f"Failed to download image {idx+1}: {img_url}")

        print("All Twitter images downloaded!")
    except Exception as e:
        print(f"Error downloading images: {e}")
