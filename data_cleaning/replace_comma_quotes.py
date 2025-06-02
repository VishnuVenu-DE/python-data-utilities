import csv


def clean_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
            open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            cleaned_row = [field.replace(',', '-').replace('"', '-') for field in row]
            writer.writerow(cleaned_row)


if __name__ == "__main__":
    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_01.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_01.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_02.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_02.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_03.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_03.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_04.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_04.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_05.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_05.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_06.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_06.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_07.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_07.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_08.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_08.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_09.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_09.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_10.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_10.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_11.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_11.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_12.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_12.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_13.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_13.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_14.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_14.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_15.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_15.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_16.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_16.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_17.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_17.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_18.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_18.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_19.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_19.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_20.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_20.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_21.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_21.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")

    input_csv = r'D:\workspace\7YEARS_SIIAM_PROD\split_output\TABLE_CASE_CL_22.csv'  # Change to your input CSV file path
    output_csv = r'D:\workspace\7YEARS_SIIAM_PROD\TABLE_CASE_CL\TABLE_CASE_CL_22.csv'  # Change to your desired output file path
    clean_csv(input_csv, output_csv)
    print(f"Cleaned CSV saved to {output_csv}")



