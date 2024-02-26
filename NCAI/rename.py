import os

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        # Check if the file is a regular file
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Split the filename and extension
            name, ext = os.path.splitext(filename)
            # Construct the new filename with "hello" appended
            new_name = name + "some_random_text" + ext
            # Rename the file
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
            print(f"Renamed {filename} to {new_name}")

# Specify the folder path here
folder_path = "C:\\Users\\ABD\\Downloads\\frames2"

# Call the function to rename files in the specified folder
rename_files(folder_path)
