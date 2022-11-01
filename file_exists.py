from PIL import Image
import time


def file_exists(input_path, output_path):
    # Check if there's an output file
    try:
        open(output_path)
    except:
        print("ERROR: Invalid output path")
        return

    # Check if the input file actually exists
    try:
        open(input_path)
    except:
        false_output = open(output_path, 'w')
        false_output.write('does not exist')
        false_output.close()
        return

    # If file is an image, get dimensions and write to output file
    if str(input_path).lower().endswith('.png') or str(input_path).lower().endswith('.jpg'):
        input_image = Image.open(input_path)

        input_width = input_image.width
        input_height = input_image.height

        output_file = open(output_path, 'w')
        output_text = 'exists, ' + str(input_width) + ', ' + str(input_height)
        output_file.write(output_text)

        output_file.close()
        input_image.close()

        return
    else:
        print('ERROR: File is not .jpg or .png')
        return
