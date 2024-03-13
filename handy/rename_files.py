import os
import csv

# Adjust these paths as necessary
mapping_file_path = 'C:\\Users\\jclay\\Desktop\\names_mapping.csv'
directory_path = 'C:\\Users\\jclay\\Desktop\\BESS'
file_extension = '.xlsx'  # Define the common file extension

# Read the mapping from the CSV file, skipping the header row
with open(mapping_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        current_name = row[0] + file_extension  # Append the file extension
        new_name = row[1] + file_extension  # Append the file extension

        # Define the full path for current and new names
        current_file_path = os.path.join(directory_path, current_name)
        new_file_path = os.path.join(directory_path, new_name)

        # Check if the current file exists before trying to rename
        if os.path.exists(current_file_path):
            os.rename(current_file_path, new_file_path)
            print(f"Renamed: {current_name} to {new_name}")
        else:
            print(f"File {current_name} not found. Skipping.")
