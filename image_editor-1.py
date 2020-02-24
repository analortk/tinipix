import os.path

OPTION_RANGE = 6
HEADER_LENGTH = 3
LINE_LENGTH = 10


def greyscale(image_list):
    """ Convert the image_list to greyscale by replacing the r, g, b
        values with an average of the 3 values.

	:return image_list
	"""

    """ create our 2D structure of pixels from the image so we can work with individual pixels"""

    """ iterate over every pixel in the image """
    
    for x in image_list:
        avg = (x[0]+x[1]+x[2])/3
        image_list[image_list.index(x)] = (avg, avg, avg)
        print(image_list)
        
    return image_list
        
    
   
       



def only_red(image_list):
    """ Remove the green and blue channels in image_list by setting them
	to zero.

	:return image_list
	"""
    return image_list


def only_blue(image_list):
    """ Remove the green and red channels in image_list by setting them
	to zero.

	:return image_list
	"""

    return image_list


def only_green(image_list):
    """ Remove the blue and red channels in image_list by setting them
	to zero.

	:return image_list
	"""

    return image_list


def negative_red(image_list):
    """ Change the red channel in the image_list to its negative value
	by subtracting the value from 255.

	:return image_list
	"""

    return image_list


def negative_green(image_list):
    """ Change the green channel in image_list to its negative value
	by subtracting the value from 255.

	:return image_list
	"""
    return image_list


def negative_blue(image_list):
    """ Change the blue channel in the image to its negative value
	by subtracting the value from 255.

	:return image_list
	"""

    return image_list


def negative_image(image_list):
    """ Change image_list to a negative by subtracting the value
	of each pixel from 255.

	Hint: use somme of the other functions you've written.

	:return image_list
	"""

    return image_list


def extreme_contrast(image_list):
    """ Change pixels in image_list to either 0 or 255. If the current value is
	less than the midpoint, set to zero. If the current value is greater than
	the midpoint, set to 255.

	:return image_list
	"""

    return image_list


def print_menu():
    print("\n\n\toptions: ")
    print("\t\t[1]  convert to greyscale")
    print("\t\t[2]  just the reds")
    print("\t\t[3]  just the greens")
    print("\t\t[4]  just the blues")
    print("\t\t[5]  negative image")
    print("\t\t[6]  extreme contrast")


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

    output_image_filename = input("\n\tenter the name of the output file: ")

    prompt = "\n\tyour choice: "
    menu_choice = get_menu_option(prompt)

    if menu_choice == 1:
        greyscale(image_list)
    elif menu_choice == 2:
        only_red(image_list)
    elif menu_choice == 3:
        only_blue(image_list)
    elif menu_choice == 4:
        only_green(image_list)
    elif menu_choice == 5:
        negative_image(image_list)
    elif menu_choice == 6:
        extreme_contrast(image_list)
    write_image(rows, cols, image_list, output_image_filename)
    print("\nImage written to file", output_image_filename)
