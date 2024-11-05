import os
import json
import threading
import time
from datetime import datetime
import signal
from App.settings.theme import color_scheme
from App.settings.locales.arabic_setting import enable_translation, translate_text, load_translations  
import subprocess
import sys
import platform
import re
for i in dir(__builtins__):
    if re.match(r'^[A-Z]', i):
        print(i)

from App.app import generate_random_word, confirm_deletion, delete_file
from src.banners.banner import start_banner, load_banners_from_folder, animate_ascii_art, stop_banner   
from src.book.bible import display_daily_verse

# From Download Modules
from modules.SocMEd.YouTube import download_youtube_video, download_youtube_audio  
from modules.SocMEd.Facebook import download_facebook_video, download_facebook_audio, save_facebook_credentials  
from modules.SocMEd.Instagram import download_instagram_highlights, download_instagram_profile, download_instagram_saved, download_instagram_stories, download_instagram_video, download_instagram_audio, download_instagram_photos, save_instagram_credentials, setup_instaloader  # Instagram functions
from  modules.SocMEd.Instagram import SESSION_FILE_PATH
from modules.SocMEd.TikTok import download_tiktok_video, download_tiktok_audio  
from modules.SocMEd.Pinterest import download_pinterest_video, download_pinterest_photos  
from modules.SocMEd.Spotify import download_spotify_audio, download_spotify_playlist, get_spotify_api_key  
from modules.SocMEd.Threads import download_threads_video, download_threads_photos  
from modules.SocMEd.Snapchat import download_snapchat_video, download_snapchat_audio, download_snapchat_photos, remove_watermark  
from modules.SocMEd.Twitter import download_twitter_video, download_twitter_audio, download_twitter_gifs, download_twitter_images  
from modules.torrent.torrent import download_magnet, download_direct, download_torrent

# langauges
'''
from App.data.locales.arabic
from App.data.locales.french
from App.data.locales.german
from App.data.locales.japanese
from App.data.locales.korean
from App.data.locales.mandarin_chinese
from App.data.locales.portogues
from App.data.locales.russian
from App.data.locales.spanish
from App.data.locales.thailand
'''

def set_executable_permission(file_path):
    """Set execute permissions based on the operating system."""
    current_os = platform.system()

    if current_os == "Linux" or current_os == "Darwin":  # Darwin is macOS
       
        subprocess.run(["chmod", "+x", file_path], check=True)
        print(f"Set executable permissions for {file_path} on {current_os}")
    elif current_os == "Windows":
        print(f"No need to set permissions for {file_path} on Windows")
    else:
        print(f"Operating system {current_os} not recognized for permission setting.")

def run_reader_script():
    """Ensure reader.sh is executable and run it to verify required files and directories."""
    try:
        # Set execute permissions on Unix-like systems (Linux, macOS)
        set_executable_permission("./App/data/reader.sh")

        # Run reader.sh
        result = subprocess.run(["./App/data/reader.sh"], check=True, text=True, capture_output=True, shell=True)
        print(result.stdout)  

    except subprocess.CalledProcessError as e:
        print(f"Error running reader.sh: {e.stderr}")


run_reader_script()

# Main Menu
def main_menu():
    start_banner()
    stop_banner()
    threading.Thread(target=display_daily_verse, daemon=True).start()

    while True:
        print("\n------Welcome to BlackMiscellen! Comprehensive Toolkits.------")
        print("1. Converter (Not Available)")
        print("2. Downloader")
        print("3. OSINT (Not Available)")
        print("4. Langauage Translator (Not Available)")
        print("5. Photos/Videos Filtering (Not Available)")
        print("6. Generation (Not Available)")
        print("7. Settings (Not Available)")
        print("8. Update")
        print("9. Exit")

        choice = input("Select Miscellaneous Tools: ")

        if choice == '1':
            converter_menu()
        elif choice == '2':
            downloader_menu()
        elif choice == '3':
            osint_menu()
        elif choice == '4':
            lang_menu()
        elif choice == '5':
            phovid_menu()
        elif choice == '6':
            generation_menu()
        elif choice == '7':
            settings_menu()
        elif choice == '8':
            update_now()
        elif choice == '9':
            print("Exiting BlackMiscellen...")
            break
        else:
            print("Think thought unto your Heart. Choose her/him wisely!")

