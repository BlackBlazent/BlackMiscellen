# color_scheme.py

# Define ANSI color codes
COLOR_SCHEMES = {
    '1': ('\033[31m', 'Red'),         # Red
    '2': ('\033[33m', 'Yellow'),      # Yellow
    '3': ('\033[36m', 'Neon Blue'),   # Neon Blue (Cyan)
    '4': ('\033[32m', 'Green'),       # Green
    'reset': '\033[0m'                # Reset to default color
}

def display_color_options():
    """Display available color schemes for user selection."""
    print("\nSelect a Color Scheme:")
    for key, value in COLOR_SCHEMES.items():
        if key != 'reset' and isinstance(value, tuple):  # Skip 'reset' and check for tuples
            _, name = value
            print(f"{key}. {name}")

def get_color_choice():
    """Prompt the user to choose a color scheme and return the color code."""
    display_color_options()
    choice = input("Enter the number of your choice (1-4): ")
    color_code = COLOR_SCHEMES.get(choice, ('', 'Invalid choice'))[0]
    if color_code:
        print(f"\nYou selected Color Scheme: {COLOR_SCHEMES[choice][1]}")
    else:
        print("Invalid choice, using default color.")
    return color_code or COLOR_SCHEMES['reset']

def apply_color(text, color_code):
    """Apply the chosen color code to the provided text."""
    return f"{color_code}{text}{COLOR_SCHEMES['reset']}"
