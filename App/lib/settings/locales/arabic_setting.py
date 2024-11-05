import json
import os
import sys

def load_translations(language):
    """Load existing translations from a JSON file based on the given language."""
    translate_file = f'./App/settings/locales/{language}.json'
    if os.path.exists(translate_file):
        with open(translate_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def translate_text(translations, text):
    """Retrieve the translated text from the loaded translations."""
    return translations.get(text, text)  # Return original text if not found

class ConsoleOutputInterceptor:
    """Intercepts console output and translates it."""
    def __init__(self, translations):
        self.original_stdout = sys.stdout
        self.translations = translations

    def write(self, message):
        # Strip whitespace from the message
        stripped_message = message.strip()
        # Translate the message before writing it to the original stdout
        translated_message = translate_text(self.translations, stripped_message)
        # Call the original stdout's write method directly
        self.original_stdout.write(translated_message + "\n")

    def flush(self):
        pass  # For compatibility with Python's I/O

def enable_translation(translations):
    """Enable the translation of all console output."""
    sys.stdout = ConsoleOutputInterceptor(translations)
