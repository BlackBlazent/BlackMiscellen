'''
import os
import yt_dlp  # For downloading YouTube videos and audio
import time  # To add delay before retrying failed downloads

# Define the output directories
AUDIO_OUTPUT_DIR = './Out/YouTube/audio/'
VIDEO_OUTPUT_DIR = './Out/YouTube/video/'

# Ensure output directories exist
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)

# Path to FFmpeg
FFMPEG_LOCATION = './App/embedded/ffmpeg/Windows/bin/ffmpeg.exe'  # Ensure this points to ffmpeg.exe

# List to keep track of failed downloads
failed_downloads = []

def download_youtube_video(url, retry=False):
    """Download YouTube video."""
    ydl_opts = {
        'ffmpeg_location': FFMPEG_LOCATION,  # Set FFmpeg location
        'format': 'bestvideo+bestaudio/best',  # Best video and audio
        'outtmpl': os.path.join(VIDEO_OUTPUT_DIR, '%(title)s.%(ext)s'),  # Save to specified folder
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"{'Retrying' if retry else 'Downloading'} video from: {url}")
            ydl.download([url])
            print("Download complete!")
    except yt_dlp.utils.DownloadError as e:
        print(f"Download failed for {url}: {e}. The video may lack a transcript or have download restrictions.")
        failed_downloads.append(url)
    except Exception as e:
        print(f"An unexpected error occurred for {url}: {e}")
        failed_downloads.append(url)

def download_youtube_audio(url, retry=False):
    """Download YouTube audio."""
    ydl_opts = {
        'ffmpeg_location': FFMPEG_LOCATION,  # Set FFmpeg location
        'format': 'bestaudio/best',  # Best audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '192',  # Set the audio quality
        }],
        'outtmpl': os.path.join(AUDIO_OUTPUT_DIR, '%(title)s.%(ext)s'),  # Save to specified folder
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"{'Retrying' if retry else 'Downloading'} audio from: {url}")
            ydl.download([url])
            print("Download complete!")
    except yt_dlp.utils.DownloadError as e:
        print(f"Download failed for {url}: {e}. The video may lack a transcript or have download restrictions.")
        failed_downloads.append(url)
    except Exception as e:
        print(f"An unexpected error occurred for {url}: {e}")
        failed_downloads.append(url)

def retry_failed_downloads():
    """Retry all failed downloads."""
    if failed_downloads:
        print("Retrying failed downloads...")
        for url in failed_downloads[:]:
            time.sleep(2)  # Optional delay before retrying
            if "audio" in url:  # Example: Distinguish between audio/video (modify as needed)
                download_youtube_audio(url, retry=True)
            else:
                download_youtube_video(url, retry=True)
            failed_downloads.remove(url)
        print("Retry attempts complete.")

'''

import os
import yt_dlp  # For downloading YouTube videos and audio
import time  # To add delay before retrying failed downloads

# Define the output directories
AUDIO_OUTPUT_DIR = './Out/YouTube/audio/'
VIDEO_OUTPUT_DIR = './Out/YouTube/video/'

# Ensure output directories exist
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)

# Path to FFmpeg
FFMPEG_LOCATION = './App/embedded/ffmpeg/Windows/bin/ffmpeg.exe'  # Ensure this points to ffmpeg.exe

# List to keep track of failed downloads
failed_downloads = []

def download_youtube_video(url, retry=False):
    """Download YouTube video."""
    ydl_opts = {
        'ffmpeg_location': FFMPEG_LOCATION,  # Set FFmpeg location
        'format': 'bestvideo+bestaudio/best',  # Best video and audio
        'outtmpl': os.path.join(VIDEO_OUTPUT_DIR, '%(title)s.%(ext)s'),  # Save to specified folder
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"{'Retrying' if retry else 'Downloading'} video from: {url}")
            ydl.download([url])
            print("Download complete!")
    except yt_dlp.utils.DownloadError as e:
        print(f"Download failed for {url}: {e}. The video may lack a transcript or have download restrictions.")
        failed_downloads.append(url)
    except Exception as e:
        print(f"An unexpected error occurred for {url}: {e}")
        failed_downloads.append(url)

def download_youtube_audio(url, retry=False):
    """Download YouTube audio."""
    ydl_opts = {
        'ffmpeg_location': FFMPEG_LOCATION,  # Set FFmpeg location
        'format': 'bestaudio/best',  # Best audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '192',  # Set the audio quality
        }],
        'outtmpl': os.path.join(AUDIO_OUTPUT_DIR, '%(title)s.%(ext)s'),  # Save to specified folder
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"{'Retrying' if retry else 'Downloading'} audio from: {url}")
            ydl.download([url])
            print("Download complete!")
    except yt_dlp.utils.DownloadError as e:
        print(f"Download failed for {url}: {e}. The video may lack a transcript or have download restrictions.")
        failed_downloads.append(url)
    except Exception as e:
        print(f"An unexpected error occurred for {url}: {e}")
        failed_downloads.append(url)

def retry_failed_downloads():
    """Retry all failed downloads."""
    if failed_downloads:
        print("Retrying failed downloads...")
        for url in failed_downloads[:]:
            time.sleep(2)  # Optional delay before retrying
            if "audio" in url:  # Example: Distinguish between audio/video (modify as needed)
                download_youtube_audio(url, retry=True)
            else:
                download_youtube_video(url, retry=True)
            failed_downloads.remove(url)
        print("Retry attempts complete.")

# Example usage
urls = [
    "https://www.youtube.com/watch?v=example1",
    "https://www.youtube.com/watch?v=example2",
    # Add more URLs here
]

# Download all videos
for url in urls:
    download_youtube_video(url)

# Retry any failed downloads
retry_failed_downloads()
