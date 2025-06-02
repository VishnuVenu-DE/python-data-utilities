import csv
from datetime import datetime


# Function to change the date format from DD-MMM-YYYY HH:MM:SS to YYYYMMDDHHMMSS
def format_entry_date(date_str):
    try:
        return datetime.strptime(date_str, "%d-%b-%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return date_str  # If the date format is incorrect, return the original




print(format_entry_date("08-DEC-2010 16:75:13"))




