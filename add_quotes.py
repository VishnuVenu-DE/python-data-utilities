import csv

#input_file = r"D:\workspace\SIIAM_OTL_NEW\new\06Sep2024\TABLE_CASE_OTL.csv"   # Input CSV file path
#output_file = r"D:\workspace\SIIAM_OTL_NEW\new\06Sep2024\quoted\TABLE_CASE_OTL.csv"  # Output CSV file path


input_file = r'C:\Users\vishnu.venugopalan\Desktop\ideal_t_di_pso_endconfig_250507.csv'  # Input CSV file path
output_file = r'C:\Users\vishnu.venugopalan\Desktop\NEW_ideal_t_di_pso_endconfig_250507.csv'  # Output CSV file path


with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)

    for row in reader:
        writer.writerow(row)

print(f"Processed file saved as {output_file}")

#
#
#
#

#
#