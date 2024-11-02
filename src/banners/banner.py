import colorama
import os
import time
import threading
import random

folder_path = os.path.join(os.path.dirname(__file__), "../../src/banners/bannerList/")

colorama.init()  


signature_text = "From BlackBlazent                                                   By BlackRose"


def load_banners_from_folder(folder_path=None):
    """Load all banner text files from a specified folder."""
    if folder_path is None:
        folder_path = os.path.join(os.path.dirname(__file__), "../../src/banners/bannerList/")

    print("Checking folder path:", folder_path)  
    banners = []

    if not os.path.isdir(folder_path):
        print(f"Folder not found: {folder_path}")
        return banners  

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            with open(os.path.join(folder_path, file_name), 'r') as file:
                banners.append(file.read())

    return banners


banners = load_banners_from_folder()


banner_running = False

def display_banner():
    """Display the initial banner without animation for a static introduction."""
    initial_banner = random.choice(banners) if banners else ""
    print(colorama.Fore.CYAN + initial_banner + "\n" + signature_text)  

def animate_ascii_art():
    """Animate the ASCII art by shuffling through banners and changing color periodically."""
    global banner_running
    colors = [colorama.Fore.RED, colorama.Fore.BLUE, colorama.Fore.YELLOW, colorama.Fore.CYAN]

    while banner_running:
        for color in colors:
            current_banner = random.choice(banners)
            
            print("\033[F" + " " * os.get_terminal_size().columns + "\033[F", end='') 
            print(color + current_banner + "\n" + signature_text)  
            time.sleep(20)  

def start_banner():
    """Start the ASCII animation in a separate thread and display the banner."""
    global banner_running
    banner_running = True
    display_banner()  
    
    threading.Thread(target=animate_ascii_art, daemon=True).start()

def stop_banner():
    """Stop the ASCII animation."""
    global banner_running
    banner_running = False


if __name__ == "__main__":
    start_banner()
    try:
        while True:
            time.sleep(1)  
    except KeyboardInterrupt:
        stop_banner()
