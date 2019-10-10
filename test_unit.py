# Python library imports
import os
import unittest

# Dependencies imports
from requests.exceptions import MissingSchema
from PIL import Image

# Local project imports
import make_art as ma

# Helper functions

def create_pillow_object():
    """Creates and returns a temporary Pillow object"""
    return Image.new('RGB', (100, 100), color = 'red')


# Test cases

class TestFilePath(unittest.TestCase):
    """Test if file paths"""
    TEST_PATH = 'test_file'

    @classmethod
    def teardown_class(cls):
        """Remove temporary file"""
        os.remove(cls.TEST_PATH)
        
    def test_image_does_not_exists(self):
        """Test if a failed image path throws an error"""
        # By default get_image_conversion throws a MissingSchema
        # exception when the image path and/or url does not exists
        with self.assertRaises(MissingSchema):
            ma.get_image_conversion(None, 1)
    
    def test_saved_text_to_file(self):
        """Test if the ascii convertion was saved as a file"""
        img = create_pillow_object()
        ascii_string = ma.convert_image_to_ascii(img, 1)
        ma.save_text_to_file(ascii_string, self.TEST_PATH)

        self.assertTrue(os.path.exists(self.TEST_PATH))

    def test_created_thumbnail(self):
        """Test if a thumbnail image file is created"""
        pass


class TestPillowObject(unittest.TestCase):
    """Test if pillow objects are returned"""
    def create_pillow_object(self):
        """Creates and returns a temporary Pillow object"""
        return Image.new('RGB', (100, 100), color = 'red')

    def test_scale_image(self):
        """Test if a pillow object is returned"""
        img = create_pillow_object()
        test_img = ma.scale_image(img, 1)
        
        self.assertEqual(type(img), type(test_img))

    def test_convert_to_grayscale(self):
        """Test if a pillow object is returned"""
        img = create_pillow_object()
        test_img = ma.convert_to_grayscale(img)
        
        self.assertEqual(type(img), type(test_img))


class TestConvertions(unittest.TestCase):
    """Test cases for image convertion to strings"""
    TEST_PATH = 'test_img.png'

    @classmethod
    def setup_class(cls):
        """Create temporary file"""
        img = create_pillow_object()
        img.save(cls.TEST_PATH)
    
    @classmethod
    def teardown_class(cls):
        """Remove temporary file"""
        os.remove(cls.TEST_PATH)

    def test_image_conversion(self):
        """Test the image path exists and is converted to ascii"""
        # If the image exists, get_image_conversion returns an string
        converted_img = ma.get_image_conversion(self.TEST_PATH, 1)

        self.assertEqual(type(converted_img), type('string'))

    def test_image_to_ascii(self):
        """Test the image is converted to ascii based string"""
        img = create_pillow_object()
        ascii_string = ma.convert_image_to_ascii(img, 1)

        self.assertEqual(type(ascii_string), type('string'))

    def test_image_to_ascii_chars(self):
        """Test the image is converted to ascii character string"""
        img = create_pillow_object()
        new_width = int(100)
        img = ma.scale_image(img, 1)
        img = ma.convert_to_grayscale(img)
        ascii_string = ma.map_pixels_to_ascii_chars(img)

        self.assertEqual(type(ascii_string), type('string'))
        
