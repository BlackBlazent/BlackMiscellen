import os
import yt_dlp
import subprocess

# Define the output directories
VIDEO_OUTPUT_DIR = './Out/TikTok/videos/'
AUDIO_OUTPUT_DIR = './Out/TikTok/audio/'

# Ensure output directories exist
os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)

# Path to FFmpeg
FFMPEG_LOCATION = './App/embedded/ffmpeg/Windows/bin/'


def download_tiktok_video(url):
    """Download TikTok video without a watermark."""
    # Step 1: Download the video using yt_dlp
    ydl_opts = {
        'ffmpeg_location': FFMPEG_LOCATION,
        'format': 'bestvideo+bestaudio/best',  # Get the best video and audio quality
        'outtmpl': os.path.join(VIDEO_OUTPUT_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',  # Use FFmpegVideoRemuxer instead of FFmpegVideoConvertor
            #'ext': 'mp4',  # Convert video to MP4 format
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading TikTok video from: {url}")
        video_info = ydl.extract_info(url, download=True)
        video_path = ydl.prepare_filename(video_info)

    # Step 2: Remove the watermark using FFmpeg
    remove_watermark_ffmpeg(video_path)



def remove_watermark_ffmpeg(input_video_path):
    """Remove TikTok watermark by cropping using FFmpeg."""
    output_video_path = input_video_path.replace('.mp4', '_no_watermark.mp4')

    # FFmpeg cropping command to remove TikTok watermark
    # This example crops a 10px margin on all sides, adjust based on the watermark position
    ffmpeg_command = [
        os.path.join(FFMPEG_LOCATION, 'ffmpeg'),
        '-i', input_video_path,  # Input file
        '-vf', 'crop=in_w-20:in_h-20',  # Cropping to remove watermark (adjust as needed)
        '-c:a', 'copy',  # Copy audio without re-encoding
        output_video_path
    ]

    print(f"Running FFmpeg to remove watermark from {input_video_path}...")
    subprocess.run(ffmpeg_command)

    print(f"Watermark removed! Saved as {output_video_path}")


def download_tiktok_audio(url):
    """Download TikTok audio (only)."""
    ydl_opts = {
        'ffmpeg_location': FFMPEG_LOCATION,
        'format': 'bestaudio/best',  # Get the best audio quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract audio
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(AUDIO_OUTPUT_DIR, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading TikTok audio from: {url}")
        ydl.download([url])
        print("TikTok audio download complete!")
