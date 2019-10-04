# This module appends color code instructions to strings so that the terminal displays colored text
# References:
# Activating VT100 on Windows 10 https://stackoverflow.com/questions/51091680/activating-vt100-via-os-system
# Color codes: 
# - https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
# - https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python

import platform
import os


class Color:
    """Holds the color code instructions to be applied to any string that will be printed
    to the stdout. The following colors are implemented:
    BLUE
    GREEN
    RED
    MAGENTA
    Methods Implemented:
    colorful_string(str) -> str
    Takes a string parameter and adds color codes based on ascii character selection
    """
    def __init__(self):
        # ANSI escape senquence color codes
        self.RED = '\033[31m'
        self.GREEN = '\033[32m'
        self.BLUE = '\033[34m'
        self.MAGENTA = '\033[35m'
        self.RESET = '\033[0m'
        # Checks of OS is windows to activate VT100
        # NOTE: this only works for Windows 10, prior Windows versions don't support ANSI escape sequences
        if platform.system() == 'Windows':
            os.system('')

    def enable(self):
        """Enable color functionality"""
        self.enabled = True
    
    def disable(self):
        """Disable color functionality"""
        self.enabled = False

    def colorful_string(self, text: str) -> str:
        """Add color codes based on some ascii character selection
        Characters used are: 3, &, =, +, *
        """
        if self.enabled:
            colored_text = ''

            for char in text:
                if char == '3':
                    colored_text += self.BLUE + char + self.RESET
                elif char == '&':
                    colored_text += self.RED + char + self.RESET
                elif char == '=':
                    colored_text += self.GREEN + char + self.RESET
                elif char == '+' or char == '*':
                    colored_text += self.MAGENTA + char + self.RESET
                else:
                    colored_text += char
            
            return colored_text
        else:
            return text
