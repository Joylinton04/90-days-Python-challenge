# Day 21 of py challenge
# Automating Tasks with Python

import os
import shutil

def organize_files(directory_path):
    """
    Organizes files in the specified directory by moving them into subfolders
    named after their file extensions.

    Args:
        directory_path (str): The path to the directory to be organized.
    """
    print(f"Starting file organization in: {directory_path}")

    # Check if the provided path is a valid directory
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return

    # List all items (files and directories) in the specified path
    try:
        items = os.listdir(directory_path)
    except OSError as e:
        print(f"Error accessing directory '{directory_path}': {e}")
        return

    for item in items:
        # Construct the full path to the item
        item_path = os.path.join(directory_path, item)

        # Check if it's a file (and not a directory)
        if os.path.isfile(item_path):
            # Split the filename into base name and extension
            # For files like 'archive.tar.gz', it will correctly get '.gz'
            # For files with no extension, it will be an empty string
            _, extension = os.path.splitext(item)
            extension = extension.lower() # Convert to lowercase for consistency

            # If there's no extension, categorize it as 'no_extension'
            if not extension:
                folder_name = "no_extension"
            else:
                # Remove the leading dot from the extension (e.g., '.txt' becomes 'txt')
                folder_name = extension[1:] + "_files"

            # Construct the path for the destination folder
            destination_folder = os.path.join(directory_path, folder_name)

            # Create the destination folder if it doesn't exist
            try:
                os.makedirs(destination_folder, exist_ok=True)
                print(f"Created folder: {destination_folder}")
            except OSError as e:
                print(f"Error creating directory '{destination_folder}': {e}")
                continue # Skip to the next file if folder creation fails

            # Construct the full path for the destination file
            destination_file_path = os.path.join(destination_folder, item)

            # Move the file
            try:
                shutil.move(item_path, destination_file_path)
                print(f"Moved '{item}' to '{destination_folder}'")
            except shutil.Error as e:
                print(f"Error moving '{item}': {e}")
            except Exception as e:
                print(f"An unexpected error occurred while moving '{item}': {e}")
        else:
            print(f"Skipping directory or special file: '{item}'")

    print("File organization complete!")

if __name__ == "__main__":

    directory_to_organize = "/Users/joylinton/repos/90-days-Python-challenge"

    organize_files(directory_to_organize)
