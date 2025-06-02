import pandas as pd
from datetime import datetime

# Function to format the date columns
def format_date_column(df, column_name):
    if column_name in df.columns:
        df[column_name] = pd.to_datetime(df[column_name], errors='coerce')  # Convert to datetime
        df[column_name] = df[column_name].dt.strftime('%d/%m/%Y %H:%M')  # Format to desired format
    return df

# File paths
input_csv = r'D:\workspace\NRF\full_nov\p\rpt5965_d4493_case_NOV_DC.csv'  # Replace with your input CSV file path
output_csv = r'D:\workspace\NRF\full_nov\p\CASE.csv'  # Replace with your desired output CSV file path

# Read the CSV file
df = pd.read_csv(input_csv)

# List of columns to format
columns_to_format = [
    "DATE_IN",
    "CASE_RESTORE_TARGET",
    "RESTORE_DATE",
    "CLOSED_DATE"
]

# Apply formatting to specified columns
for column in columns_to_format:
    df = format_date_column(df, column)

# Save the updated DataFrame to a new CSV file
df.to_csv(output_csv, index=False)

print(f"Date formats updated and saved to {output_csv}")
