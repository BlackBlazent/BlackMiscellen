import os
import sys
import requests
import zipfile
import shutil


GITHUB_RELEASE_URL = "https://github.com/LoneStamp/BlackDownloader/releases/download/v1.10.0/BlackDownloader-v1.10.0.zip"
DOWNLOAD_PATH = "./temp/update.zip"  
EXTRACT_PATH = "./temp/extracted_update" 


TARGET_PATHS = {
    "./App/": [
        "config",
        "config/bin/connect.rb",
        "config/bin/quarrel.rb",
        "config/bin/db.sqlite",
        "config/bin/raw_select.rb",
        "config/deb_miscellen.dev",
        "config/main.cpp",
        "config/Makefile.win",
        "data/api/spotifyAPI.db",
        "data/api/spotifyAPI.json",
        "data/auth/facebook/facebook.details.json",
        "data/auth/instaloader/instagram.details.json",
        "data/forbidden/backup_gathering.sh",
        "data/forbidden/backup.py",
        "data/forbidden/blackmiscellen.db"
        "data/forbidden/Khah.Jvssljavy.py"
        "data",
        "app.py"
    ],
    "./App/another_folder/": [
        "another_config.json",
        "another_folder/settings.py",
    ],
    "./App/extra_folder/": [
        "extra_config.json",
        "extra_folder/init.py",
    ],

}

def download_update():
    print("Downloading the latest update...")
    try:
        response = requests.get(GITHUB_RELEASE_URL, stream=True)
        response.raise_for_status()
        os.makedirs(os.path.dirname(DOWNLOAD_PATH), exist_ok=True)
        with open(DOWNLOAD_PATH, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print("Download completed!")
    except requests.RequestException as e:
        print(f"Error downloading the update: {e}")
        sys.exit(1)

def extract_update():
    print("Extracting the update...")
    try:
        os.makedirs(EXTRACT_PATH, exist_ok=True)
        with zipfile.ZipFile(DOWNLOAD_PATH, 'r') as zip_ref:
            zip_ref.extractall(EXTRACT_PATH)
        print("Extraction completed!")
    except zipfile.BadZipFile as e:
        print(f"Error extracting the update: {e}")
        sys.exit(1)

def should_replace(path, target_list):
    """Check if a path is in the given target list."""
    return any(path.startswith(target) for target in target_list)

def replace_files():
    print("Replacing old files and adding new ones from the update...")

    
    for target_base, target_list in TARGET_PATHS.items():
        for root, dirs, files in os.walk(EXTRACT_PATH):
            rel_path = os.path.relpath(root, EXTRACT_PATH)
            dest_dir = os.path.join(target_base, rel_path)

            
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            for file in files:
                src_file = os.path.join(root, file)
                file_rel_path = os.path.join(rel_path, file)
                dest_file = os.path.join(dest_dir, file)

               
                if should_replace(file_rel_path, target_list):
                    shutil.move(src_file, dest_file)
                    print(f"Updated: {dest_file}")
                else:
                    
                    shutil.move(src_file, dest_file)
                    print(f"Added new file: {dest_file}")

def cleanup():
    print("Cleaning up temporary files...")
    shutil.rmtree(EXTRACT_PATH)
    os.remove(DOWNLOAD_PATH)
    print("Cleanup completed!")

def update_app():
    download_update()
    extract_update()
    replace_files()
    cleanup()
    print("Update process completed successfully!")

if __name__ == "__main__":
    update_app()
