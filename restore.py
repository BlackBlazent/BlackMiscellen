import os
import shutil
import stat


BACKUP_PATH = './App/data/forbidden/backup/'
RESTORE_PATH = './App/data/forbidden/backup/crossx/'

def make_invisible_and_protected(filepath):
    
    if os.name == 'nt':
       
        os.system(f'attrib +h "{filepath}"')
    else:
        s
        os.chmod(filepath, stat.S_IREAD) 

def restore_backup():

    backup_file = os.path.join(BACKUP_PATH, 'backup.py')
    if not os.path.exists(backup_file):
        print("Backup file does not exist.")
        return

    
    os.makedirs(RESTORE_PATH, exist_ok=True)

    
    for filename in os.listdir(BACKUP_PATH):
        if filename == 'backup.py':
            continue  
        src = os.path.join(BACKUP_PATH, filename)
        dst = os.path.join(RESTORE_PATH, filename)
        if os.path.isfile(src):
            shutil.copy2(src, dst)  
            make_invisible_and_protected(dst) 
            print(f"Restored and protected: {dst}")

    print("Restoration completed.")

if __name__ == "__main__":
    restore_backup()
