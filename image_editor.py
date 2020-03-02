# Student numbers: 18068712 and 18098087

import os.path

OPTION_RANGE = 8
HEADER_LENGTH = 3
LINE_LENGTH = 10
import pdb;

def greyscale(image_list):

    """
	Image list is an array of arrays, in other words, is a list of pixels containing RGB values in a list.
	For a greyscale filter, it is required that each pixel's RGB value is replaced by the average of the RGB value for that pixel.
	The int (integer) function is used so that the average RGB value is returned as an integer, as RGB values cannont be floats (contain decimals).
	A for loop is used so that each individual red, green and blue value is assigned the average value.
	:return image_list
	"""

    for rgb in image_list :
        
        avg = int((rgb[0] + rgb[1] + rgb[2]) / 3)

        rgb[0] = avg
        rgb[1] = avg
        rgb[2] = avg

    return image_list


def only_red(image_list):
    '''
    Image list is an array of arrays, in other words, is a list of pixels containing RGB values in a list.
    For the only red filter, it is required that each pixels green and blue value is set to zero, while the red value remains unchanged.
    For example, the pixel [150,25,67] is changed to [150,0,0].
    :return image_list
    '''

    for rgb in image_list :

        rgb[1] = 0
        rgb[2] = 0
        
    return image_list



def only_blue(image_list):

    '''
    Image list is an array of arrays, in other words, is a list of pixels containing RGB values in a list.
    For the only blue filter, it is required that each pixels red and green value is set to zero, while the blue value remains unchanged.
    For example, the pixel [150,25,67] is changed to [0,0,67].
    :return image_list
    '''

    for rgb in image_list :
        
        rgb[0] = 0
        rgb[1] = 0

    
    return image_list


def only_green(image_list):

    '''
    Image list is an array of arrays, in other words, is a list of pixels containing RGB values in a list.
    For the only green filter, it is required that each pixels red and blue value is set to zero, while the green value remains unchanged.
    For example, the pixel [150,25,67] is changed to [0,25,0].
    :return image_list
    '''

    for rgb in image_list :

        rgb[0] = 0

        rgb[2] = 0

    return image_list


def negative_red(image_list):
    """
	Image list is an array of arrays, in other words, is a list of pixels containing RGB values in a list.
    For the negative red filter, it is required that each pixels red value is changed to 255 minus its inital value, while the green and blue
    values remain unchanged.
    For example, the pixel [150,25,67] is changed to [105,25,67].
    :return image_list
	"""

    for rgb in image_list :
        
        rgb[0] = 255 - rgb[0]

    return image_list


def negative_green(image_list):
    """
	Image list is an array of arrays, in other words, is a list of pixels containing RGB values in a list.
    For the negative green filter, it is required that each pixels green value is changed to 255 minus its inital value, while the red and blue
    values remain unchanged.
    For example, the pixel [150,25,67] is changed to [150,230,67].
    :return image_list
	"""

    for rgb in image_list :
        
        rgb[1] = 255 - rgb[1]

    return image_list


def negative_blue(image_list):
    """
	Image list is an array of arrays, in other words, is a list of pixels containing RGB values in a list.
    For the negative blue filter, it is required that each pixels blue value is changed to 255 minus its inital value, while the red and green
    values remain unchanged.
    For example, the pixel [150,25,67] is changed to [150,25,188].
    :return image_list
	"""

    for rgb in image_list :
        
        rgb[2] = 255 - rgb[2]

    return image_list


def negative_image(image_list):
    """
	Image list is an array of arrays, in other words, is a list of pixels containing RGB values in a list.
    For the negative image filter, it is required that each pixels red, blue and green value is changed to 255 minus its inital value.
    For example, the pixel [150,25,67] is changed to [105,230,188].
    :return image_list
	"""

    for rgb in image_list :
        
        rgb[0] = 255 - rgb[0]
        rgb[1] = 255 - rgb[1]
        rgb[2] = 255 - rgb[2]

    return image_list


def extreme_contrast(image_list):
    """ Change pixels in image_list to either 0 or 255. If the current r, g or b value is
	less than the 127, set to zero. If the current r, g or b  value is greater than
	the 127, set to 255.
	:return image_list

	"""
    for rgb in image_list :
        
        if rgb[0] < 127:
            rgb[0] = 0
        else:
            rgb[0] = 255

        if rgb[0] < 127:
            rgb[1] = 0
        else:
            rgb[1] = 255
            
        if rgb[0] < 127:
            rgb[2] = 0
        else:
            rgb[2] = 255

    return image_list

