# This module appends color code instructions to strings so that the terminal displays colored text
# Reference: 

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
        self.RED = '\033[31m'
        self.GREEN = '\033[32m'
        self.BLUE = '\033[34m'
        self.MAGENTA = '\033[35m'
        self.RESET = '\033[0m'

    def colorful_string(self, text: str) -> str:
        """Add color codes based on some ascii character selection
        Characters used are: 3, &, =, +, *
        """
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
