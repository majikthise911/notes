import os
import csv

# Specify the directory where both your files and the mapping CSV are located
directory_path = 'C:\\Users\\jclay\\Desktop\\BESS'
mapping_file_name = 'names_mapping.csv'  # Name of your mapping file
file_extension = '.xlsx'  # The common file extension for your files

# Combine the directory path with the mapping file name to get the full path
mapping_file_path = os.path.join(directory_path, mapping_file_name)

# Read the mapping from the CSV file, skipping the header row
with open(mapping_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        current_name = row[0] + file_extension  # Append the file extension to the current name
        new_name = row[1] + file_extension  # Append the file extension to the new name

        # Define the full path for current and new names
        current_file_path = os.path.join(directory_path, current_name)
        new_file_path = os.path.join(directory_path, new_name)

        # Check if the current file exists before trying to rename
        if os.path.exists(current_file_path):
            os.rename(current_file_path, new_file_path)
            print(f"Renamed: {current_name} to {new_name}")
        else:
            print(f"File {current_name} not found. Skipping.")
