# python-data-utilities
A collection of Python scripts for common file and data tasks like formatting, cleaning and processing

## 📂 Project Structure:

python_data_utilities/
* file_formatting/
* data_cleaning/
* excel_utilities/
* environment/

### 📁 file_formatting/
Scripts to format or update file structures:
- `add_header_trailer.py` – Adds header and trailer rows to structured data files.
- `add_quotes.py` – Wraps values in quotes for specific file formats.
- `filename_replace.py` – Renames or updates filenames based on patterns.
- `interchange_columns.py` – Swaps specified columns in a delimited file.
- `exchange_col_values.py` – Swaps values between columns based on conditions.

### 📁 data_cleaning/
Scripts to clean or transform data values:
- `change_date_format.py` – Converts date strings from one format to another.
- `compare_FA.py` – Compares files for field alignment or specific rules.
- `add_in_condition.py` – Adds or modifies values based on defined rules.

### 📁 excel_utilities/
Excel-based data manipulations:
- `excel_filering.py` – Filters Excel rows based on given conditions.

### 📁 environment/
Miscellaneous:
- `activate_this.py` – Environment setup or utility-related script.

---

## 🚀 How to Use

Each script is self-contained and can be executed from the command line.

### Example
```bash
python file_formatting/add_header_trailer.py input.dat output.dat
```
Some scripts may require modifying the input path, delimiter, or specific rule inside the script itself.

## 🧠 Key Concepts Used
- File I/O and text parsing
- Regular expressions
- CSV and Excel handling (pandas, openpyxl, etc.)
- Conditional logic and string manipulation
- Basic script automation

📌 PS:  These scripts were developed for on-demand data corrections and quick fixes rather than full-scale production pipelines. They are shared here to demonstrate my learning, problem-solving approach and hands-on experience with Python for data handling.
