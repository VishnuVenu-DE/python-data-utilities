import csv
from datetime import datetime


# Function to change the date format from DD-MMM-YYYY HH:MM:SS to YYYYMMDDHHMMSS
def format_entry_date(date_str):
    try:
        #return datetime.strptime(date_str, "%d-%b-%Y %H:%M:%S").strftime("%Y%m%d%H%M%S")
        return datetime.strptime(date_str, "%d-%b-%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return date_str  # If the date format is incorrect, return the original


# Open the original CSV file and the output CSV file
input_filename = r'D:\workspace\SIIAM_7YEARS_HIST\SET3_FACT_ASSURANCE_1.csv'
output_filename = r'D:\workspace\SIIAM_7YEARS_HIST\SET3_FACT_ASSURANCE_01_lates.csv'

with open(input_filename, 'r', newline='', encoding='utf-8') as infile, \
        open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    # Create a CSV DictWriter object to write to the output file
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    # Write the header to the output file
    writer.writeheader()

    # Process each row in the input file
    for row in reader:
        # Format the Entry_date column
        #row['CASE_CREATION_TIME'] = format_entry_date(row['CASE_CREATION_TIME'])
        #row['CASE_CLOSED_DATE'] = format_entry_date(row['CASE_CLOSED_DATE'])
        row['CALL_DATE'] = format_entry_date(row['CALL_DATE'])
        row['RESPONSE_DATE'] = format_entry_date(row['RESPONSE_DATE'])
        row['DISPATCH_DATE'] = format_entry_date(row['DISPATCH_DATE'])
        row['COMMIT_DATE'] = format_entry_date(row['COMMIT_DATE'])
        row['APPT_DATE'] = format_entry_date(row['APPT_DATE'])
        row['ACTL_RESTORE_DATE'] = format_entry_date(row['ACTL_RESTORE_DATE'])
        row['CLOSED_DATE'] = format_entry_date(row['CLOSED_DATE'])
        row['INT_DEL_DATE'] = format_entry_date(row['INT_DEL_DATE'])
        row['PRASSIST_REG_DATE'] = format_entry_date(row['PRASSIST_REG_DATE'])
        row['REPORT_DATE'] = format_entry_date(row['REPORT_DATE'])
        row['MAX_LEG_DATE'] = format_entry_date(row['MAX_LEG_DATE'])
        row['CSG_DATE'] = format_entry_date(row['CSG_DATE'])
        row['CSG_TAIL_DATE'] = format_entry_date(row['CSG_TAIL_DATE'])
        row['CSE_DATE'] = format_entry_date(row['CSE_DATE'])
        row['CSE_TAIL_DATE'] = format_entry_date(row['CSE_TAIL_DATE'])
        row['CSG_RESTORE_DATE'] = format_entry_date(row['CSG_RESTORE_DATE'])
        row['COPY_DATE'] = format_entry_date(row['COPY_DATE'])
        row['CALC_RESTORE_DATE'] = format_entry_date(row['CALC_RESTORE_DATE'])
        row['MPA_TARGET_DATE'] = format_entry_date(row['MPA_TARGET_DATE'])
        row['NRF_PROACT_DATE'] = format_entry_date(row['NRF_PROACT_DATE'])
        row['RESTORATION_COPY_DATE'] = format_entry_date(row['RESTORATION_COPY_DATE'])
        row['TRAD_MIN_DECL_DATE'] = format_entry_date(row['TRAD_MIN_DECL_DATE'])
        row['PIPS_MIN_DECL_DATE'] = format_entry_date(row['PIPS_MIN_DECL_DATE'])
        row['CASE_RESPONSE_TARGET'] = format_entry_date(row['CASE_RESPONSE_TARGET'])
        row['CASE_ACTUAL_RESPONSE'] = format_entry_date(row['CASE_ACTUAL_RESPONSE'])
        row['CASE_RESTORE_TARGET'] = format_entry_date(row['CASE_RESTORE_TARGET'])
        row['CASE_TEMP_RESTORE'] = format_entry_date(row['CASE_TEMP_RESTORE'])
        row['PB_MAX_LEG_DATE'] = format_entry_date(row['PB_MAX_LEG_DATE'])
        row['PB_EXEMPT_END_DATE'] = format_entry_date(row['PB_EXEMPT_END_DATE'])
        row['PB_RESTORED_DATE'] = format_entry_date(row['PB_RESTORED_DATE'])
        row['PB_RESTORE_TARGET'] = format_entry_date(row['PB_RESTORE_TARGET'])
        row['PB_STANDARD_TARGET'] = format_entry_date(row['PB_STANDARD_TARGET'])
        row['DATE_UPDATED'] = format_entry_date(row['DATE_UPDATED'])
        row['CLOSED_DT_TM'] = format_entry_date(row['CLOSED_DT_TM'])
        row['PB_LSD_END'] = format_entry_date(row['PB_LSD_END'])

        # Update the file_name column
       # row['FILE_NAME'] = "TABLE_ACT_ENTRY_1"

        # Write the modified row to the output file
        writer.writerow(row)

print(f"Processing completed. The output file is saved as {output_filename}.")
