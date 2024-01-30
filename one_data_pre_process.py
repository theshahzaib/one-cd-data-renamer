# -*- coding: utf-8 -*-
"""one_data_pre_process.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bo4oaBz1Vdj-vTRFHt6Sx4yL5fggIlbB
"""



"""# Pre-Processing Data

## Make all 'Pre' Masks will all non-zero pixel to 1
"""

import os
import shutil


os.makedirs("train/pre", exist_ok=True)
os.makedirs("train/post", exist_ok=True)
os.makedirs("train/mask", exist_ok=True)
os.makedirs("train/images", exist_ok=True)
os.makedirs("train/labels", exist_ok=True)


print('ok')

"""## Replace Dosts in file names"""

def replace_dots_in_file_name(folder_path):
    for filename in os.listdir(folder_path):
        # Get the full file path
        filepath = os.path.join(folder_path, filename)

        # Check if it is a file (not a directory)
        if os.path.isfile(filepath):
            # Split the file name and extension
            root, ext = os.path.splitext(filename)

            # Replace dots in the root part of the file name
            new_root = root.replace('.', '_')

            # Combine the new root and the original extension
            new_filename = new_root + ext

            # Construct the new file path
            new_filepath = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(filepath, new_filepath)

# Example usage
folder_path = 'train'
replace_dots_in_file_name(folder_path)

import os

def replace_string_in_filenames(folder_path, old_string, new_string):
    for filename in os.listdir(folder_path):
        # Get the full file path
        filepath = os.path.join(folder_path, filename)

        # Check if it is a file (not a directory)
        if os.path.isfile(filepath):
            # Replace the specified string in the file name
            new_filename = filename.replace(old_string, new_string)

            # Construct the new file path
            new_filepath = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(filepath, new_filepath)
            print(f'Renamed: {filepath} -> {new_filepath}')

# Example usage
folder_path = 'train'
old_string = '_jpg'
new_string = ''

replace_string_in_filenames(folder_path, old_string, new_string)

"""## move first file to the pre folder"""

import os
import shutil

def move_first_jpg(source_folder, destination_folder):
    # Get the list of files in the source folder
    files = [f for f in os.listdir(source_folder) if f.lower().endswith('.jpg')]

    if not files:
        print("No '.jpg' files found in the source folder.")
        return

    # Get the first '.jpg' file in the list
    first_jpg_file = files[0]

    # Build the full paths for source and destination
    source_path = os.path.join(source_folder, first_jpg_file)
    destination_path = os.path.join(destination_folder, first_jpg_file)

    # Move the file to the destination folder
    shutil.move(source_path, destination_path)

    print(f"Moved {first_jpg_file} from {source_folder} to {destination_folder}.")

# Example usage
source_folder = 'train'
destination_folder = 'train/pre'

move_first_jpg(source_folder, destination_folder)

"""## move all remaining '.jpg' files in the post folder"""

import os
import shutil

def move_all_jpg(source_folder, destination_folder):
    # Ensure the destination folder exists, create it if necessary
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get the list of all files in the source folder
    files = os.listdir(source_folder)

    # Filter files to keep only the '.jpg' files
    jpg_files = [f for f in files if f.lower().endswith('.jpg')]

    if not jpg_files:
        print("No '.jpg' files found in the source folder.")
        return

    # Move each '.jpg' file to the destination folder
    for jpg_file in jpg_files:
        source_path = os.path.join(source_folder, jpg_file)
        destination_path = os.path.join(destination_folder, jpg_file)
        shutil.move(source_path, destination_path)
        print(f"Moved {jpg_file} from {source_folder} to {destination_folder}.")

# Example usage
source_folder = 'train'
destination_folder = 'train/post'

move_all_jpg(source_folder, destination_folder)



def add_postfix_to_files(folder_path, postfix):
    for filename in os.listdir(folder_path):
        # Get the full file path
        filepath = os.path.join(folder_path, filename)

        # Check if it is a file (not a directory)
        if os.path.isfile(filepath):
            # Split the file name and extension
            root, ext = os.path.splitext(filename)

            # Add the postfix to the root part of the file name
            new_root = root + postfix

            # Combine the new root and the original extension
            new_filename = new_root + ext

            # Construct the new file path
            new_filepath = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(filepath, new_filepath)

# Example usage
folder_path = 'train/post'
postfix = '_post'
add_postfix_to_files(folder_path, postfix)

"""## Generate Pre-Image Duplicate copies"""

folder_path = 'train/post'
files = os.listdir(folder_path)
num_files = len(files)
folder_path_pre = 'train/pre'
file_pre = os.listdir(folder_path_pre)

import shutil

