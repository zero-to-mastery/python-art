# this project requires Pillow installation: https://pillow.readthedocs.io/en/stable/installation.html

# code credit goes to: https://www.hackerearth.com/practice/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
# code modified to work with Python 3 by @aneagoie
import argparse
import sys
import os
import re
from io import BytesIO
from bullet import Bullet, colors

from PIL import Image
import requests

from color.colored_term import ColorTerm, ANSIColor

ASCII_CHARS = ('#', '?', ' ', '.', '=', '+', '.', '*', '3', '&', '@')
color = ColorTerm()


def scale_image(image, clarity):
    """Resizes an image preserving the aspect ratio.
    """
    new_width = int(100*clarity)
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image


def convert_to_grayscale(image):
    return image.convert('L')


def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in
                       image.getdata()]

    return "".join(pixels_to_chars)


def convert_image_to_ascii(image, clarity):
    new_width = int(100*clarity)
    image = scale_image(image, clarity)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
                   range(0, len_pixels_to_chars, new_width)]
    return "\n".join(image_ascii)


def get_image_conversion(image_filepath, clarity):
    image = None

    try:
        image = Image.open(image_filepath)
    except:
        """
        If path entered is invalid or image not found,
        Tries to get image from the given image_filepath by assuming as URL
        This requires "requests" library to fecth data from url.
        """
        try:
            response = requests.get(image_filepath)
            image = Image.open(BytesIO(response.content))
        except FileNotFoundError as e:
            msg = f"Unable to open image file {image_filepath}."
            print(color.error(msg))
            print(e)
            return

    return convert_image_to_ascii(image, clarity)


def create_thumbnail(image_file_path):
    while True:
        msg = "Please enter the needed output size in pixels (Ex 1920x1080): "
        input_size = input(color.info(msg))

        if re.match(r'^[0-9]{1,}x[0-9]{1,}$', input_size):
            input_size = [int(size) for size in input_size.split('x')]
            break
        continue

    try:
        image = Image.open(image_file_path)
    except Exception as e:
        msg = f"Unable to open image file {image_file_path}."
        print(color.error(msg))
        print(e)
        return

    msg = f"Creating a thumbnail of size: {input_size[0]}x{input_size[1]}..."
    print(color.info(msg))

    size = int(input_size[0]), int(input_size[1])

    image_name, image_extention = os.path.splitext(image_file_path)
    image.thumbnail(size)
    image.save("{}-thumbnail{}".format(image_name,
                                       image_extention), image_extention[1:])

    msg = f"Thumbnail saved. Please check in the destination directory."
    print(color.success(msg))

    userChoices = Bullet(
        # Prompt for the user to see
        prompt="\n\tWould you like to see the image now?",
        # List of options to choose from
        choices=["Yes", "No"],
        # How much space to pad in from the start of the prompt
        align=5,
        # Spacing between the bullet and the choice
        margin=2,
        # Space between the prompt and the list of choices
        shift=1,
        # The foreground colour of the bullet
        bullet_color=colors.foreground["cyan"]
    )
    menu = userChoices.launch()
    choice = menu[0]
    if choice == 'Y':
        image.show()

    # msg_show_img = ""
    # reply = input(color.info(msg_show_img))
    # if len(reply) > 0 and reply[0] == 'y':
    #     image.show()


def save_text_to_file(ascii_art, filename):
    try:
        with open(filename, 'w') as out_file:
            out_file.write(ascii_art)
    except Exception:
        msg = f'Error: could not open \'{filename}\' for writing'
        print(color.error(msg))
        sys.exit()
    msg = f'Saved to \'{filename}\'.'
    print(color.success(msg))


def menu(image_file_path, clarity):
    options = [
        "A: Create an ASCII representation",
        "B: Create a colored ASCII representation",
        "C: Create a thumbnail",
        "Q: Quit/Log Out",
    ]

    while True:
        userChoices = Bullet(
            # Prompt for the user to see
            prompt="\n\tUse up & down arrows and hit enter to make choice:",
            # List of options to choose from
            choices=options,
            # How much space to pad in from the start of the prompt
            align=5,
            # Spacing between the bullet and the choice
            margin=2,
            # Space between the prompt and the list of choices
            shift=1,
            # The foreground colour of the bullet
            bullet_color=colors.foreground["cyan"]
        )

        menu = userChoices.launch()
        choice = menu[0]

        if choice.upper() == 'A' or choice.upper() == 'B':
            if choice.upper() == 'A':
                msg = f"\n Creating an ASCII representation of {image_file_path}: \n"
                color.disable()
            elif choice.upper() == 'B':
                msg = f"\n Creating a colored ASCII representation of {image_file_path}: \n"
                color.enable()

            print(color.info(msg))
            image_ascii = get_image_conversion(image_file_path, clarity)
            print(color.ascii_color_chars(image_ascii))

            while True:
                msg = '\nSave to file? '
                save = input(color.info(msg))

                if save.upper() == 'Y' or save.upper() == 'N':
                    if save.upper() == 'Y':
                        msg = 'Filename: '
                        save_text_to_file(image_ascii, input(color.info(msg)))
                    break
                else:
                    msg = 'Please enter \'Y\' or \'N\'.'
                    print(color.warning(msg))
                    continue

        elif choice.upper() == 'C':
            create_thumbnail(image_file_path)
        elif choice.upper() == 'Q':
            break
        else:
            msg = f"ERROR!\nYou must only select either A,B,C or Q.\nPlease try again."
            print(color.error(msg))

        print(f'\n\n')


def main():
    parser = argparse.ArgumentParser(description='Convert images to ASCII art')
    parser.add_argument('-i', '--image', help='Image filepath', required=True)
    parser.add_argument('-c', '--clarity', help='Image clarity (float)')

    args = parser.parse_args()

    image_file_path = args.image

    try:
        clarity = args.clarity
        clarity = float(clarity)
        if not clarity:
            clarity = 1
        elif clarity > 2:
            clarity = 2
    except Exception:
        clarity = 1
    try:
        menu(image_file_path, clarity)
    except KeyboardInterrupt:
        msg = "\nBye!"
        print(color.colored_string(msg, ANSIColor.MAGENTA))


if __name__ == '__main__':
    main()
