import os


def fix_line(line: str, expected_length: int):
    parts = line.strip().split()
    if len(parts) < 2:
        return None  # Skip if format is invalid
    table_name = parts[0]
    metadata = ''.join(parts[1:])

    if expected_length == 48:
        return f"{table_name:<32}{metadata:>16}"
    elif expected_length == 57:
        return f"{table_name:<32}{metadata:>25}"
    else:
        return None


def fix_dat_file(input_path, output_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()

    if len(lines) < 2:
        print(f"Skipping file (too short): {input_path}")
        return

    header_fixed = fix_line(lines[0], 48)
    trailer_fixed = fix_line(lines[-1], 57)

    if not header_fixed or not trailer_fixed:
        print(f"Invalid header/trailer format in {input_path}")
        return

    lines[0] = header_fixed + '\n'
    lines[-1] = trailer_fixed + '\n'

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as f:
        f.writelines(lines)

    print(f"✅ Saved fixed file: {output_path}")


# Input and output directories
input_dir = r'C:\Users\vishnu.venugopalan\Desktop\wdr_test'  # Change to your input folder path
output_dir = r'C:\Users\vishnu.venugopalan\Desktop\wdr_test\output'  # Change to your output folder path

for filename in os.listdir(input_dir):
    if filename.endswith(".dat"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        fix_dat_file(input_path, output_path)
