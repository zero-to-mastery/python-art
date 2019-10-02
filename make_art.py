# this project requires Pillow installation: https://pillow.readthedocs.io/en/stable/installation.html

# code credit goes to: https://www.hackerearth.com/practice/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
# code modified to work with Python 3 by @aneagoie
from PIL import Image
ASCII_CHARS = ['#', '?', ' ', '.', '=', '+', '.', '*', '3', '&', '@']


def scale_image(image, clearity):
    """Resizes an image preserving the aspect ratio.
    """
    new_width = int(100*clearity)
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

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in
                       pixels_in_image]

    return "".join(pixels_to_chars)


def convert_image_to_ascii(image, clearity):
    new_width = int(100*clearity)
    image = scale_image(image, clearity)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
                   range(0, len_pixels_to_chars, new_width)]
    return "\n".join(image_ascii)


def handle_image_conversion(image_filepath, clearity):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception as e:
        print(f"Unable to open image file {image_filepath}.")
        print(e)
        return

    image_ascii = convert_image_to_ascii(image, clearity)
    print(image_ascii)


def create_thumbnail(image_file_path):
    input_size = int(input("Please enter the needed output size in pixels: "))
    size = (input_size, input_size)

    try:
        image = Image.open(image_file_path)
    except Exception as e:
        print(f"Unable to open image file {image_file_path}.")
        print(e)
        return

    print(
        f"Creating a thumbnail in the current directory (size: {input_size}X{input_size})...")

    image_name, image_extention = image_file_path.split(".")
    image.thumbnail(size)
    image.save(image_name + ".thumbnail." + image_extention, image_extention)

    print("Thumbnail created. Please check in the current directory.")


def menu():
    choice = input("""
                      A: Create an ASCII representation
                      B: Create a thumbnail
                      Q: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice == "a":
        print(f"\n Creating an ASCII representation of {image_file_path}: \n")
        handle_image_conversion(image_file_path, clearity)
    elif choice == "B" or choice == "b":
        create_thumbnail(image_file_path)
    elif choice == "Q" or choice == "q":
        sys.exit
    else:
        print("You must only select either A,B or Q")
        print("Please try again")


if __name__ == '__main__':
    import sys

    image_file_path = sys.argv[1]
    try:
        clearity = sys.argv[2]
        clearity = float(clearity)
        if not clearity:
            clearity = 1
        elif clearity > 2:
            clearity = 2
    except:
        clearity = 1

    menu()
