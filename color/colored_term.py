# This module appends color code instructions to strings so that the terminal displays colored text
# References:
# Activating VT100 on Windows 10 https://stackoverflow.com/questions/51091680/activating-vt100-via-os-system
# Color codes: 
# - https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
# - https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python

import platform
import os

class ANSIColor:
    """Holds the ANSI escaped color code sequences"""
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

class Color(ANSIColor):
    """Holds the color code instructions to be applied to any string that will be printed
    to the stdout. The following colors are implemented:
    BLUE
    GREEN
    RED
    MAGENTA
    Methods Implemented:
    colorful_ascii_chars(str) -> str
    Takes a string parameter and adds color codes based on ascii character selection
    Static Methods Implemented:
    colorful_string(str, ANSIColor) -> str
    Takes a string as the first paramenter and adds the color specified by the second parameter
    """
    def __init__(self):
        # Checks if OS is Windows to activate VT100
        # NOTE: this only works for Windows 10, prior Windows versions don't support ANSI escape sequences
        if platform.system() == 'Windows':
            os.system('')
        self.enabled = False

    def enable(self):
        """Enable color functionality"""
        self.enabled = True
    
    def disable(self):
        """Disable color functionality"""
        self.enabled = False

    def colorful_ascii_chars(self, text: str) -> str:
        """Add color codes based on some ascii character selection
        Characters used are: 3, &, =, +, *
        By defaul this is disable, make sure to call enable() before usage
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
                elif char == '#' or char == '?':
                    colored_text += self.CYAN + char + self.RESET
                else:
                    colored_text += char
            
            return colored_text
        else:
            return text

    @staticmethod
    def colorful_string(text: str, color: ANSIColor) -> str:
        """Adds ANSI color codes to the string
        colorful_string(string, ANSIColor) -> str
        Example:
        colorful_string('Hello', ANSIColor.RED) -> '\033[31mHello\033[0m'
        """
        return color + text + ANSIColor.RESET
