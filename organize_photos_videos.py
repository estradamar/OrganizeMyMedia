import os
import shutil
from datetime import datetime
from pathlib import Path

def get_file_attributes(file_path):
    # Get the creation date and file size
    stat = os.stat(file_path)
    creation_time = datetime.fromtimestamp(stat.st_ctime)
    file_size = stat.st_size
    return creation_time, file_size

def organize_files(source_folder, destination_folder):
    duplicates = []  # List to store duplicate files
    for root, _, files in os.walk(source_folder):
        for file in files:
            # Filter only photo and video files
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov')):
                file_path = os.path.join(root, file)
                creation_time, file_size = get_file_attributes(file_path)
                year_month = creation_time.strftime('%Y_%m')
                dest_subfolder = os.path.join(destination_folder, year_month)
                Path(dest_subfolder).mkdir(parents=True, exist_ok=True)  # Create subfolder if it doesn't exist
                
                dest_file_path = os.path.join(dest_subfolder, file)
                if not os.path.exists(dest_file_path):
                    # Copy the file if it doesn't exist in the destination folder
                    shutil.copy2(file_path, dest_file_path)
                else:
                    # Check if the file is a duplicate
                    dest_creation_time, dest_file_size = get_file_attributes(dest_file_path)
                    if (creation_time, file_size) == (dest_creation_time, dest_file_size):
                        duplicates.append(file_path)  # Add the duplicate file to the list
    
    # Write the list of duplicate files to a text file
    with open(os.path.join(destination_folder, 'duplicates.txt'), 'w') as f:
        for duplicate in duplicates:
            f.write(f"{duplicate}\n")

if __name__ == "__main__":
    # Prompt the user for the source and destination folder paths
    source_folder = input("Enter the source folder path: ")
    destination_folder = input("Enter the destination folder path: ")
    organize_files(source_folder, destination_folder)
