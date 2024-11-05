import time
import colorama
import os
import random
from datetime import datetime

colorama.init() 


verse_folder_path = os.path.join(os.path.dirname(__file__), "book-chapter")

def load_daily_verse():
    """Select a daily verse file based on the current date."""
    verse_files = [file for file in os.listdir(verse_folder_path) if file.endswith(".txt")]
    if not verse_files:
        return "No verses available."

    
    day_of_year = datetime.now().timetuple().tm_yday
    selected_file = verse_files[day_of_year % len(verse_files)]

    
    with open(os.path.join(verse_folder_path, selected_file), 'r') as file:
        return file.read().strip()

def display_daily_verse():
    """Display the verse of the day with a sliding interval and color transitions."""
    colors = [colorama.Fore.CYAN, colorama.Fore.GREEN, colorama.Fore.YELLOW]
    verse_text = load_daily_verse()

    while True:
        for color in colors:
            os.system('cls' if os.name == 'nt' else 'clear')  
            print(color + verse_text)  
            time.sleep(50)  


if __name__ == "__main__":
    display_daily_verse()
