import csv

# File paths
input_file = r'D:\workspace\to_DDG\LOAD_AXIS_SEG_COMMENTS_20250107.csv'  # Replace with your input file name
output_file =  r'D:\workspace\to_DDG\shar\LOAD_AXIS_SEG_COMMENTS_20250107.csv'   # Replace with your output file name

"""
# Function to clean double quotes in COMMENT_TEXT
def clean_comment_text(comment_text):
    return comment_text.replace('"', ' ')

# Process the CSV file
with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)

    # Write the header row (optional, if your file has headers)
    for row in reader:
        # Assuming COMMENT_TEXT is the 5th column (index 4)
        row[4] = clean_comment_text(row[4])
        writer.writerow(row)


"""

# Function to clean double quotes in COMMENT_TEXT
def clean_comment_text(comment_text):
    return comment_text.replace('"', ' ')

# Process the CSV file
with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header row (optional, if your file has headers)
    for row in reader:
        # Assuming COMMENT_TEXT is the 5th column (index 4)
        row[4] = clean_comment_text(row[4])
        writer.writerow(row)
