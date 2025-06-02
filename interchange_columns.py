import pandas as pd

# File paths
file_path = r"C:\Users\vishnu.venugopalan\Downloads\load_in_rass_progress.csv"
new_file_path = r'C:\Users\vishnu.venugopalan\Downloads\swapped_columns_file.csv'

# Define the chunksize (number of rows per chunk)
chunksize = 10000  # Adjust the chunk size depending on your system's memory

# Initialize a variable to track if it's the first chunk
is_first_chunk = True

# Read the CSV file in chunks
with pd.read_csv(file_path, chunksize=chunksize) as reader:
    for chunk in reader:
        # Swap the first and second columns
        cols = chunk.columns.tolist()  # Get the list of column names
        cols[0], cols[1] = cols[1], cols[0]  # Swap the first and second columns
        chunk = chunk[cols]  # Reorder the DataFrame based on the swapped columns

        # Write to the new file, append if it's not the first chunk
        if is_first_chunk:
            chunk.to_csv(new_file_path, index=False, mode='w')  # Write header for the first chunk
            is_first_chunk = False
        else:
            chunk.to_csv(new_file_path, index=False, mode='a', header=False)  # Append without header

print(f"New CSV file saved as {new_file_path}")
