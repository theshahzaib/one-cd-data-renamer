import os
import shutil


os.makedirs("train\A", exist_ok=True)
os.makedirs("train\B", exist_ok=True)
os.makedirs("train\mask", exist_ok=True)

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

source_dir = os.getcwd()+'/train'
# print(source_dir)  # Get the current working directory
destination_dir = "train/A"  # Replace with your desired destination directory

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

try:
    for filename in os.listdir(source_dir):
        if filename.endswith(".jpg"):
            src_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(destination_dir, filename)
            shutil.copy(src_file, dest_file)

    print("All JPG files copied successfully!")

except shutil.Error as e:
    print(f"Error occurred: {e}")


source_dir = os.getcwd()+'/train'
# print(source_dir)  # Get the current working directory
destination_dir = "train/B"  # Replace with your desired destination directory

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

try:
    for filename in os.listdir(source_dir):
        if filename.endswith(".jpg"):
            src_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(destination_dir, filename)
            shutil.copy(src_file, dest_file)

    print("All JPG files copied successfully!")

except shutil.Error as e:
    print(f"Error occurred: {e}")


source_dir = os.getcwd()+'/train'
# print(source_dir)  # Get the current working directory
destination_dir = "train/mask/A"  # Replace with your desired destination directory

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

try:
    for filename in os.listdir(source_dir):
        if filename.endswith(".png"):
            src_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(destination_dir, filename)
            shutil.copy(src_file, dest_file)

    print("All PNG Masks copied successfully!")

except shutil.Error as e:
    print(f"Error occurred: {e}")


source_dir = os.getcwd()+'/train'
# print(source_dir)  # Get the current working directory
destination_dir = "train/mask/B"  # Replace with your desired destination directory

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

try:
    for filename in os.listdir(source_dir):
        if filename.endswith(".png"):
            src_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(destination_dir, filename)
            shutil.copy(src_file, dest_file)

    print("All PNG Masks copied successfully!")

except shutil.Error as e:
    print(f"Error occurred: {e}")


def delete_last_file(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Check if there are any files in the folder
    if files:
        # Construct the full path of the last file
        last_file_path = os.path.join(folder_path, files[-1])

        # Delete the last file
        os.remove(last_file_path)
        print(f'Deleted last file: {last_file_path}')
    else:
        print('Folder is empty, no files to delete.')

# Example usage
folder_path = 'train\A'
delete_last_file(folder_path)


def delete_first_file(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Check if there are any files in the folder
    if files:
        # Construct the full path of the first file
        first_file_path = os.path.join(folder_path, files[0])

        # Delete the first file
        os.remove(first_file_path)
        print(f'Deleted first file: {first_file_path}')
    else:
        print('Folder is empty, no files to delete.')

# Example usage
folder_path = 'train\B'
delete_first_file(folder_path)


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
folder_a = 'train\A'
folder_b = 'train\B'

replace_file_names(folder_a, folder_b)


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
folder_path = 'train\A'
postfix = '_pre'
add_postfix_to_files(folder_path, postfix)


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
folder_path = 'train\B'
postfix = '_post'
add_postfix_to_files(folder_path, postfix)


def delete_last_file(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Check if there are any files in the folder
    if files:
        # Construct the full path of the last file
        last_file_path = os.path.join(folder_path, files[-1])

        # Delete the last file
        os.remove(last_file_path)
        print(f'Deleted last file: {last_file_path}')
    else:
        print('Folder is empty, no files to delete.')

# Example usage
folder_path = 'train\mask\A'
delete_last_file(folder_path)


def delete_first_file(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Check if there are any files in the folder
    if files:
        # Construct the full path of the first file
        first_file_path = os.path.join(folder_path, files[0])

        # Delete the first file
        os.remove(first_file_path)
        print(f'Deleted first file: {first_file_path}')
    else:
        print('Folder is empty, no files to delete.')

# Example usage
folder_path = 'train\mask\B'
delete_first_file(folder_path)


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
folder_a = 'train\mask\A'
folder_b = 'train\mask\B'

replace_file_names(folder_a, folder_b)


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
folder_path = 'train\mask\A'
old_string = 'mask'
new_string = 'pre'

replace_string_in_filenames(folder_path, old_string, new_string)


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
folder_path = 'train\mask\B'
old_string = 'mask'
new_string = 'post'

replace_string_in_filenames(folder_path, old_string, new_string)


def move_all_files(source_folder, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Move the file to the destination folder
        shutil.move(source_path, destination_path)
        print(f'Moved: {source_path} -> {destination_path}')


# Example usage
source_folder = 'train\mask\A'
destination_folder = 'train\mask'

move_all_files(source_folder, destination_folder)

# Example usage
source_folder = 'train\mask\B'
destination_folder = 'train\mask'

move_all_files(source_folder, destination_folder)



def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f'Deleted folder: {folder_path}')
    except Exception as e:
        print(f'Error deleting folder: {e}')



# Example usage
folder_to_delete = 'train\mask\A'
delete_folder(folder_to_delete)


# Example usage
folder_to_delete = 'train\mask\B'
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
file_extension_to_delete = '.jpg'  # Replace with your desired file extension
delete_files_with_extension(folder_path, file_extension_to_delete)

# Example usage
folder_path = 'train'
file_extension_to_delete = '.png'  # Replace with your desired file extension
delete_files_with_extension(folder_path, file_extension_to_delete)