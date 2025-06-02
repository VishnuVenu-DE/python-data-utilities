import re

# Define file paths
input_file_path = r"C:\Users\vishnu.venugopalan\Desktop\control-m QR changes\FILE WATCHER\changes\QBI_DFSSIID.xml"
replacement_values_path = r"C:\Users\vishnu.venugopalan\Desktop\control-m QR changes\FILE WATCHER\changes\automated\siiam_files.txt"
output_file_path = r"C:\Users\vishnu.venugopalan\Desktop\control-m QR changes\FILE WATCHER\changes\automated\QBI_DFSSIID_FINAL.xml"

# Read the replacement values from the text file
with open(replacement_values_path, 'r') as f:
    replacement_values = [line.strip() for line in f]

# Read the input file
with open(input_file_path, 'r') as f:
    lines = f.readlines()

# Define the pattern to match the string to be replaced
pattern = re.compile(r'(<AUTOEDIT2 NAME="%%PARM1" VALUE="&quot;-iddg_root/data/corporate/inbound/PRD/siiam/src/land/)(table_case)(&quot;"/>)')

# Function to replace the string with a new value
def replace_string(line, new_value):
    return pattern.sub(r'\1' + new_value + r'\3', line)

# Replace the strings in the file
updated_lines = []
replacement_index = 0

for line in lines:
    if pattern.search(line):
        if replacement_index < len(replacement_values):
            new_value = replacement_values[replacement_index]
            updated_lines.append(replace_string(line, new_value))
            replacement_index += 1
        else:
            updated_lines.append(line)  # If no more replacement values, keep the line unchanged
    else:
        updated_lines.append(line)  # If no match, keep the line unchanged

# Write the updated lines to the output file
with open(output_file_path, 'w') as f:
    f.writelines(updated_lines)

print(f"Replacement completed. Check '{output_file_path}' for the results.")
