import os
import json
from src.banner import banner # Import the print_banner function from banner.py
from modules.SocMEd.YouTube import download_youtube_video, download_youtube_audio  # Import YouTube functions
from modules.SocMEd.Facebook import download_facebook_video, download_facebook_audio, save_facebook_credentials  # Facebook functions
from modules.SocMEd.Instagram import download_instagram_video, download_instagram_audio, download_instagram_photos, save_instagram_credentials  # Instagram functions
from modules.SocMEd.TikTok import download_tiktok_video, download_tiktok_audio  # Import TikTok functions
from modules.SocMEd.Pinterest import download_pinterest_video, download_pinterest_photos  # Pinterest functions
from modules.SocMEd.Spotify import download_spotify_audio, download_spotify_playlist, get_spotify_api_key  # Spotify functions
from modules.SocMEd.Threads import download_threads_video, download_threads_photos  # Threads functions
from modules.SocMEd.Snapchat import download_snapchat_video, download_snapchat_audio, download_snapchat_photos, remove_watermark  # Snapchat functions
from modules.SocMEd.Twitter import download_twitter_video, download_twitter_audio, download_twitter_gifs, download_twitter_images  # Twitter functions

def main():
    banner.start_banner()


def main_menu():
    while True:
        print("Welcome to BlackDownloader!")
        print("1. Download from YouTube")
        print("2. Download from Facebook")  # Video & Audio
        print("3. Download from X (Twitter)")  # Video & Audio
        print("4. Download from Spotify")  # Video & Audio
        print("5. Download from Threads")  # Video only
        print("6. Download from Instagram")  # Video, Audio, Photos
        print("7. Download from Pinterest")  # Video & Photos
        print("8. Download from TikTok")  # Video & Audio
        print("9. Download from Snapchat")  # Video, Audio, Photos
        print("10. Update BlackDownloader. Visit (https://github.com/LoneStamp/BlackDownloader) for more info.")
        print("11. Langauge") # For langauge translation
        print("12. Help")
        print("13. Exit")

        choice = input("Please select Platforms (1-10): ")

        if choice == '1':
            youtube_menu()  # Move to YouTube download selection
        elif choice == '2':
            facebook_menu()  # Facebook download selection
        elif choice == '3':
            twitter_menu()  # Twitter (X) download selection
        elif choice == '4':
            spotify_menu()  # Spotify download selection
        elif choice == '5':
            threads_menu()  # Threads download selection
        elif choice == '6':
            instagram_menu()  # Instagram download selection
        elif choice == '7':
            pinterest_menu()  # Pinterest download selection
        elif choice == '8':
            tiktok_menu()  # TikTok download selection
        elif choice == '9':
            snapchat_menu()  # Snapchat download selection
        elif choice == '10':
             update() # Update BlackDownloader
        elif choice == '13':
            print("Exiting the program. BlackDownloader!")
            break
        else:
            print("Selection not found. Please choose above.")

# This is YouTube
def youtube_menu():
    while True:
        print("\nYouTube Download Options:")
        print("1. Download YouTube Video")
        print("2. Download YouTube Audio")
        print("3. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the YouTube URL (Video or playlist): ")
            download_youtube_video(url)
            print("Video download completed!")
        elif choice == '2':
            url = input("Enter the YouTube URL (video or playlist): ")
            download_youtube_audio(url)
            print("Audio download completed!")
        elif choice == '3':
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

# This is Facebook
def facebook_menu():
    while True:
        print("\nFacebook Download Options:")
        print("1. Download Facebook Video")
        print("2. Download Facebook Audio")
        print("3. Set Facebook Login Credentials")  # New option to set credentials
        print("4. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the Facebook video Link: ")
            private = input("Is the video private? (y/n): ").lower()
            if private == 'y':
                download_facebook_video(url, use_auth=True)  # Download using authentication
            else:
                download_facebook_video(url)  # Download without authentication
        elif choice == '2':
            url = input("Enter the Facebook audio Link: ")
            private = input("Is the audio private? (y/n): ").lower()
            if private == 'y':
                download_facebook_audio(url, use_auth=True)  # Download using authentication
            else:
                download_facebook_audio(url)  # Download without authentication
        elif choice == '3':
            # Set Facebook credentials
            email = input("Enter your Facebook email: ")
            mobile = input("Enter your two-factor authentication mobile (if applicable): ")
            password = input("Enter your Facebook password: ")
            save_facebook_credentials(email, mobile, password)  # Save credentials to JSON
        elif choice == '4':
            break
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

# This is X
def twitter_menu():
    while True:
        print("\nTwitter (X) Download Options:")
        print("1. Download Twitter Video")
        print("2. Download Twitter Audio")
        print("3. Download Twitter GIFs and Images")
        print("4. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the Twitter video Link: ")
            try:
                download_twitter_video(url)
            except Exception as e:
                print(f"Error downloading Twitter video: {e}")
        elif choice == '2':
            url = input("Enter the Twitter audio Link: ")
            try:
                download_twitter_audio(url)
            except Exception as e:
                print(f"Error downloading Twitter audio: {e}")
        elif choice == '3':
            url = input("Enter the Twitter GIF/Image Link: ")
            try:
                download_twitter_gifs(url)
                download_twitter_images(url)
            except Exception as e:
                print(f"Error downloading Twitter GIFs/Images: {e}")
        elif choice == '4':
            break
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

