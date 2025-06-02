import re

# Define the full path to the input file
input_file_path = r"C:\Users\vishnu.venugopalan\Desktop\control-m QR changes\FILE WATCHER\changes\automated\QBI_DFSSIID_1.xml"
strings_to_replace = r"C:\Users\vishnu.venugopalan\Desktop\control-m QR changes\FILE WATCHER\changes\automated\strings_to_replace.txt"

# Read the file containing the new strings to replace
with open(strings_to_replace, 'r') as f:
    new_strings = [line.strip() for line in f]

# Read the input file
with open(input_file_path, 'r') as f:
    lines = f.readlines()

# Define a pattern to match the target string in the specific format
pattern = re.compile(r'(<DOCOND NAME="QBIS0[0-9]{5}K)(-DFSSIID-OK" ODATE="ODAT" SIGN="ADD"/>)')

# Function to replace the matched string with the corresponding new string
def replace_line(line, new_string):
    return pattern.sub(r'\1' + new_string + r'\2', line)

# Replace the strings in the file
updated_lines = []
new_string_index = 0

for line in lines:
    if pattern.search(line):
        updated_lines.append(replace_line(line, new_strings[new_string_index]))
        new_string_index += 1
    else:
        updated_lines.append(line)

# Write the updated lines to a new file
output_file_path = r"C:\Users\vishnu.venugopalan\Desktop\control-m QR changes\FILE WATCHER\changes\automated\QBI_DFSSIID_1_updated.xml"
with open(output_file_path, 'w') as f:
    f.writelines(updated_lines)

print(f"Replacement completed. Check '{output_file_path}' for the results.")
