import os
import csv


# Function to process and modify CSV files
def process_csv_file(file_path):
    temp_file = file_path + ".tmp"

    with open(file_path, 'r', newline='', encoding='utf-8') as infile, \
            open(temp_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            modified_row = [value.replace(',', '-') if isinstance(value, str) else value for value in row]
            writer.writerow(modified_row)

    os.replace(temp_file, file_path)  # Replace the original file with the modified one


# Folder containing CSV files
csv_folder_path = r'D:\workspace\NBN_HIER\CHECK\csv_files'  # Update this with the actual folder path

# Process all CSV files in the folder
for file_name in os.listdir(csv_folder_path):
    if file_name.lower().endswith('.csv'):
        file_path = os.path.join(csv_folder_path, file_name)
        process_csv_file(file_path)

print("Processing complete.")