# This is Spotify
def spotify_menu():
    api_key = get_spotify_api_key()

    while True:
        print("\nSpotify Download Options:")
        print("1. Download Spotify Playlist")
        print("2. Download Spotify Audio")
        print("3. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the Spotify playlist Link: ")
            try:
                download_spotify_playlist(url, api_key)
            except Exception as e:
                print(f"Error downloading playlist: {e}")
                prompt_for_api_key(url, 'playlist')
        elif choice == '2':
            url = input("Enter the Spotify audio Link: ")
            try:
                download_spotify_audio(url, api_key)
            except Exception as e:
                print(f"Error downloading audio: {e}")
                prompt_for_api_key(url, 'audio')
        elif choice == '3':
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

def prompt_for_api_key(url, download_type):
    """Prompt the user to input an API key and retry the download."""
    retry = input("Error when downloading. Would you like to provide a Spotify API key? (y/n): ")
    if retry.lower() == 'y':
        new_api_key = input("Enter your Spotify API key: ")
        save_spotify_api_key(new_api_key)
        
        if download_type == 'playlist':
            download_spotify_playlist(url, new_api_key)
        elif download_type == 'audio':
            download_spotify_audio(url, new_api_key)
    else:
        print("Skipping download...")

def save_spotify_api_key(api_key):
    """Save the Spotify API key to the json file."""
    data = {"api": api_key}
    with open('./App/data/api/spotify.api.json', 'w') as f:
        json.dump(data, f)
    print("API key saved successfully.")

# This is Threads
def threads_menu():
    while True:
        print("\nThreads Download Options:")
        print("1. Download Threads Video")
        print("2. Download Threads Photos")
        print("3. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the Threads video Link: ")
            try:
                download_threads_video(url)
            except Exception as e:
                print(f"Error downloading Threads video: {e}")
        elif choice == '2':
            url = input("Enter the Threads photo post Link: ")
            try:
                download_threads_photos(url)
            except Exception as e:
                print(f"Error downloading Threads photos: {e}")
        elif choice == '3':
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

# This is Instagram
def instagram_menu():
    while True:
        print("\nInstagram Download Options:")
        print("1. Download Instagram Video")
        print("2. Download Instagram Audio")
        print("3. Download Instagram Photos")
        print("4. Set Instagram Login Credentials")  # New option to set credentials
        print("5. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the Instagram video Link: ")
            private = input("Is the video private? (y/n): ").lower()
            if private == 'y':
                download_instagram_video(url, use_auth=True)  # Download using authentication
            else:
                download_instagram_video(url)  # Download without authentication
        elif choice == '2':
            url = input("Enter the Instagram audio Link: ")
            private = input("Is the audio private? (y/n): ").lower()
            if private == 'y':
                download_instagram_audio(url, use_auth=True)  # Download using authentication
            else:
                download_instagram_audio(url)  # Download without authentication
        elif choice == '3':
            url = input("Enter the Instagram photos Link: ")
            private = input("Are the photos private? (y/n): ").lower()
            if private == 'y':
                download_instagram_photos(url, use_auth=True)  # Download using authentication
            else:
                download_instagram_photos(url)  # Download without authentication
        elif choice == '4':
            # Set Instagram credentials
            email = input("Enter your Instagram email: ")
            mobile = input("Enter your two-factor authentication mobile (if applicable): ")
            password = input("Enter your Instagram password: ")
            save_instagram_credentials(email, mobile, password)  # Save credentials to JSON
        elif choice == '5':
            break
        else:
            print("Invalid selection. Please choose 1, 2, 3, 4, or 5.")

# This is Pinterest
def pinterest_menu():
    while True:
        print("\nPinterest Download Options:")
        print("1. Download Pinterest Video")
        print("2. Download Pinterest Photos")
        print("3. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the Pinterest video Link: ")
            download_pinterest_video(url)  # Download Pinterest video
        elif choice == '2':
            url = input("Enter the Pinterest photos Link: ")
            download_pinterest_photos(url)  # Download Pinterest photos
        elif choice == '3':
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

# This is TikTok
def tiktok_menu():
    while True:
        print("\nTikTok Download Options:")
        print("1. Download TikTok Video")
        print("2. Download TikTok Audio")
        print("3. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the TikTok video Link: ")
            download_tiktok_video(url)  # Download TikTok video and remove watermark
        elif choice == '2':
            url = input("Enter the TikTok audio Link: ")
            download_tiktok_audio(url)  # Download TikTok audio
        elif choice == '3':
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

# This is Snapchat
def snapchat_menu():
    while True:
        print("\nSnapchat Download Options:")
        print("1. Download Snapchat Video")
        print("2. Download Snapchat Audio")
        print("3. Download Snapchat Photos")
        print("4. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the Snapchat video Link: ")
            try:
                download_snapchat_video(url)
                # Prompt for watermark removal if required
                remove_watermark_input = input("Do you want to remove the watermark? (yes/no): ").lower()
                if remove_watermark_input == 'yes':
                    input_file = input("Enter the downloaded video file path: ")
                    output_file = input("Enter the output file path (without watermark): ")
                    remove_watermark(input_file, output_file)
            except Exception as e:
                print(f"Error downloading Snapchat video: {e}")
        elif choice == '2':
            url = input("Enter the Snapchat audio Link: ")
            try:
                download_snapchat_audio(url)
            except Exception as e:
                print(f"Error downloading Snapchat audio: {e}")
        elif choice == '3':
            url = input("Enter the Snapchat photos Link: ")
            try:
                download_snapchat_photos(url)
            except Exception as e:
                print(f"Error downloading Snapchat photos: {e}")
        elif choice == '4':
            break
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main_menu()
