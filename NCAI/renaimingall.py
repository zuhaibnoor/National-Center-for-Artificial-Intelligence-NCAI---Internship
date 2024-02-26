import os

folder = 'C:\\Users\\ABD\\Downloads\\frames'

# Get a list of all files in the folder
files = os.listdir(folder)

# Iterate over the files and rename each one
for i, filename in enumerate(files):
    # Construct the new filename
    dest = os.path.join(folder, f"{i}.jpg")
    # Get the full path of the original file
    original_path = os.path.join(folder, filename)
    # Rename the file
    os.rename(original_path, dest)
    print(f"Renamed {filename} to {dest}")
