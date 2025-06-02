import pandas as pd
import os
import glob

def fix_csv(input_path, output_path):
    """
    Fix the CSV file by copying values from specific columns.
    - EffectiveStartMLTDttm to EffectiveEndUTCDttm
    - EffectiveStartMLTDttm to EffectiveEndMLTDttm
    - EffectiveStartUTCDttm to EffectiveStartMLTDttm
    """
    chunk_size = 10 ** 6  # Process in chunks of 1 million rows
    with pd.read_csv(input_path, chunksize=chunk_size) as reader:
        for i, chunk in enumerate(reader):
            # Update the columns as specified
            chunk['EffectiveEndUTCDttm'] = chunk['EffectiveStartMLTDttm']
            chunk['EffectiveEndMLTDttm'] = chunk['EffectiveStartMLTDttm']
            chunk['EffectiveStartMLTDttm'] = chunk['EffectiveStartUTCDttm']

            # Write to the output file
            if i == 0:
                chunk.to_csv(output_path, index=False, mode='w')  # Write header for the first chunk
            else:
                chunk.to_csv(output_path, index=False, mode='a', header=False)

def process_files(input_dir, output_dir):
    """
    Process all CSV files in the input directory and save them to the output directory.
    """
    csv_files = glob.glob(os.path.join(input_dir, "*202*.csv"))  # Find all CSV files in the folder
    if not csv_files:
        print(f"No CSV files found in {input_dir}")
        return

    for file in csv_files:
        input_path = file
        output_path = os.path.join(output_dir, os.path.basename(file))
        print(f"Processing {input_path}...")
        fix_csv(input_path, output_path)
        print(f"Processed file saved to {output_path}")

# Define input and output directories
input_directory = r"D:\workspace\SIIAM_7YEARS_HIST"
output_directory = r"D:\workspace\SIIAM_7YEARS_HIST\FIXED"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Process the files
process_files(input_directory, output_directory)
