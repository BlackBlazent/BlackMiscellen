import colorama
import os
import time
import threading
import random

folder_path = os.path.join(os.path.dirname(__file__), "../../src/banners/bannerList/")

colorama.init()  # Initialize colorama

# Define the text to remain at the bottom of each banner
signature_text = "From BlackBlazent                                                   By BlackRose"

# Load banners from the folder
def load_banners_from_folder(folder_path=None):
    """Load all banner text files from a specified folder."""
    if folder_path is None:
        folder_path = os.path.join(os.path.dirname(__file__), "../../src/banners/bannerList/")

    print("Checking folder path:", folder_path)  # Debugging print
    banners = []

    if not os.path.isdir(folder_path):
        print(f"Folder not found: {folder_path}")
        return banners  # Return an empty list if the folder doesn't exist

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            with open(os.path.join(folder_path, file_name), 'r') as file:
                banners.append(file.read())

    return banners

# Initialize the banners list by loading from the folder
banners = load_banners_from_folder()

# Global variable to control the banner animation
banner_running = False

def display_banner():
    """Display the initial banner without animation for a static introduction."""
    initial_banner = random.choice(banners) if banners else ""
    print(colorama.Fore.CYAN + initial_banner + "\n" + signature_text)  # Initial display

def animate_ascii_art():
    """Animate the ASCII art by shuffling through banners and changing color periodically."""
    global banner_running
    colors = [colorama.Fore.RED, colorama.Fore.BLUE, colorama.Fore.YELLOW, colorama.Fore.CYAN]

    while banner_running:
        for color in colors:
            current_banner = random.choice(banners)  # Randomly pick a banner
            # Move the cursor back to the start of the banner area
            print("\033[F" + " " * os.get_terminal_size().columns + "\033[F", end='')  # Clear the previous line
            print(color + current_banner + "\n" + signature_text)  # Print banner with signature
            time.sleep(20)  # Change banner every 20 seconds

def start_banner():
    """Start the ASCII animation in a separate thread and display the banner."""
    global banner_running
    banner_running = True
    display_banner()  # Display the banner immediately
    # Start ASCII animation in a separate thread
    threading.Thread(target=animate_ascii_art, daemon=True).start()

def stop_banner():
    """Stop the ASCII animation."""
    global banner_running
    banner_running = False

# If you want to run the banner display directly for testing
if __name__ == "__main__":
    start_banner()
    try:
        while True:
            # Here you can handle user input for the main menu
            print("\n" * 3)  # Add some space before displaying the menu
            print("Welcome to BlackMiscellen! Comprehensive Toolkits.")
            print("1. Converter (Files to extension names)")
            print("2. Downloader (Media Downloader)")
            print("3. Osint")
            print("4. Language Translator")
            print("5. Photos/Images Filtering")
            print("6. Settings")
            print("7. Update")
            print("8. Exit")

            choice = input("Select Miscellaneous Tools: ")

            if choice == '1':
                print("You selected Converter.")
            elif choice == '2':
                print("You selected Downloader.")
            elif choice == '3':
                print("You selected Osint.")
            elif choice == '4':
                print("You selected Language Translator.")
            elif choice == '5':
                print("You selected Photos/Images Filtering.")
            elif choice == '6':
                print("You selected Settings.")
            elif choice == '7':
                print("You selected Update.")
            elif choice == '8':
                print("Exiting BlackMiscellen...")
                stop_banner()  # Stop the banner animation
                break
            else:
                print("Invalid choice, please try again.")
    except KeyboardInterrupt:
        stop_banner()
