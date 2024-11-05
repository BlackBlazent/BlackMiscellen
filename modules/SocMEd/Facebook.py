import os
import json
import yt_dlp  # For downloading Facebook videos and audio

# Define the output directories
AUDIO_OUTPUT_DIR = './Out/Facebook/audio/'
VIDEO_OUTPUT_DIR = './Out/Facebook/videos/'

# Ensure output directories exist
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)

# Path to the JSON file storing Facebook user credentials
FACEBOOK_DETAILS_PATH = './App/data/facebook.details.json'

# Path to FFmpeg
FFMPEG_LOCATION = './App/embedded/ffmpeg/Windows/bin/'

def load_facebook_credentials():
    """Load Facebook login details from the JSON file."""
    try:
        with open(FACEBOOK_DETAILS_PATH, 'r') as f:
            credentials = json.load(f)
        return credentials
    except FileNotFoundError:
        print("Facebook credentials not found! Please set your email, mobile, and password.")
        return None

def save_facebook_credentials(email, mobile, password):
    """Save Facebook login details to the JSON file."""
    credentials = {
        "email": email,
        "mobile": mobile,
        "password": password
    }
    with open(FACEBOOK_DETAILS_PATH, 'w') as f:
        json.dump(credentials, f)
    print("Facebook credentials saved successfully!")

def download_facebook_video(url, use_auth=False):
    """Download Facebook video."""
    ydl_opts = {
        'ffmpeg_location': FFMPEG_LOCATION,  # Set FFmpeg location
        'format': 'bestvideo+bestaudio/best',  # Best video and audio
        'outtmpl': os.path.join(VIDEO_OUTPUT_DIR, '%(title)s.mp4'),  # Save as MP4 directly
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',  # Use FFmpeg to remux video to MP4
        }],
        'verbose': True,  # Enable verbose logging
    }

    # If authentication is required
    if use_auth:
        credentials = load_facebook_credentials()
        if credentials:
            ydl_opts.update({
                'username': credentials['email'],  # Add Facebook email
                'password': credentials['password'],  # Add Facebook password
                'twofactor': credentials.get('mobile'),  # Two-factor authentication (if needed)
            })
        else:
            print("No credentials found. Unable to download private content.")
            return

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading Facebook video from: {url}")
        ydl.download([url])
        print("Facebook video download complete!")


def download_facebook_audio(url, use_auth=False):
    """Download Facebook audio."""
    ydl_opts = {
        'ffmpeg_location': FFMPEG_LOCATION,  # Set FFmpeg location
        'format': 'bestaudio/best',  # Best audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(AUDIO_OUTPUT_DIR, '%(title)s.%(ext)s'),  # Save to specified folder
    }

    # If authentication is required
    if use_auth:
        credentials = load_facebook_credentials()
        if credentials:
            ydl_opts.update({
                'username': credentials['email'],  # Add Facebook email
                'password': credentials['password'],  # Add Facebook password
                'twofactor': credentials.get('mobile'),  # Two-factor authentication (if needed)
            })
        else:
            print("No credentials found. Unable to download private content.")
            return

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading Facebook audio from: {url}")
        ydl.download([url])
        print("Facebook audio download complete!")

