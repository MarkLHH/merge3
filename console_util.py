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

def input_check(string_input):
        num = '1234567890'
        for i in string_input:
            if i not in num:
                return False
        return True
        
def print_spacer():
    print()