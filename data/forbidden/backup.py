import os
import shutil

# Path to the original files directory
ORIGINAL_PATH = './App/data/forbidden/'
# Path to the backup directory
BACKUP_PATH = './App/data/forbidden/backup/crossx/'

def create_backup():
    # Check if the backup directory exists; if not, create it
    os.makedirs(BACKUP_PATH, exist_ok=True)

    # Iterate over the files and directories in the original path
    for item in os.listdir(ORIGINAL_PATH):
        src = os.path.join(ORIGINAL_PATH, item)
        dst = os.path.join(BACKUP_PATH, item)

        # If it's a file, copy it to the backup directory
        if os.path.isfile(src):
            shutil.copy2(src, dst)  # Preserve metadata
            print(f"Backed up file: {src} to {dst}")
        elif os.path.isdir(src):
            # If it's a directory, copy it recursively
            shutil.copytree(src, dst, dirs_exist_ok=True)  # Python 3.8+
            print(f"Backed up directory: {src} to {dst}")

    print("Backup completed.")

if __name__ == "__main__":
    create_backup()
