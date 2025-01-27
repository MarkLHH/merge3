import os
import shutil

def get_condole_width():
    size = shutil.get_terminal_size()
    return size.columns

def center_text(text):
    console_width = get_condole_width()
    return text.center(console_width)

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')
        
def print_spacer():
    print()