import os
import re


def fix_line(line: str, total_length: int, numeric_length: int):
    line = line.strip()

    # Extract numeric part from the end
    match = re.search(rf"(\d{{{numeric_length}}})$", line)
    if not match:
        return None  # Invalid line format

    numeric_part = match.group(1)
    table_name = line[:line.rfind(numeric_part)].strip()

    # Calculate spaces needed before numeric part
    padded_line = f"{table_name}{' ' * (total_length - len(table_name) - numeric_length)}{numeric_part}"

    # Final safety check
    if len(padded_line) != total_length:
        return None

    return padded_line


def fix_dat_file(input_path, output_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()

    if len(lines) < 2:
        print(f"Skipping file (too short): {input_path}")
        return

    header_fixed = fix_line(lines[0], total_length=48, numeric_length=17)
    trailer_fixed = fix_line(lines[-1], total_length=57, numeric_length=26)

    if not header_fixed or not trailer_fixed:
        print(f"❌ Invalid header/trailer format in {input_path}")
        return

    lines[0] = header_fixed + '\n'
    lines[-1] = trailer_fixed + '\n'

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as f:
        f.writelines(lines)

    print(f"✅ Fixed file saved: {output_path}")


# Paths
input_dir = r'C:\Users\vishnu.venugopalan\Desktop\wdr_test\20250522\22ndMay'  # Change to your input folder path
output_dir = r'C:\Users\vishnu.venugopalan\Desktop\wdr_test\20250522\output'  # Change to your output folder path

for filename in os.listdir(input_dir):
    if filename.endswith('.dat'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        fix_dat_file(input_path, output_path)
