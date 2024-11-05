import os
import random
import string

# List of important files that should trigger confirmation before deletion
IMPORTANT_FILES = [
    './App/data/forbidden/blackbuilder.db',
    './App/data/forbidden/Khah.Jvssljavy.py',
    './App/lib/',
    './App/embedded/ffmpeg/',
    './App/modules/',
]

# Function to generate a random word of a given length
def generate_random_word(length=6):
    letters = string.ascii_letters  # All lowercase and uppercase letters
    return ''.join(random.choice(letters) for _ in range(length))

# Function to show confirmation in the console
def confirm_deletion(file_path):
    # Generate a random confirmation word
    confirmation_word = generate_random_word()

    print(f"Warning: Deleting '{file_path}' may cause the app to stop working.")
    print(f"To confirm deletion, type the following word: '{confirmation_word}'")
    
    # Ask for user input
    user_input = input("Enter the confirmation word: ")

    if user_input == confirmation_word:
        try:
            # Check if it's a file or directory and delete accordingly
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"{file_path} deleted successfully.")
            elif os.path.isdir(file_path):
                os.rmdir(file_path)  # Use shutil.rmtree() to remove non-empty directories if needed
                print(f"Directory {file_path} deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")
    else:
        print("Deletion cancelled.")

# Function to attempt deleting a file
def delete_file(file_path):
    # Check if the file is in the list of important files
    if any(file_path.startswith(important_file) for important_file in IMPORTANT_FILES):
        confirm_deletion(file_path)
    else:
        try:
            # Delete file if it's not critical
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"{file_path} deleted successfully.")
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
                print(f"Directory {file_path} deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")

# Example usage
if __name__ == "__main__":
    # Example: User tries to delete a critical file
    file_to_delete = './App/data/forbidden/blackbuilder.db'  # Replace this with the file path the user wants to delete
    delete_file(file_to_delete)
