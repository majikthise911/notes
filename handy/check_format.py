import os
import pandas as pd

# Define the directory and example file
directory_path = 'C:\\Users\\jclay\\Desktop\\BESS'
example_file_name = 'Anson-II_BESS_SG-PT1_1hr_BE_SOV_2023.07.14.xlsx'

# Full path to the example file
example_file_path = os.path.join(directory_path, example_file_name)

# Read the example file to determine the expected structure
example_df = pd.read_excel(example_file_path)
expected_columns = example_df.columns.tolist()
expected_row_count = len(example_df)

def file_structure_matches(file_path, expected_columns, expected_row_count):
    try:
        df = pd.read_excel(file_path)
        # Check if the structure matches (columns and row count)
        if set(df.columns) == set(expected_columns) and len(df) == expected_row_count:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

# Iterate through each file in the directory and compare its structure to the example
for filename in os.listdir(directory_path):
    # Skip the example file itself
    if filename.endswith('.xlsx') and filename != example_file_name:
        file_path = os.path.join(directory_path, filename)
        if file_structure_matches(file_path, expected_columns, expected_row_count):
            print(f"{filename} matches the example file structure.")
        else:
            print(f"{filename} does NOT match the example file structure.")
