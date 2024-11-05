import os
import json
import re
from pydantic_core import Url
import yt_dlp  # For downloading specific media (videos, audio, photos)
import instaloader

# Global variables
credentials = None  # Declare the credentials variable globally

def setup_instaloader():
    L = instaloader.Instaloader()
    print("Instaloader instance created successfully.")
    return L

# Define output directories for each content type
OUTPUT_DIR = './Out/Instagram'
AUDIO_OUTPUT_DIR = os.path.join(OUTPUT_DIR, 'audio')
VIDEO_OUTPUT_DIR = os.path.join(OUTPUT_DIR, 'videos')
PHOTO_OUTPUT_DIR = os.path.join(OUTPUT_DIR, 'images')
SAVED_OUTPUT_DIR = os.path.join(OUTPUT_DIR, 'saved')
STORY_OUTPUT_DIR = os.path.join(OUTPUT_DIR, 'story')
HIGHLIGHTS_OUTPUT_DIR = os.path.join(OUTPUT_DIR, 'highlights')
ACCOUNTS_OUTPUT_DIR = os.path.join(OUTPUT_DIR, 'accounts')

# Ensure output directories exist
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(VIDEO_OUTPUT_DIR, exist_ok=True)
os.makedirs(PHOTO_OUTPUT_DIR, exist_ok=True)
os.makedirs(SAVED_OUTPUT_DIR, exist_ok=True)
os.makedirs(STORY_OUTPUT_DIR, exist_ok=True)
os.makedirs(HIGHLIGHTS_OUTPUT_DIR, exist_ok=True)
os.makedirs(ACCOUNTS_OUTPUT_DIR, exist_ok=True)

# Path to store Instagram user credentials
INSTAGRAM_DETAILS_PATH = '../../App/data/auth/instaloader/instagram.details.json'
FFMPEG_LOCATION = './App/embedded/ffmpeg/Windows/bin/'
SESSION_FILE_PATH = '../../App/data/auth/instaloader/session-your_username'

# Load Instagram credentials globally
credentials_dir = os.path.dirname(INSTAGRAM_DETAILS_PATH)
os.makedirs(credentials_dir, exist_ok=True)

def load_instagram_credentials():
    """Load Instagram login details from JSON file."""
    global credentials
    if credentials is None:
        try:
            with open(INSTAGRAM_DETAILS_PATH, 'r') as f:
                credentials = json.load(f)
        except FileNotFoundError:
            print("Instagram credentials not found! Please set your email and password.")
    return credentials

def save_instagram_credentials(email, mobile, password):
    """Save Instagram login details to JSON file."""
    # Check if the credentials directory exists
    if not os.path.exists(credentials_dir):
        os.makedirs(credentials_dir)  # Create it if it does not exist

    global credentials  # Use the global variable
    credentials = {
        "email": email,
        "mobile": mobile,
        "password": password
    }
    with open(INSTAGRAM_DETAILS_PATH, 'w') as f:
        json.dump(credentials, f)
    print("Instagram credentials saved successfully!")

def setup_ydl_opts(outtmpl, format='bestvideo+bestaudio/best'):
    """Setup yt-dlp options, including authentication if credentials are available."""
    ydl_opts = {
        'ffmpeg_location': FFMPEG_LOCATION,
        'format': format,
        'outtmpl': outtmpl,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'cookiefile': 'cookies.txt',  # Load cookies if needed
        'noplaylist': True,
        'verbose': True,
        'write_pages': True,  # Add this line to write pages
    }

    # Load credentials
    creds = load_instagram_credentials()
    if creds and not os.path.exists('cookies.txt'):
        ydl_opts.update({
            'username': creds['email'],
            'password': creds['password'],
            'twofactor': creds['mobile'],
        })

    return ydl_opts

def download_instagram_video(url):
    """Download Instagram video."""
    if not os.path.exists(VIDEO_OUTPUT_DIR):
        os.makedirs(VIDEO_OUTPUT_DIR)

    ydl_opts = setup_ydl_opts(os.path.join(VIDEO_OUTPUT_DIR, '%(title)s.%(ext)s'))
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading Instagram video from: {url}")
        try:
            ydl.download([url])
            print("Instagram video download complete!")
        except Exception as e:
            print(f"An error occurred while downloading video: {e}")

