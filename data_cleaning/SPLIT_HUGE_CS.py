import os
import csv
file_count = 47
def split_csv(input_file, output_dir, max_size_mb=3072):
    global file_count
    # Calculate the max size in bytes
    max_size = max_size_mb * 1024 * 1024

    # Open the input CSV file
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        headers = next(reader)

        # Initialize variables for the split files

        current_file_size = 0
        output_file = None
        writer = None

        def write_header_and_open_new_file():
            nonlocal current_file_size,  output_file, writer
            global file_count
            if output_file:
                output_file.close()
            output_file_name = os.path.join(output_dir, f"TABLE_ACT_ENTRY_{file_count}.csv")
            output_file = open(output_file_name, mode='w', newline='', encoding='utf-8')
            writer = csv.writer(output_file)
            writer.writerow(headers)
            current_file_size = 0
            file_count += 1

        # Start by creating the first output file
        write_header_and_open_new_file()

        # Write rows to the file, splitting as needed
        for row in reader:
            row_size = len(','.join(row).encode('utf-8'))
            if current_file_size + row_size > max_size:
                write_header_and_open_new_file()
                #break;

            writer.writerow(row)
            current_file_size += row_size

        if output_file:
            output_file.close()

# Usage
input_file = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_ACT_ENTRY\TABLE_ACT_ENTRY_2023.csv'  # Path to your input CSV file
output_dir = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_ACT_ENTRY\split_output'         # Directory where the output files will be saved

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

split_csv(input_file, output_dir)

input_file = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_ACT_ENTRY\TABLE_ACT_ENTRY_2022.csv'
split_csv(input_file, output_dir)

input_file = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_ACT_ENTRY\TABLE_ACT_ENTRY_2021.csv'
split_csv(input_file, output_dir)