import os

directory = "/Users/jclay/Desktop/sow"  # Replace with the path to the directory containing the files to be renamed

files = os.listdir(directory)
n = len(files)

for index, filename in enumerate(files, start=1):
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, f"{index}.txt")  # Replace 'ext' with the desired file extension
    os.rename(old_path, new_path)

print(f"{n} files renamed.")
