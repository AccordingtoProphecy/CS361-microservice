from file_exists import file_exists
import time


def file_exists_service():
    # Continuously check if the file path exists
    while True:
        file_check = open('input.txt', 'r+')
        file_check_path = file_check.read()

        # Check if empty string
        if file_check_path == '':
            time.sleep(1)
            continue
        # Clear both files and exit program if input.txt contains 'exit'
        elif file_check_path == 'exit':
            input_clear = open('input.txt', 'w')
            output_clear = open('output.txt')
            input_clear.close()
            output_clear.close()
            return
        # Call file_exists and clear input.txt
        else:
            file_exists(file_check_path.strip(), 'output.txt')
            file_check.seek(0)
            file_check.truncate(0)

        file_check.close()


file_exists_service()
