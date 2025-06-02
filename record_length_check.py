def check_line_length(file_path, target_length):
    """
    Reads a .dat file and identifies lines that do not match the target length.

    :param file_path: Path to the .dat file.
    :param target_length: The required length of each line.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        invalid_lines = [
            (index + 1, line.strip(), len(line.strip()))
            for index, line in enumerate(lines)
            if len(line.strip()) != target_length
        ]

        if invalid_lines:
            print(f"Lines with length not equal to {target_length}:")
            for line_number, content, length in invalid_lines:
                print(f"Line {line_number}: Length={length} | Content='{content}'")
        else:
            print(f"All lines have the correct length of {target_length}.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Specify the path to your .dat file and the target length
file_path = r'D:\workspace\NRF\full_nov\p\NRF_PLANT_NOV_DC.csv'   # Replace with your file path
target_length = 353

check_line_length(file_path, target_length)
