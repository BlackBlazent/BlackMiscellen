import colorama
import os
import time
import threading

colorama.init()  # Initialize colorama

# Define the ASCII art using a raw string
ascii_art = r"""
  ____  _            _    ____                      _                 _           
 | __ )| | __ _  ___| | _|  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ 
 |  _ \| |/ _` |/ __| |/ / | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 | |_) | | (_| | (__|   <| |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
 |____/|_|\__,_|\___|_|\_\____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|

 From BlackBlazent                                                   By BlackRose
"""

def animate_ascii_art():
    """Animate the ASCII art by changing its color periodically."""
    colors = [colorama.Fore.RED, colorama.Fore.BLUE, colorama.Fore.YELLOW, colorama.Fore.CYAN]
    while True:
        for color in colors:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
            print(color + ascii_art)  # Print ASCII art in the current color
            time.sleep(5)  # Change color every 5 seconds

def display_banner():
    """Display the ASCII banner at the top of the console without clearing."""
    print(colorama.Fore.CYAN + ascii_art)  # Print ASCII art in the specified color

def start_banner():
    """Start the ASCII animation in a separate thread and display the banner."""
    display_banner()  # Display the banner immediately
    # Start ASCII animation in a separate thread
    threading.Thread(target=animate_ascii_art, daemon=True).start()
    
    # Keep the main thread alive to prevent exiting
    while True:
        time.sleep(1)  # Main thread sleep

# Run the banner display
if __name__ == "__main__":
    start_banner()
