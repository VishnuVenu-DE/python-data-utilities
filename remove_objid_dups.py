import pandas as pd

# Step 1: Load the CSV file
file_path = r"D:\workspace\SIIAM_OTL_NEW\new\09Sep2024\TABLE_EMPLOYEE_OTL.csv"
cleaned_file = r"D:\workspace\SIIAM_OTL_NEW\new\09Sep2024\cleaned\TABLE_EMPLOYEE_OTL.csv"
df = pd.read_csv(file_path,low_memory=False)

# Step 2: Remove duplicates based on the 'OBJID' column
df_dedup = df.drop_duplicates(subset='OBJID')

# Step 3: Reset the index and update the row numbers
df_dedup = df_dedup.reset_index(drop=True)
df_dedup['FILE_RECORD_ROW_NUMBER'] = df_dedup.index + 1
df_dedup['FileLineNumber'] = df_dedup.index + 1

# Step 4: Save the cleaned data back to a CSV file
df_dedup.to_csv(cleaned_file, index=False)
