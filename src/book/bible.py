import time
import colorama
import os
import random
from datetime import datetime

colorama.init()  # Initialize colorama for colorful output

# Folder path for verse files
verse_folder_path = os.path.join(os.path.dirname(__file__), "book-chapter")

def load_daily_verse():
    """Select a daily verse file based on the current date."""
    verse_files = [file for file in os.listdir(verse_folder_path) if file.endswith(".txt")]
    if not verse_files:
        return "No verses available."

    # Use the day of the year to select a file (1 to 365 or 366)
    day_of_year = datetime.now().timetuple().tm_yday
    selected_file = verse_files[day_of_year % len(verse_files)]

    # Read and return the verse text from the selected file
    with open(os.path.join(verse_folder_path, selected_file), 'r') as file:
        return file.read().strip()

def display_daily_verse():
    """Display the verse of the day with a sliding interval and color transitions."""
    colors = [colorama.Fore.CYAN, colorama.Fore.GREEN, colorama.Fore.YELLOW]
    verse_text = load_daily_verse()

    while True:
        for color in colors:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
            print(color + verse_text)  # Display verse with color effect
            time.sleep(50)  # Wait for 15 seconds before changing color

# Run the display function
if __name__ == "__main__":
    display_daily_verse()
