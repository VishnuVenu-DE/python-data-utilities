import pandas as pd
from datetime import datetime

# Function to change the date format from DD-MMM-YYYY HH:MM:SS to YYYYMMDDHHMMSS
def format_entry_date(date_str):
    try:
        return datetime.strptime(date_str, "%d-%b-%Y %H:%M:%S").strftime("%Y%m%d%H%M%S")
    except ValueError:
        return date_str  # If the date format is incorrect, return the original

# Read the large CSV in chunks and process
chunk_size = 10**6  # Process in chunks of 1 million rows
filename = r'D:\workspace\SIIAM_7YEARS_HIST\ACT_ENTRY\split_output\TABLE_ACT_ENTRY_1_new.csv'
output_filename = r'D:\workspace\SIIAM_7YEARS_HIST\ACT_ENTRY\split_output\act_entry_processed.csv'

chunk_iter = pd.read_csv(filename, chunksize=chunk_size)

for i, chunk in enumerate(chunk_iter):
    # Format the Entry_date column
    chunk['ENTRY_TIME'] = chunk['ENTRY_TIME'].apply(format_entry_date)

    # Update the file_name column to "TABLE_ACT_ENTRY_1"
    chunk['FILE_NAME'] = "TABLE_ACT_ENTRY_1"

    # Write the chunk to the output file (append mode)
    if i == 0:
        # Write the header for the first chunk
        chunk.to_csv(output_filename, mode='w', header=True, index=False)
    else:
        # Append the rest of the chunks without headers
        chunk.to_csv(output_filename, mode='a', header=False, index=False)

print(f"Processing completed. The output file is saved as {output_filename}.")
