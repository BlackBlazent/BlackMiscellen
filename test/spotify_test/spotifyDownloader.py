import os
import json
import subprocess

# Define output directories
AUDIO_OUTPUT_DIR = '../../Out/Spotify/audio/'
PODCAST_OUTPUT_DIR = '../../Out/Spotify/podcast/'

# Path to FFmpeg
FFMPEG_LOCATION = os.path.abspath('../../App/embedded/ffmpeg/Windows/bin/ffmpeg.exe')  # Ensure this points to ffmpeg.exe
FFPROBE_LOCATION = os.path.abspath('../../App/embedded/ffmpeg/Windows/bin/ffprobe.exe')  # Ensure this points to ffprobe.exe

# Ensure output directories exist
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(PODCAST_OUTPUT_DIR, exist_ok=True)

API_FILE = '../../App/data/api/spotifyAPI.json'

def get_spotify_api_keys():
    """Fetch the Spotify API keys from the JSON file."""
    os.makedirs(os.path.dirname(API_FILE), exist_ok=True)

    try:
        with open(API_FILE, 'r') as f:
            data = json.load(f)
            client_id = data.get('client_id', None)
            client_secret = data.get('client_secret', None)
            return client_id, client_secret
    except FileNotFoundError:
        return None, None

def set_env_variables():
    """Set the Spotify API credentials and FFmpeg location as environment variables."""
    client_id, client_secret = get_spotify_api_keys()
    if client_id and client_secret:
        os.environ['SPOTIPY_CLIENT_ID'] = client_id
        os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret

    # Set the FFMPEG_BINARY environment variable to the FFmpeg executable path
    os.environ['FFMPEG_BINARY'] = FFMPEG_LOCATION

def download_with_spotify_dl(url, output_dir):
    """Download content using spotify_dl."""
    print(f"Downloading with spotify_dl for: {url}")
    try:
        # Prepare the command with --ffmpeg-location argument
        command = [
            "spotify_dl",
            "-l", url,
            "-o", output_dir,
            "--ffmpeg-location", FFMPEG_LOCATION  # Add this line to specify ffmpeg location
        ]
        subprocess.run(command, check=True)
        print("Download complete!")
    except subprocess.CalledProcessError as e:
        print(f"Download failed: {e}")

def handle_download(url, download_func):
    """Handles the download process and error management."""
    try:
        download_func(url)
    except Exception as e:
        print(f"Error downloading: {e}")
        prompt_for_api_key(url, download_func.__name__)

def prompt_for_api_key(url, download_type):
    """Prompt the user to input an API key and retry the download."""
    retry = input("Error when downloading. Would you like to provide a Spotify API key? (y/n): ")
    if retry.lower() == 'y':
        new_client_id = input("Enter your Spotify Client ID: ")
        new_client_secret = input("Enter your Spotify Client Secret: ")
        save_spotify_api_keys(new_client_id, new_client_secret)  # Save the new keys
        set_env_variables()  # Set the new keys as environment variables

        # Retry download with updated API keys
        retry_download(download_type, url)

def save_spotify_api_keys(client_id, client_secret):
    """Save the Spotify API keys to the JSON file."""
    with open(API_FILE, 'w') as f:
        json.dump({'client_id': client_id, 'client_secret': client_secret}, f)

def retry_download(download_type, url):
    """Retry the download with the updated API key."""
    if download_type == 'download_spotify_playlist':
        download_spotify_playlist(url)
    elif download_type == 'download_spotify_audio':
        download_spotify_audio(url)
    elif download_type == 'download_spotify_podcast':
        download_spotify_podcast(url)
    else:
        print("Unknown download type.")

def download_spotify_audio(url):
    """Download Spotify audio using spotify_dl."""
    print(f"Downloading Spotify audio: {url}")
    set_env_variables()  # Ensure environment variables are set before downloading
    download_with_spotify_dl(url, AUDIO_OUTPUT_DIR)

def download_spotify_playlist(url):
    """Download Spotify playlist using spotify_dl."""
    print(f"Downloading Spotify playlist: {url}")
    set_env_variables()  # Ensure environment variables are set before downloading
    download_with_spotify_dl(url, AUDIO_OUTPUT_DIR)

def download_spotify_podcast(url):
    """Download Spotify podcast using spotify_dl."""
    print(f"Downloading Spotify podcast: {url}")
    set_env_variables()  # Ensure environment variables are set before downloading
    download_with_spotify_dl(url, PODCAST_OUTPUT_DIR)
