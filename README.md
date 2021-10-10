# CSV_Append
This script will append multiple CSV files that have similar case sensitive column headers.
CSV files with different columns headers will be appended at the end (See example).

Example: 
First CSV columns  (Last Name, first name, DOB, Address)
Second CSV columns (last name, first name, DOB, Address)

| Last Name | first name | DOB      | Address    | last name |
|-----------|------------|----------|------------|-----------|
| smith     | john       | 1/1/2000 | 123 main   |           |
| martin    |            | 1/2/2001 | 456 main   |           |
|           | mary       | 2/2/2003 | 789 valley | jane      |
|           | peter      | 5/6/1998 | 135 NY     | parker    |

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pandas.

```bash
pip install pandas
```

## How to Use:
-Create a new folder with name "FILES_TO_APPEND" at the same directory level (Skip this step if the file is already created)

-Move two or more CSV files to the "FILES_TO_APPEND" folder

-Run script

-After the script is run, CSV file named OUTPUT will be created in the same directory with CSV_Append.py
