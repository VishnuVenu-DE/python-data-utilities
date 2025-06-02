import os

# Constants
l_batch_id = "786"
odate_timestamp = "20240705030358"
directory_path = r"C:\Users\vishnu.venugopalan\Desktop\WDR shar may\hd_tl"

# Function to add header and trailer to a file
def add_header_trailer(file_path, l_batch_id, odate_timestamp):
    formatted_name = os.path.basename(file_path).replace(".dat", "").upper()
    file_name = formatted_name[5:]
    header = f"H{file_name.ljust(30)}{l_batch_id.zfill(3)}{odate_timestamp}"
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data_count = len(lines)
    trailer = f"T{file_name.ljust(30)}{l_batch_id.zfill(3)}{odate_timestamp}{str(data_count).zfill(9)}"

    with open(file_path, 'w') as file:
        file.write(header + '\n')
        file.writelines(lines)
        file.write(trailer + '\n')

# Iterate over all .dat files in the directory and add header and trailer
for file_name in os.listdir(directory_path):
    if file_name.endswith(".dat"):
        file_path = os.path.join(directory_path, file_name)
        add_header_trailer(file_path, l_batch_id, odate_timestamp)

print("Header and trailer lines added to all .dat files.")
