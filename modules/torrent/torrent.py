from PyBitTorrent import TorrentClient
import time
import os
import subprocess
import threading

# Path to FFmpeg executable
FFMPEG_PATH = "../App/embedded/ffmpeg/Windows/bin/ffmpeg.exe"

# Global variable for managing downloads
active_torrents = []

def download_magnet(magnet_link, destination_folder):
    """Download using a magnet link."""
    print(f"Downloading via magnet link: {magnet_link} to {destination_folder}")

    # Initialize Torrent download with the magnet link
    client = TorrentClient()  # Initialize the client here
    torrent = client.add_torrent(magnet_link, download_dir=destination_folder)
    active_torrents.append(torrent)
    
    # Start download tracking in a new thread
    threading.Thread(target=track_download, args=(torrent,)).start()

def download_direct(direct_link, destination_folder):
    """Download via direct link and process with FFmpeg."""
    print(f"Downloading via direct link: {direct_link} to {destination_folder}")
    
    output_file = os.path.join(destination_folder, os.path.basename(direct_link))
    command = [FFMPEG_PATH, '-i', direct_link, output_file]
    
    # Download and process with FFmpeg
    subprocess.run(command)
    print("Download complete. Processing with FFmpeg...")
    process_with_ffmpeg(destination_folder)

def download_torrent(torrent_file_path, destination_folder):
    """Download via .torrent file."""
    print(f"Downloading via torrent file: {torrent_file_path} to {destination_folder}")

    # Initialize Torrent download with the .torrent file
    client = TorrentClient()  # Initialize the client here
    torrent = client.add_torrent(torrent_file_path, download_dir=destination_folder)
    active_torrents.append(torrent)
    
    # Start download tracking in a new thread
    threading.Thread(target=track_download, args=(torrent,)).start()

def track_download(torrent):
    """Track the progress of an active torrent download."""
    while not torrent.is_complete:
        # Fetch the progress and speed of the download
        progress = torrent.progress * 100
        speed = torrent.download_rate / 1024  # Convert to kB/s
        file_size = torrent.size / (1024 * 1024)  # Convert to MB
        
        # Print the progress status
        print(f"Download progress: {progress:.2f}% complete")
        print(f"Download speed: {speed:.2f} kB/s")
        print(f"File size: {file_size:.2f} MB")
        
        time.sleep(1)
    
    print("Download complete. Processing with FFmpeg...")
    process_with_ffmpeg(torrent.download_dir)

def process_with_ffmpeg(destination_folder):
    """Process downloaded files with FFmpeg."""
    for filename in os.listdir(destination_folder):
        if filename.endswith('.mkv') or filename.endswith('.mp4'):
            input_file = os.path.join(destination_folder, filename)
            output_file = os.path.join(destination_folder, f"processed_{filename}")
            
            # FFmpeg command to process the file
            command = [FFMPEG_PATH, '-i', input_file, output_file]
            print(f"Processing {input_file} with FFmpeg...")
            subprocess.run(command)
            print(f"Processed {input_file} to {output_file}")
