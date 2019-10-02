# This module provides color functionality using the stdout
# It is compatible with Linux, UNIX, and Windows

class Color:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    BLACK = '\033[30m'
    MAGENTA = '\033[35m'
    END = '\033[0m'

# ASCII_CHARS = [ '#', '?', ' ', '.', '=', '+', '.', '*', '3', '&', '@']

    def color_full_string(self, str):
        colored_str = ''
        for char in str:
            if char == '3':
                colored_str += self.BLUE + char + self.END
            elif char == '&':
                colored_str += self.RED + char + self.END
            elif char == '=':
                colored_str += self.GREEN + char + self.END
            elif char == '*' or char == '+':
                colored_str += self.MAGENTA + char + self.END
            else:
                colored_str += char
        
        return colored_str
