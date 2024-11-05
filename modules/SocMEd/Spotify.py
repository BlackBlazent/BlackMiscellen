import os
import json
import subprocess
from time import sleep

# Define output directories
AUDIO_OUTPUT_DIR = './Out/Spotify/audio/'
PODCAST_OUTPUT_DIR = './Out/Spotify/podcast/'

# Ensure output directories exist
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(PODCAST_OUTPUT_DIR, exist_ok=True)

API_FILE = '../../App/data/api/spotify.api.json'

def get_spotify_api_key(new_key=None):
    """Fetch or update the Spotify API key."""
    os.makedirs(os.path.dirname(API_FILE), exist_ok=True)

    if new_key:
        with open(API_FILE, 'w') as f:
            json.dump({'api': new_key}, f)
    else:
        try:
            with open(API_FILE, 'r') as f:
                data = json.load(f)
                return data.get('api', None)
        except FileNotFoundError:
            return None

def download_with_spotify_dl(url, output_dir):
    """Download content using spotify-dl."""
    print(f"Downloading with spotify-dl for: {url}")
    try:
        subprocess.run(["spotify-dl", url, "-o", output_dir], check=True)
        print("spotify-dl download complete!")
    except subprocess.CalledProcessError as e:
        print(f"spotify-dl download failed: {e}")

def download_spotify_audio(url, api_key=None):
    """Download Spotify audio using spotify-dl."""
    print(f"Downloading Spotify audio with spotify-dl: {url}")
    download_with_spotify_dl(url, AUDIO_OUTPUT_DIR)

def download_spotify_playlist(url, api_key=None):
    """Download Spotify playlist using spotify-dl."""
    print(f"Downloading Spotify playlist with spotify-dl: {url}")
    download_with_spotify_dl(url, AUDIO_OUTPUT_DIR)

def download_spotify_podcast(url, api_key=None):
    """Download Spotify podcast with spotify-dl."""
    print(f"Downloading Spotify podcast with spotify-dl: {url}")
    download_with_spotify_dl(url, PODCAST_OUTPUT_DIR)
