import re

# Define the full path to the input file
input_file_path = r"C:\Users\vishnu.venugopalan\Desktop\control-m QR changes\FILE WATCHER\changes\automated\QBI_DFSSIID_1_updated.xml"
output_file_path = r"C:\Users\vishnu.venugopalan\Desktop\control-m QR changes\FILE WATCHER\changes\automated\QBI_DFSSIID_1_NEW.xml"

# Read the input file
with open(input_file_path, 'r') as f:
    lines = f.readlines()

# Define the pattern to match the OUTCOND lines
pattern = re.compile(r'<OUTCOND NAME="(QBIS0[0-9]{5}D)-DFSSIID-OK" ODATE="ODAT" SIGN="ADD"/>')

# Function to create the INCOND lines
def create_incond_lines(match):
    variable_part = match.group(1)
    return (f'<INCOND AND_OR="AND" NAME="{variable_part}-DFSSIID-OK" ODATE="PREV"/>\n'
            f'<INCOND AND_OR="AND" NAME="{variable_part}-DFSSIID-OK" ODATE="ODAT"/>\n')

# Process the lines
updated_lines = []
for line in lines:
    match = pattern.search(line)
    if match:
        incond_lines = create_incond_lines(match)
        updated_lines.append(incond_lines)  # Add the INCOND lines above
    updated_lines.append(line)  # Add the original line

# Write the updated lines to a new file
with open(output_file_path, 'w') as f:
    f.writelines(updated_lines)

print(f"Insertion completed. Check '{output_file_path}' for the results.")
