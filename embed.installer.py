import platform
import os
import shutil
import subprocess
import urllib.request
import zipfile
import tarfile

# URLs downloads
MAC_PYTHON_URL = "https://www.python.org/ftp/python/3.13.0/python-3.13.0-macos11.pkg"
WIN_PYTHON_URL = "https://www.python.org/ftp/python/3.13.0/python-3.13.0-embed-amd64.zip"
LINUX_PYTHON_LOG = "./App/embedded/python/Linux/python_installed.log"

WIN_FFMPEG_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z"
MAC_FFMPEG_URL = "https://evermeet.cx/ffmpeg/ffmpeg-117464-g1eb026dd8b.7z"
LINUX_FFMPEG_URL = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl-shared.tar.xz"

# Paths save downloads
PYTHON_PATH_MAC = "./App/embedded/python/MacOs/python.pkg"
PYTHON_PATH_WIN = "./App/embedded/python/Windows/python.zip"
FFMPEG_PATH_WIN = "./App/embedded/ffmpeg/Windows/ffmpeg.7z"
FFMPEG_PATH_MAC = "./App/embedded/ffmpeg/MacOs/ffmpeg.7z"

def is_installed(command):
    """Check if a command is available on the system."""
    try:
        subprocess.run([command, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except Exception:
        return False

def download_file(url, path):
    """Download file from a URL."""
    try:
        if os.path.exists(path):
            print(f"{path} already exists. Skipping download.")
        else:
            print(f"Downloading {url} to {path}")
            urllib.request.urlretrieve(url, path)
            print(f"Downloaded {url} successfully.")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def unzip_file(zip_path, extract_to):
    """Unzip a file."""
    try:
        print(f"Unzipping {zip_path} to {extract_to}")
        if zipfile.is_zipfile(zip_path):
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
        elif zip_path.endswith(".7z"):
            # For 7z extraction, we rely on 7z command-line utility
            subprocess.run(["7z", "x", zip_path, f"-o{extract_to}"], check=True)
        print(f"Unzipped {zip_path} successfully.")
    except Exception as e:
        print(f"Error unzipping {zip_path}: {str(e)}")

def install_python_mac():
    """Install Python on macOS."""
    if is_installed("python3"):
        print("Python is already installed on macOS.")
    else:
        download_file(MAC_PYTHON_URL, PYTHON_PATH_MAC)
        try:
            subprocess.run(["installer", "-pkg", PYTHON_PATH_MAC, "-target", "/"], check=True)
        except Exception as e:
            print("Python installation failed on macOS. Please install manually.")
            print(f"Error: {str(e)}")

def install_python_windows():
    """Install Python on Windows."""
    if is_installed("python"):
        print("Python is already installed on Windows.")
    else:
        download_file(WIN_PYTHON_URL, PYTHON_PATH_WIN)
        unzip_file(PYTHON_PATH_WIN, "./App/embedded/python/Windows/")
        print("Python installed on Windows.")

def install_ffmpeg_mac():
    """Install FFmpeg on macOS."""
    if is_installed("ffmpeg"):
        print("FFmpeg is already installed on macOS.")
    else:
        download_file(MAC_FFMPEG_URL, FFMPEG_PATH_MAC)
        unzip_file(FFMPEG_PATH_MAC, "./App/embedded/ffmpeg/MacOs/")

def install_ffmpeg_windows():
    """Install FFmpeg on Windows."""
    if is_installed("ffmpeg"):
        print("FFmpeg is already installed on Windows.")
    else:
        download_file(WIN_FFMPEG_URL, FFMPEG_PATH_WIN)
        unzip_file(FFMPEG_PATH_WIN, "./App/embedded/ffmpeg/Windows/")

def install_ffmpeg_linux():
    """Install FFmpeg on Linux."""
    if is_installed("ffmpeg"):
        print("FFmpeg is already installed on Linux.")
    else:
        download_file(LINUX_FFMPEG_URL, "./App/embedded/ffmpeg/Linux/ffmpeg.tar.xz")
        with tarfile.open("./App/embedded/ffmpeg/Linux/ffmpeg.tar.xz") as tar_ref:
            tar_ref.extractall("./App/embedded/ffmpeg/Linux/")

def detect_system():
    """Detect OS and install the required packages."""
    os_name = platform.system().lower()
    if "darwin" in os_name:
        print("Detected macOS. Installing dependencies...")
        install_python_mac()
        install_ffmpeg_mac()
    elif "windows" in os_name:
        print("Detected Windows. Installing dependencies...")
        install_python_windows()
        install_ffmpeg_windows()
    elif "linux" in os_name:
        print("Detected Linux. Please use your package manager to install Python.")
        with open(LINUX_PYTHON_LOG, 'w') as log_file:
            log_file.write("Python installed via package manager.\n")
        install_ffmpeg_linux()
    else:
        print(f"Unsupported OS: {os_name}")

if __name__ == "__main__":
    detect_system()




'''When running the setup.py add a command in setup.py to run the script file embed.installer.py
to install this dependecies or requirements.

Before that add a function also to embed.install.py that make a system detection for OS, if macos then install it, if there an error that cannot be install, then add a prompt message that python installation error, download it mannualy, also include windows for that matter then except for linux, since it will install via command.

The embed.installer.py components to create."
---
# Python
macOs Python Installer = https://www.python.org/ftp/python/3.13.0/python-3.13.0-macos11.pkg # The path were the file will saved ./App/embedded/python/MacOs/ and send command to install without human intervention or other means auto install.
Windows Python Embed = https://www.python.org/ftp/python/3.13.0/python-3.13.0-embed-amd64.zip #Add fuction to unzip # The path were the file will saved ./App/embedded/python/Windows/ and send command to install without human intervention or other means auto install.
Linux Python Command Installer # Since linux python are based install via command just create a file log, that the python for linux installed in this path "./App/embedded/python/Linux/" the log file.

# ffmpeg

Windows = https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z # Add function to unzip # This is the path were to be saved  ./App/embedded/ffmpeg/Windows/
macos = https://evermeet.cx/ffmpeg/ffmpeg-117464-g1eb026dd8b.7z # Add function to unzip # This is the path were to be saved  ./App/embedded/ffmpeg/MacOs/
linux = https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl-shared.tar.xz # Add function to unzip # This is the path were to be saved  ./App/embedded/ffmpeg/Linux/ "
My current setup.py code "from setuptools import setup, find_packages
---
setup(
    name='BlackDownloader',
    version='1.10.0',
    description='A systematic downloader which covers a wide variety of platforms made by BlackBlazent.',
    author='BlackRose',
    packages=find_packages(),
    install_requires=[
        'yt-dlp>=0.1.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
" add a send command to install those requirements above.
'''
