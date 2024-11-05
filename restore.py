import os
import shutil
import stat

# Path to the backup directory
BACKUP_PATH = './App/data/forbidden/backup/'
RESTORE_PATH = './App/data/forbidden/backup/crossx/'

def make_invisible_and_protected(filepath):
    # Make the file hidden (Windows) or set permissions (Linux/Mac)
    if os.name == 'nt':
        # For Windows, use the hidden attribute
        os.system(f'attrib +h "{filepath}"')
    else:
        # For Unix-like systems, remove all permissions
        os.chmod(filepath, stat.S_IREAD)  # Read-only

def restore_backup():
    # Check if backup.py exists
    backup_file = os.path.join(BACKUP_PATH, 'backup.py')
    if not os.path.exists(backup_file):
        print("Backup file does not exist.")
        return

    # Create the restore directory if it doesn't exist
    os.makedirs(RESTORE_PATH, exist_ok=True)

    # Copy files from the backup directory to the restore path
    for filename in os.listdir(BACKUP_PATH):
        if filename == 'backup.py':
            continue  # Skip the backup.py itself
        src = os.path.join(BACKUP_PATH, filename)
        dst = os.path.join(RESTORE_PATH, filename)
        if os.path.isfile(src):
            shutil.copy2(src, dst)  # Copy file with metadata
            make_invisible_and_protected(dst)  # Make the file invisible and protected
            print(f"Restored and protected: {dst}")

    print("Restoration completed.")

if __name__ == "__main__":
    restore_backup()
