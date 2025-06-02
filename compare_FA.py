import pandas as pd

# Specify the file paths
oracle_file_path = r'D:\workspace\FA_test\legacy_FA_CL_01Jul.csv'
sql_file_path = r'D:\workspace\FA_test\datacoe_fa_CL_01jul.csv'
comparison_result_path = r'D:\workspace\FA_test\comparison_result.csv'


# Read CSV files into DataFrames
df_oracle = pd.read_csv(oracle_file_path, delimiter=',')
df_sql = pd.read_csv(sql_file_path, delimiter=',')

# Ensure both DataFrames have the same columns and index
common_columns = df_oracle.columns.intersection(df_sql.columns)

# Reindex both DataFrames to have the same columns and reset index to ensure alignment
df_oracle = df_oracle[common_columns].sort_index(axis=1).reset_index(drop=True)
df_sql = df_sql[common_columns].sort_index(axis=1).reset_index(drop=True)

# Compare DataFrames
comparison_result = df_oracle.compare(df_sql)

# Save the comparison result to a CSV file for further analysis
comparison_result.to_csv(comparison_result_path)

# Print summary of discrepancies
print(f'Total discrepancies: {comparison_result.shape[0]}')
print(comparison_result.head())