def duplicate_file(file_path, count):
    try:
        # Validate that the file exists
        if not os.path.isfile(file_path):
            print(f"The file '{file_path}' does not exist.")
            return

        # Get the file's extension and basename
        file_name, file_extension = os.path.splitext(os.path.basename(file_path))

        # Create duplicate copies
        for i in range(1, count + 1):
            duplicate_file_name = f"{file_name}_copy_{i}{file_extension}"
            duplicate_file_path = os.path.join(os.path.dirname(file_path), duplicate_file_name)
            shutil.copy2(file_path, duplicate_file_path)
            print(f"Duplicate copy {i} created: {duplicate_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_to_duplicate = 'train/pre/'+file_pre[0]
duplicate_count = num_files-1

duplicate_file(file_to_duplicate, duplicate_count)



"""## Replacing B names with A"""

import os

def replace_file_names(folder_a, folder_b):
    # Get lists of files in both folders
    files_a = os.listdir(folder_a)
    files_b = os.listdir(folder_b)

    # Check if the number of files in both folders is the same
    if len(files_a) != len(files_b):
        print("Error: The number of files in the two folders is not the same.")
        return

    # Rename files in folder B to match files in folder A
    for file_a, file_b in zip(files_a, files_b):
        path_a = os.path.join(folder_a, file_a)
        path_b = os.path.join(folder_b, file_b)

        # Replace file name in folder B
        os.rename(path_b, os.path.join(folder_b, file_a))

        print(f'Replaced: {path_b} -> {os.path.join(folder_b, file_a)}')

# Example usage
folder_a = 'train/post'
folder_b = 'train/pre'

replace_file_names(folder_a, folder_b)

"""## Replace 'Post' String with 'Pre' in Pre folder"""

import os

def replace_string_in_filenames(folder_path, old_string, new_string):
    for filename in os.listdir(folder_path):
        # Get the full file path
        filepath = os.path.join(folder_path, filename)

        # Check if it is a file (not a directory)
        if os.path.isfile(filepath):
            # Replace the specified string in the file name
            new_filename = filename.replace(old_string, new_string)

            # Construct the new file path
            new_filepath = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(filepath, new_filepath)
            print(f'Renamed: {filepath} -> {new_filepath}')

# Example usage
folder_path = 'train/pre'
old_string = 'post'
new_string = 'pre'

replace_string_in_filenames(folder_path, old_string, new_string)

"""## Remove first 'png' file from folder"""

import os

def remove_first_png_file(folder_path):
    try:
        # List all files in the folder
        files = os.listdir(folder_path)

        # Filter files to keep only the '.png' files
        png_files = [f for f in files if f.lower().endswith('.png')]

        if not png_files:
            print("No '.png' files found in the folder.")
            return

        # Get the first '.png' file in the list
        first_png_file = png_files[0]

        # Build the full path for the file to be removed
        file_to_remove_path = os.path.join(folder_path, first_png_file)

        # Remove the file
        os.remove(file_to_remove_path)

        print(f"Removed the first '.png' file '{first_png_file}' from the folder.")

    except FileNotFoundError:
        print(f"The folder '{folder_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
folder_path = 'train'
remove_first_png_file(folder_path)



import os
import shutil

def copy_all_png_files(source_folder, destination_folder):
    try:
        # Ensure the destination folder exists, create it if necessary
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # List all files in the source folder
        files = os.listdir(source_folder)

        # Filter files to keep only the '.png' files
        png_files = [f for f in files if f.lower().endswith('.png')]

        if not png_files:
            print("No '.png' files found in the source folder.")
            return

        # Copy each '.png' file to the destination folder
        for png_file in png_files:
            source_path = os.path.join(source_folder, png_file)
            destination_path = os.path.join(destination_folder, png_file)
            shutil.copy2(source_path, destination_path)
            print(f"Copied '{png_file}' from {source_folder} to {destination_folder}.")

    except FileNotFoundError:
        print(f"The source folder '{source_folder}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_folder = 'train'
destination_folder = 'train/post'

copy_all_png_files(source_folder, destination_folder)



import os

def replace_string_in_filenames(folder_path, old_string, new_string):
    for filename in os.listdir(folder_path):
        # Get the full file path
        filepath = os.path.join(folder_path, filename)

        # Check if it is a file (not a directory)
        if os.path.isfile(filepath):
            # Replace the specified string in the file name
            new_filename = filename.replace(old_string, new_string)

            # Construct the new file path
            new_filepath = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(filepath, new_filepath)
            print(f'Renamed: {filepath} -> {new_filepath}')

# Example usage
folder_path = 'train/post'
old_string = 'mask'
new_string = 'post'

replace_string_in_filenames(folder_path, old_string, new_string)

"""# PNG Mask Update Replace all non-zero px to 1"""

from PIL import Image
import os

def replace_non_zero_pixels_in_folder(input_folder, output_folder):
    try:
        # Ensure the output folder exists, create it if necessary
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # List all files in the input folder
        files = os.listdir(input_folder)

        # Filter files to keep only the '.png' files
        png_files = [f for f in files if f.lower().endswith('.png')]

        if not png_files:
            print("No '.png' files found in the input folder.")
            return

        # Iterate over each '.png' file in the folder
        for png_file in png_files:
            input_path = os.path.join(input_folder, png_file)
            output_path = os.path.join(output_folder, png_file)

            # Open the image
            image = Image.open(input_path)

            # Convert the image to grayscale
            image = image.convert('L')

            # Create a new image with all pixels set to 1 except for 0
            new_image = image.point(lambda p: 1 if p != 0 else 0)

            # Save the new image
            new_image.save(output_path)

            print(f"Non-zero pixels in '{input_path}' replaced with 1. Result saved to '{output_path}'.")

    except FileNotFoundError:
        print(f"The input folder '{input_folder}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_folder = 'train'
output_folder = 'train/mask'

replace_non_zero_pixels_in_folder(input_folder, output_folder)

import os

def replace_string_in_filenames(folder_path, old_string, new_string):
    for filename in os.listdir(folder_path):
        # Get the full file path
        filepath = os.path.join(folder_path, filename)

        # Check if it is a file (not a directory)
        if os.path.isfile(filepath):
            # Replace the specified string in the file name
            new_filename = filename.replace(old_string, new_string)

            # Construct the new file path
            new_filepath = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(filepath, new_filepath)
            print(f'Renamed: {filepath} -> {new_filepath}')

# Example usage
folder_path = 'train/mask'
old_string = 'mask'
new_string = 'pre'

replace_string_in_filenames(folder_path, old_string, new_string)

"""## Move all masks to the 'Pre' folder"""

import os
import shutil

def move_all_files(source_folder, destination_folder):
    try:
        # Ensure the destination folder exists, create it if necessary
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # List all files in the source folder
        files = os.listdir(source_folder)

        if not files:
            print("No files found in the source folder.")
            return

        # Move each file to the destination folder
        for file in files:
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)
            print(f"Moved '{file}' from {source_folder} to {destination_folder}.")

    except FileNotFoundError:
        print(f"The source folder '{source_folder}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_folder = 'train/mask'
destination_folder = 'train/pre'

move_all_files(source_folder, destination_folder)



"""## Deleting unused data"""

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f'Deleted folder: {folder_path}')
    except Exception as e:
        print(f'Error deleting folder: {e}')

# Example usage
folder_to_delete = 'train/mask'
delete_folder(folder_to_delete)

def delete_files_with_extension(folder_path, extension):
    try:
        # Iterate through all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Check if it is a file and has the specified extension
            if os.path.isfile(file_path) and filename.endswith(extension):
                os.remove(file_path)
                print(f'Deleted: {file_path}')

        print(f'Deleted all files with extension "{extension}" in {folder_path}')
    except Exception as e:
        print(f'Error deleting files: {e}')

# Example usage
folder_path = 'train'
file_extension_to_delete = '.png'  # Replace with your desired file extension
delete_files_with_extension(folder_path, file_extension_to_delete)



"""# Finalizing and Moving Data"""

import os
import shutil

def move_all_png_files(source_folder, destination_folder):
    try:
        # Ensure the destination folder exists, create it if necessary
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # List all files in the source folder
        files = os.listdir(source_folder)

        # Filter files to keep only the '.png' files
        png_files = [f for f in files if f.lower().endswith('.jpg')]

        if not png_files:
            print("No '.png' files found in the source folder.")
            return

        # Move each '.png' file to the destination folder
        for png_file in png_files:
            source_path = os.path.join(source_folder, png_file)
            destination_path = os.path.join(destination_folder, png_file)
            shutil.move(source_path, destination_path)
            print(f"Moved '{png_file}' from {source_folder} to {destination_folder}.")

    except FileNotFoundError:
        print(f"The source folder '{source_folder}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_folder = 'train/pre'
destination_folder = 'train/images'

move_all_png_files(source_folder, destination_folder)

# Example usage
source_folder = 'train/post'
destination_folder = 'train/images'

move_all_png_files(source_folder, destination_folder)

import os
import shutil

def move_all_png_files(source_folder, destination_folder):
    try:
        # Ensure the destination folder exists, create it if necessary
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # List all files in the source folder
        files = os.listdir(source_folder)

        # Filter files to keep only the '.png' files
        png_files = [f for f in files if f.lower().endswith('.png')]

        if not png_files:
            print("No '.png' files found in the source folder.")
            return

        # Move each '.png' file to the destination folder
        for png_file in png_files:
            source_path = os.path.join(source_folder, png_file)
            destination_path = os.path.join(destination_folder, png_file)
            shutil.move(source_path, destination_path)
            print(f"Moved '{png_file}' from {source_folder} to {destination_folder}.")

    except FileNotFoundError:
        print(f"The source folder '{source_folder}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_folder = 'train/pre'
destination_folder = 'train/labels'

move_all_png_files(source_folder, destination_folder)

# Example usage
source_folder = 'train/post'
destination_folder = 'train/labels'

move_all_png_files(source_folder, destination_folder)



# Example usage
folder_to_delete = 'train/pre'
delete_folder(folder_to_delete)

# Example usage
folder_to_delete = 'train/post'
delete_folder(folder_to_delete)

print('------------ All Done Thank You!!! ------------')