# Convertion Menu
'''Start of Convertion Menu'''
def converter_menu():
    while True:
        print("\n------BlackMiscellen: Converter Secton.------")
        print("1. Documents")
        print("2. Images")
        print("3. Videos")
        print("4. Web to Mobile App")
        print("5. Exit")

        choice = input("Select Convertion Options: ")

        if choice == '1':
            document_menu()
        elif choice == '2':
            images_menu()
        elif choice == '3':
            videovert_menu()
        elif choice == '4':
            webApp_menu()
        elif choice == '5':
            print("Exiting Convertion Menu...")
            break
        else:
            print("Invalid selection: Choose 1, 2, 3, 4, or 5: ")

def document_menu():
    while True:
        print("Documents Convertion Section")

def images_menu():
    while True:
        print("Image Convertion Section")
def videovert_menu():
    print("Video COnvertion Section")

def webApp_menu():
    print("Webapp COnvertion Section")
    print("1. IOS")
    print("2. Android")

'''End of Convertion MEnu'''

# Downloader Menu
'''Start of Downloader'''
def downloader_menu():
    while True:
        print("\n------BlackMiscellen: Downloader Sections.------")
        print("1. Torrent (Not Available)")
        print("2. SocMed")
        print("3. Settings")
        print("4. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            torrent_menu()  
        elif choice == '2':
            socmed_menu()  
        elif choice == '3':
            settings_menu()  
        elif choice == '4':
            print("Exiting BlackDownloader.")
            break
        else:
            print("Invalid choice, please select again.")

# For Torrents
def torrent_menu():
    while True:
        print("\n--- Torrent Download Options ---")
        print("1. Magnet Link")
        print("2. Direct Link")
        print("3. Torrent File")
        print("4. Back to Main Menu")

        choice = input("Please select an option (1-4): ")

        if choice == '1':
            magnet_link = input("Enter the magnet link: ")
            destination_folder = input("Enter the destination folder for download (or leave empty for default): ")
            if not destination_folder:
                destination_folder = "./Out/torrents/magnet/"
            download_magnet(magnet_link, destination_folder)
        elif choice == '2':
            direct_link = input("Enter the direct download link: ")
            destination_folder = input("Enter the destination folder for download (or leave empty for default): ")
            if not destination_folder:
                destination_folder = "./Out/torrents/direct/"
            download_direct(direct_link, destination_folder)
        elif choice == '3':
            torrent_file_path = input("Enter the full path to the .torrent file: ")
            destination_folder = input("Enter the destination folder for download (or leave empty for default): ")
            if not destination_folder:
                destination_folder = "./Out/torrents/file.torrent/"
            download_torrent(torrent_file_path, destination_folder)
        elif choice == '4':
            break  
        else:
            print("Invalid choice, please select again.")

# For Social Media
'''Start of Social Media Downloader'''
def socmed_menu():
    while True:
        print("\n------SocMed Selection------")
        print("1. Download from YouTube")
        print("2. Download from Facebook (Not Available)")  # Video & Audio
        print("3. Download from X 'Twitter' (Not Available)")  # Video & Audio
        print("4. Download from Spotify (Not Available)")  # Video & Audio
        print("5. Download from Threads (Not Available)")  # Video & Photos
        print("6. Download from Instagram")  # Video, Audio, Photos
        print("7. Download from Pinterest")  # Video & Photos
        print("8. Download from TikTok")  # Video & Audio
        print("9. Download from Snapchat (Not Available)")  # Video, Audio, Photos
        print("10. Back to Main Menu")

        choice = input("Please select a platform or back to?: ")

        if choice == '1':
            youtube_menu()  
        elif choice == '2':
            facebook_menu()  
        elif choice == '3':
            twitter_menu()  
        elif choice == '4':
            spotify_menu()  
        elif choice == '5':
            threads_menu()  
        elif choice == '6':
            instagram_menu()  
        elif choice == '7':
            pinterest_menu()  
        elif choice == '8':
            tiktok_menu()  
        elif choice == '9':
            snapchat_menu()  
        elif choice == '10':
            break  
        else:
            print("Invalid choice, please select again.")

# This is YouTube
def youtube_menu():
    while True:
        print("\n------YouTube Download Options:------")
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
        print("\n------nFacebook Download Options:------")
        print("1. Download Facebook Video")
        print("2. Download Facebook Audio")
        print("3. Set Facebook Login Credentials") 
        print("4. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the Facebook video Link: ")
            private = input("Is the video private? (y/n): ").lower()
            if private == 'y':
                download_facebook_video(url, use_auth=True)  
            else:
                download_facebook_video(url)  
        elif choice == '2':
            url = input("Enter the Facebook audio Link: ")
            private = input("Is the audio private? (y/n): ").lower()
            if private == 'y':
                download_facebook_audio(url, use_auth=True)  
            else:
                download_facebook_audio(url)  
        elif choice == '3':
            # Set Facebook credentials
            email = input("Enter your Facebook email: ")
            mobile = input("Enter your two-factor authentication mobile (if applicable): ")
            password = input("Enter your Facebook password: ")
            save_facebook_credentials(email, mobile, password)  
        elif choice == '4':
            break
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

# This is X
def twitter_menu():
    while True:
        print("\n------Twitter (X) Download Options:------")
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
        print("\n------Spotify Download Options:------")
        print("1. Download Spotify Playlist")
        print("2. Download Spotify Audio")
        print("3. Download Spotify Podcast")
        print("4. Back to Main Menu")

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
            url = input("Enter the Spotify podcast Link: ")
            try:
                download_spotify_podcast(url, api_key)
            except Exception as e:
                print(f"Error downloading podcast: {e}")
                prompt_for_api_key(url, 'podcast')
        elif choice == '4':
            break
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

def download_spotify_podcast(url, api_key):
    """Download a Spotify podcast using the provided API key."""
    print(f"Starting download of podcast from URL: {url}")
    try:
        print("Podcast download complete!")
    except Exception as e:
        print(f"Failed to download podcast: {e}")

def prompt_for_api_key(url, download_type):
    """Prompt the user to input an API key and retry the download."""
    retry = input("Error when downloading. Would you like to provide a Spotify API key? (y/n): ")
    if retry.lower() == 'y':
        new_api_key = input("Enter your Spotify API key: ")
        get_spotify_api_key(new_api_key)  

       
        if download_type == 'playlist':
            download_spotify_playlist(url, new_api_key)
        elif download_type == 'audio':
            download_spotify_audio(url, new_api_key)
        elif download_type == 'podcast':
            download_spotify_podcast(url, new_api_key)
    else:
        print("Skipping download...")


# This is Threads
def threads_menu():
    while True:
        print("\n------Threads Download Options:------")
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
        print("\n------Instagram Download Options:------")
        print("1. Download All Content from Profile (Videos, Photos, Stories, Highlights, Saved)")
        print("2. Download Instagram Video")
        print("3. Download Instagram Audio")
        print("4. Download Instagram Photos")
        print("5. Download Instagram Stories")
        print("6. Download Instagram Highlights")
        print("7. Download Instagram Saved Content")
        print("8. Login to Instagram") 
        print("9. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            profile_url = input("Enter the Instagram profile URL: ")
            private = input("Is the profile private? (y/n): ").lower()
            is_private = private == 'y'  
            download_instagram_profile(profile_url, is_private)  
        elif choice == '2':
            url = input("Enter the Instagram video Link: ")
            private = input("Is the video private? (y/n): ").lower()
            if private == 'y':
                download_instagram_video(url, use_auth=True)
            else:
                download_instagram_video(url)
        elif choice == '3':
            url = input("Enter the Instagram audio Link: ")
            private = input("Is the audio private? (y/n): ").lower()
            if private == 'y':
                download_instagram_audio(url, use_auth=True)
            else:
                download_instagram_audio(url)
        elif choice == '4':
            url = input("Enter the Instagram photos Link: ")
            private = input("Are the photos private? (y/n): ").lower()
            if private == 'y':
                download_instagram_photos(url, use_auth=True)
            else:
                download_instagram_photos(url)
        elif choice == '5':
            profile_url = input("Enter the Instagram profile URL: ")
            download_instagram_stories(profile_url)
        elif choice == '6':
            profile_url = input("Enter the Instagram profile URL: ")
            download_instagram_highlights(profile_url)
        elif choice == '7':
            profile_url = input("Enter the Instagram profile URL: ")
            download_instagram_saved(profile_url)
        elif choice == '8':
            # Check if session file exists
            session_file_path = SESSION_FILE_PATH.replace('your_username', 'your_actual_username')  
            if not os.path.exists(session_file_path):
                print("No existing session found. Please log in to your Instagram account.")
                email = input("Enter your Instagram email: ")
                password = input("Enter your Instagram password: ")

                # Save the credentials
                save_instagram_credentials(email=email, mobile=None, password=password)  
            

                L = setup_instaloader(login=True)
                if L.context.is_logged_in:
                    print("Successfully logged into Instagram.")
            else:
                print("Failed to login. Please check your credentials.")
        elif choice == '9':
            break
        else:
            print("Invalid selection. Please choose a number from 1 to 9.")


# This is Pinterest
def pinterest_menu():
    while True:
        print("\n------Pinterest Download Options:------")
        print("1. Download Pinterest Video")
        print("2. Download Pinterest Photos")
        print("3. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the Pinterest video Link: ")
            download_pinterest_video(url)  
        elif choice == '2':
            url = input("Enter the Pinterest photos Link: ")
            download_pinterest_photos(url)  
        elif choice == '3':
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

# This is TikTok
def tiktok_menu():
    while True:
        print("\n------TikTok Download Options:------")
        print("1. Download TikTok Video")
        print("2. Download TikTok Audio")
        print("3. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the TikTok video Link: ")
            download_tiktok_video(url)  
        elif choice == '2':
            url = input("Enter the TikTok audio Link: ")
            download_tiktok_audio(url)  
        elif choice == '3':
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

# This is Snapchat
def snapchat_menu():
    while True:
        print("\n------Snapchat Download Options:------")
        print("1. Download Snapchat Video")
        print("2. Download Snapchat Audio")
        print("3. Download Snapchat Photos")
        print("4. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the Snapchat video Link: ")
            try:
                download_snapchat_video(url)
               
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
            '''End of Downloader'''

# Osint Menu
'''Start of OSINT'''
def osint_menu():
    while True:
        print("\n------BlackMiscellen: OSINT Secton.------")
        print("1. Sherlock")
        print("2. Images")
        print("3. Videos")
        print("4. Exit")
'''End of OSINT'''

# Language Translation
'''Start of Translation'''
def lang_menu():

    while True:
        print("\n------BlackMiscellen: Languages Secton.------")
        print("1. Africa")
        print("2. Asia")
        print("3. Antartica")
        print("4. Austrilla & Oceania")
        print("5. Europe")
        print("6. North America")
        print("7. South America")
        print("9. Exit")

        choice = input("Select Langauge transaltions: ")

        if choice == '1':
            african_menu()
        elif choice == '2':
            asian_menu()
        elif choice == '3':
            antartican_menu
        elif choice == '4':
            austrillian_menu
        elif choice == '5':
           europian_menu()
        elif choice == '6':
            generation_menu()
        elif choice == '7':
            north_american_menu()
        elif choice == '8':
            south_american_menu()
        elif choice == '9':
            print("Exiting Language Translation...")
            break
        else:
            print("Invalid choice: Choose 1, 2, 3, 4, 5, 6, 7, 8, or 9: ")

# African
def african_menu():
    while True:
        print("African Translations")
        print("000. Exit")
# Asian
# African
def asian_menu():
    while True:
        print("Asian Translations")
        print("000. Exit")
# African
def antartican_menu():
    while True:
        print("Antartican Translations")
        print("000. Exit")

# Austrillian
def austrillian_menu():
    while True:
        print("Austrillian Translations")
        print("000. Exit")

# Europe
def europian_menu():
    while True:
        print("\n------Europe------")
        print("1. English (Default)")
        print("2. Albanian")
        print("3. Andorra (Catalan)")
        print("4. Austrian (German)")
        print("5. Belarusian")
        print("6. Belgium( Dutch, French, German)")
        print("7. Bosnian")
        print("8. Bulgarian")
        print("9. Croatian")
        print("10. Czech")
        print("11. Denmark (Danish, Greenlandic, Faroese)")
        print("12. Estonian")
        print("13. Finnish")
        print("14. French")
        print("15. German")
        print("16. Greek")
        print("17. Hungarian")
        print("18. Icelandic")
        print("19. Irish")
        print("20. Italian")
        print("21. Kosovo (Albanian, Serbian)")
        print("22. Latvian")
        print("23. Liechtenstien (German)")
        print("24. Lithuanian")
        print("25. Luxembourgish")
        print("26. Macedonian")
        print("27. Maltese")
        print("28. Moldovan")
        print("29. Monaco (French)")
        print("30. Montanegrin")
        print("31. Netherlands (Ducth)")
        print("32. Norwegian")
        print("33. Polish")
        print("34. Portogues")
        print("35. Romanian")
        print("36. Russian")
        print("37. San Marino (Italian)")
        print("38. Serbian")
        print("39. Slovak")
        print("40. Slovenian")
        print("41. Spanish")
        print("42. Swedish")
        print("43. Switzerland (French, German, Italian, Romansch)")
        print("44. Ukrainian")
        print("45. United Kingdom (Scottish Gaelic, Welsh, Irish)")
        print("46. Vatican (French, Latin, Italian)")
        print("47. Exit")

        choice = input("Select Langauge transaltions: ")

        if choice == '1':
            textarea = input("Enter text here...")
        elif choice == '2':
            asian_menu()
        elif choice == '3':
            antartican_menu
        elif choice == '4':
            austrillian_menu
        elif choice == '5':
           europian_menu()
        elif choice == '6':
            generation_menu()
        elif choice == '7':
            north_american_menu()
        elif choice == '8':
            south_american_menu()
        elif choice == '47':
            print("Exiting European Translation...")
            break
        else:
            print("Invalid choice: Choose 1, 2, 3, 4, 5, 6, 7; up to 46, or 47 exit: ")

# North America
def north_american_menu():
    while True:
        print("\n------North American Translations------")
        print("000. Exit")

# South American
def south_american_menu():
    while True:
        print("\n------South American Translations------")
        print("000. Exit")

'''End of Transaltion'''

# Image Filtering Menu
'''Start of Photos & Videos'''
def phovid_menu():
    while True:
        print("\n------BlackMiscellen: Photos & Videos Filters Secton.------")
        print("1. Photos")
        print("2. Videos")
        print("3. Exit")

        choice = input("Select what you desired: ")

        if choice == '1':
            photos_menu()
        elif choice == '2':
            videos_menu()
        elif choice == '3':
            print("Exiting this Section...")
            break
        else:
            print("Invalid selection: Please select 1 or 2.")

# Image Filtering Menu
def photos_menu():
    while True:
        print("\n------BlackMiscellen: Photos Filters Secton.------")
        print("1. PIXIELIXE [Supported image type:] (JPG, PNG, BMP, TIFF, GIF)")
        print("2. PICSART")
        print("3. ApyHub")
        print("4. Photopea.com (Alternative to Photoshop)")
        print("5. Exit")

# Video Filtering Menu
def videos_menu():
    while True:
        print("\n------BlackMiscellen: Video Filters Secton.------")
        print("1. PIXIELIXE [Supported image type:] (JPG, PNG, BMP, TIFF, GIF)")
        print("2. PICSART")
        print("3. ApyHub")
        print("4. Photopea.com (Alternative to Photoshop)")
        print("5. Exit")
'''End of Photos & Videos'''

# Image Generation Menu
def generation_menu():
    while True:
        print("\n------BlackMiscellen: Generation Secton.------")
        print("1. Videos")
        print("2. Images")
        print("3. Text")
        print("4. Powerpoint")
        print("5. Transcript")
        print("6. Exit")

# This is Settings
'''Start of Langauge'''
def settings_menu():
    """Display the settings menu."""
    selected_color = color_scheme.COLOR_SCHEMES['reset'] 

    while True:
        print("\n------Settings Menu:------")
        print("1. Color Scheme")
        print("2. Language")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == '1':
            
            selected_color = color_scheme.get_color_choice()

        elif choice == '2':
            # Define languages
            languages = [
                "Arabic", "French", "German", "Japanese", "Korean",
                "Mandarin Chinese", "Portuguese", "Russian", "Spanish", "Thai"
            ]

            # Display languages
            print("\nSelect a Language:")
            for idx, language in enumerate(sorted(languages), start=1):
                print(f"{idx}. {translate_text(translations, language)}")  # Translate language names

            # Get user's choice for language
            language_choice = input(translate_text(translations, "Enter the number of your choice (1-10): "))
            if language_choice.isdigit() and 1 <= int(language_choice) <= 10:
                selected_language = sorted(languages)[int(language_choice) - 1]

                # Update translations based on new language selection
                translations = load_translations(selected_language.lower())
                enable_translation(translations)  # Re-enable translation with new language
                print(translate_text(translations, f"You selected Language: {selected_language}"))
            else:
                print("Invalid choice")

        elif choice == '3':
            print("Exiting settings menu...")
            break  # Exit the settings menu

        else:
            print("Invalid choice, please try again.")
            '''End of Langauge'''

# Update Trigger
def update_now():
    try:
        # Call update.py as a new process
        subprocess.run(["python", "update.py"], check=True)
        print("Update script triggered successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running update.py: {e}")
    except FileNotFoundError:
        print("update.py script not found. Make sure it’s in the correct directory.")


log_file_path = "./temp/temp.log.txt"

s
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

def log_event(event_type):
    """
    Logs the log-in or log-out event to the specified log file.

    :param event_type: str, 'login' for log-in or 'logout' for log-out
    """
    
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

   
    computer_name = os.uname().nodename if os.name != 'nt' else os.getenv('COMPUTERNAME')

    
    log_message = f"{timestamp} - {event_type.upper()} - Computer: {computer_name}\n"

    
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_message)

def log_in():
    """Logs a log-in event."""
    log_event("login")

def log_out():
    """Logs a log-out event."""
    log_event("logout")

def handle_exit(signum, frame):
    """Handles exit signal."""
    log_out()  
    sys.exit(0)

   
    signal.signal(signal.SIGINT, handle_exit)  
    signal.signal(signal.SIGTERM, handle_exit)  

    
    try:
        while True:
            time.sleep(1)  
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        log_out()  


if __name__ == "__main__":
    main_menu()  
    log_in()
