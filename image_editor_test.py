import unittest
import image_editor

class TestStringMethods(unittest.TestCase):

    def test_only_red(self):
        input = image_editor.only_red(image_editor.read_image('tinypix.ppm'))
        expected_output = image_editor.read_image('expected_red_output.ppm')
        self.assertEqual(input, expected_output)

if __name__ == '__main__':
    unittest.main()