def sepia_filter(image_list):
    '''
    Image list is an array of arrays, in other words, is a list of pixels containing RGB values in a list.
    This function calculates weighted values (sepia effect) for the rgb values of each pixel and then checks if the new calculated values
    are greater than 255, as no pixel value can be greater than 255.
    :return image_list
    '''

    for rgb in image_list :

        sep_red = int(rgb[0] * 0.393 + rgb[1] * 0.769 + rgb[2] * 0.189)
        sep_green = int(rgb[0] * 0.349 + rgb[1] * 0.686 + rgb[2] * 0.168)
        sep_blue = int(rgb[0] * 0.272 + rgb[1] * 0.534 + rgb[2] * 0.131)

        if sep_red > 255 :
            sep_red = 255

        if sep_green > 255 :
            sep_green = 255

        if sep_blue > 255 :
            sep_blue = 255

        rgb[0] = sep_red
        rgb[1] = sep_green
        rgb[2] = sep_blue

    return image_list

def black_white(image_list):
    '''
    This function is similar to extreme contrast but used the average of the rgb values for each pixel to determine
    where the r, g or b values should be assigned a zero or 255. It is an alternative way to create a black and white image.
    :return image_list
    '''

    for rgb in image_list :

        avg = int((rgb[0]+rgb[1]+rgb[2])/3)

        if avg < 128 :
            rgb[0] = 0
            rgb[1] = 0
            rgb[2] = 0
        else :
            rgb[0] = 255
            rgb[1] = 255
            rgb[2] = 255


    return image_list

def print_menu():
    print("\n\n\toptions: ")
    print("\t\t[1]  convert to greyscale")
    print("\t\t[2]  just the reds")
    print("\t\t[3]  just the greens")
    print("\t\t[4]  just the blues")
    print("\t\t[5]  negative image")
    print("\t\t[6]  extreme contrast")
    print("\t\t[7]  sepia filter")
    print("\t\t[8]  black and white")


def get_menu_option(prompt):

    valid_option = False

    while not valid_option:
        print_menu()
        try:
            option = int(input(prompt))
            if option in range(1, OPTION_RANGE + 1):
                valid_option = True
            else:
                raise ValueError
        except ValueError:
            print("\n\n\tthat's not a valid choice, please try again.")
    return option


def get_valid_filename(prompt):
    """Use prompt (a string) to ask the user to type the name of a file. If
	the file does not exist, keep asking until they give a valid filename.
	Return the name of that file.
	"""

    filename = input(prompt)
    while not os.path.exists(filename):
        print("That file does not exist.")
        filename = input(prompt)
    return filename


def get_dimensions(input_filename):
    """ Read the image size from the file header.
		Return a tuple containing the number of rows and columns.
	"""

    with open(input_filename, "r") as file:
        file.readline()
        dimensions = file.readline().split()
    rows = int(dimensions[0])
    cols = int(dimensions[1])

    return rows, cols


def get_file_contents(input_filename):
    """
	Return the tokens in the file as a list.
	Ignore the file header.
	"""

    line_count = 1
    read_data = []

    with open(input_filename, "r") as file:

        for line in file:
            # ignore the header
            if line_count <= HEADER_LENGTH:
                line_count += 1
            else:
                read_data += line.split()
    return read_data


def read_image(input_filename):
    """
	Return a list of the pixels in the file.
	"""

    read_data = get_file_contents(input_filename)

    # convert all the ascii pixel values to numbers
    read_data = [int(x) for x in read_data]

    # put the r,g,b values in a list
    all_pixels = []
    for i in range(0, len(read_data), 3):
        rgb = read_data[i : i + 3]
        all_pixels.append(rgb)
    return all_pixels


def write_image(rows, cols, image, output_filename):
    """ Write the list of pixels to a file. """

    with open(output_filename, "w") as file:
        file.write("P3\n")
        file.write(str(rows) + " " + str(cols) + "\n")
        file.write("255\n")

        for i in range(len(image)):
            for channel in image[i]:
                file.write(str(channel))
                file.write(" ")
            file.write("\t")

            if i % LINE_LENGTH == 0:
                file.write("\n")


if __name__ == "__main__":

    print("Welcome to the Portable Pixmap (PPM) Image Editor!")

    prompt = "\n\tenter the name of the image file: "
    input_image_filename = get_valid_filename(prompt)

    # This isn't a very efficient approach but it's best for the coursework
    rows, cols = get_dimensions(input_image_filename)

    image_list = read_image(input_image_filename)
    
    print('\n\tadd ".ppm" to the end of the filename so that the output is an image')
    output_image_filename = input("\n\tenter the name of the output file : ")

    prompt = "\n\tyour choice: "
    menu_choice = get_menu_option(prompt)

    if menu_choice == 1:
        greyscale(image_list)
    elif menu_choice == 2:
        only_red(image_list)
    elif menu_choice == 3:
        only_green(image_list)
    elif menu_choice == 4:
        only_blue(image_list)
    elif menu_choice == 5:
        negative_image(image_list)
    elif menu_choice == 6:
        extreme_contrast(image_list)
    elif menu_choice == 7:
        sepia_filter(image_list)
    elif menu_choice == 8:
        black_white(image_list)
    write_image(rows, cols, image_list, output_image_filename)
    print("\nImage written to file", output_image_filename)
