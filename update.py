import os
import sys
import requests
import zipfile
import shutil

# GitHub release details
GITHUB_RELEASE_URL = "https://github.com/LoneStamp/BlackDownloader/releases/download/v1.10.0/BlackDownloader-v1.10.0.zip"
DOWNLOAD_PATH = "./temp/update.zip"  # Temporary download location
EXTRACT_PATH = "./temp/extracted_update"  # Temporary extraction folder
TARGET_PATH = "./App/"  # Path where files will be replaced

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

def replace_files():
    print("Replacing old files with the new update...")
    for root, dirs, files in os.walk(EXTRACT_PATH):
        rel_path = os.path.relpath(root, EXTRACT_PATH)
        dest_dir = os.path.join(TARGET_PATH, rel_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.move(src_file, dest_file)
            print(f"Updated: {dest_file}")

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