def download_instagram_audio(url):
    """Download Instagram audio as MP3."""
    ydl_opts = setup_ydl_opts(os.path.join(AUDIO_OUTPUT_DIR, '%(title)s.%(ext)s'), 'bestaudio/best')
    ydl_opts['postprocessors'] = [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading Instagram audio from: {url}")
        try:
            ydl.download([url])
            print("Instagram audio download complete!")
        except Exception as e:
            print(f"An error occurred while downloading audio: {e}")

def download_instagram_photos(url):
    """Download Instagram photos."""
    ydl_opts = {
        'outtmpl': os.path.join(PHOTO_OUTPUT_DIR, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'verbose': True,
        'cookiefile': 'cookies.txt'  # Include this if needed
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading Instagram photos from: {url}")
        try:
            ydl.download([url])
            print("Instagram photos download complete!")
        except Exception as e:
            print(f"An error occurred while downloading photos: {e}")

def extract_username(url):
    """Extracts the username from a full Instagram profile URL."""
    match = re.search(r"instagram\.com/([A-Za-z0-9_.]+)", url)
    return match.group(1) if match else None

def setup_instaloader(login=False):
    """Initialize instaloader instance, with optional session login."""
    L = instaloader.Instaloader()

    # Define session path for login session persistence
    session_file = SESSION_FILE_PATH.replace('your_username', L.context.username or 'default')

    # Try loading the session from file
    try:
        L.load_session_from_file(L.context.username or 'default', filename=session_file)
        print("Session loaded successfully.")
    except FileNotFoundError:
        print("No session file found. Please login to create a new session.")
        if login:  # If login is requested, prompt for credentials
            creds = load_instagram_credentials()  # Changed from credentials to creds
            if creds:
                try:
                    L.login(creds['email'], creds['password'])
                    L.save_session_to_file(filename=session_file)  # Save the new session
                    print("New session saved.")
                except instaloader.exceptions.BadCredentialsException:
                    print("Login error: Incorrect email or password.")
                except Exception as e:
                    print(f"An unexpected error occurred during login: {e}")
            else:
                print("Instagram credentials are missing.")

    return L

def download_instagram_profile(profile_url, is_private):
    """Download all profile content using instaloader."""
    profile_name = extract_username(profile_url)  # Extract profile name from URL
    L = setup_instaloader(login=is_private)  # Only login if the profile is private
    print(f"Downloading all content from profile: {profile_name}...")
    try:
        L.download_profile(profile_name, profile_pic=True, fast_update=True)
        print("Profile content download complete.")
    except Exception as e:
        print(f"An error occurred while downloading profile content: {e}")

def download_instagram_stories(profile_name):
    """Download Instagram stories, requiring login if the profile is private."""
    L = setup_instaloader(login=True)  # Ensure login is done
    print(f"Downloading stories from profile: {profile_name}...")
    try:
        profile = instaloader.Profile.from_username(L.context, profile_name)
        L.download_stories(userids=[profile.userid], filename_target=f"{STORY_OUTPUT_DIR}/{profile_name}")
        print("Stories download complete.")
    except instaloader.exceptions.LoginRequiredException:
        print("Error: Login required. Please check credentials.")
    except Exception as e:
        print(f"An error occurred while downloading stories: {e}")

def download_instagram_highlights(profile_name):
    """Download Instagram highlights."""
    L = setup_instaloader()
    print(f"Downloading highlights from profile: {profile_name}...")
    try:
        L.download_highlights(profile_name)
        print("Highlights download complete.")
    except Exception as e:
        print(f"An error occurred while downloading highlights: {e}")

def download_instagram_saved(profile_name):
    """Download saved posts."""
    L = setup_instaloader()
    print(f"Downloading saved posts from profile: {profile_name}...")
    try:
        L.download_saved_posts(profile_name)
        print("Saved posts download complete.")
    except Exception as e:
        print(f"An error occurred while downloading saved posts: {e}")

# Main script logic
if __name__ == "__main__":
    profile_url = input("Enter the Instagram profile URL: ")
    is_private = input("Is the profile private? (y/n): ").strip().lower() == 'y'

    # Wrapping the main logic in a try-except block
    try:
        download_instagram_profile(profile_url, is_private)
        download_instagram_stories(extract_username(profile_url))
        download_instagram_highlights(extract_username(profile_url))
        download_instagram_saved(extract_username(profile_url))
    except Exception as e:
        print(f"An error occurred in the main script: {e}")

