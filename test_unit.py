# Python library imports
import os

# Dependencies imports
from pytest import raises, fixture
from requests.exceptions import MissingSchema
from PIL import Image

# Local project imports
from make_art import get_image_conversion, convert_image_to_ascii

# Testing constants

TEST_IMG = 'test_img.png'

# Setups

@fixture()
def create_temp_file():
    """Create a temporary image file"""
    img = create_temp_pil_obj()
    img.save(TEST_IMG)
    yield
    remove_temp_file()

def remove_temp_file():
    """Remove temporary image file"""
    os.remove(TEST_IMG)

def create_temp_pil_obj():
    """Creates and returns a temporary Pillow object"""
    return Image.new('RGB', (60, 60), color = 'red')


# Test cases

def test_image_does_not_exists():
    """Tests if a failed image path throws error"""
    # By default get_image_conversion throws a MissingSchema
    # exception when the image path and/or url does not exists
    with raises(MissingSchema):
        assert get_image_conversion(None, 1)

def test_image_to_ascii():
    """Test the image is converted to ascii based string"""
    img = create_temp_pil_obj()
    ascii_string = convert_image_to_ascii(img, 1)
    assert type(ascii_string) == type('string')

def test_image_conversion(create_temp_file):
    """Test the image path exists and is converted to ascii"""
    # If the image exists, get_image_conversion returns an string
    converted_img = get_image_conversion(TEST_IMG, 1)
    assert type(converted_img) == type('string')