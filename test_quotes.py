import csv

# Input and output file paths
input_file = r"D:\workspace\SIIAM_OTL_NEW\to_PROD\cleaned\TABLE_X_TEST_RESULTS_OTL2.csv"
output_file = r"D:\workspace\SIIAM_OTL_NEW\to_PROD\cleaned\TABLE_X_TEST_RESULTS_OTL3.csv"


# Function to clean the CASE_HISTORY column
def clean_case_history(value):
    # Remove internal commas and quotes, not the enclosing ones
    return value.replace('"', '').replace(',', '')


# Process the CSV file
with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames  # Get the field names from the input file
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()  # Write the header to the output file

    for row in reader:
        # Clean the CASE_HISTORY column
        row['X_COMMENTS'] = clean_case_history(row['X_COMMENTS'])
        # Write the modified row to the output file
        writer.writerow(row)

print(f'Processed file saved as {output_file}')

