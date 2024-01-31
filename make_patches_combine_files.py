from PIL import Image
import os
import shutil

def create_folder(folder_path):
    # Check if the folder already exists
    if os.path.exists(folder_path):
        # If it exists, delete the folder and its contents
        shutil.rmtree(folder_path)
        print(f"Existing folder '{folder_path}' deleted.")

    # Create the new folder
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' created.")



def move_png_files_with_keyword(source_folder, destination_folder, keyword):
    # Ensure the destination folder exists, create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith('.png') and keyword in filename:
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Copy the file to the destination folder
            shutil.move(source_path, destination_path)
            print(f"File '{filename}' copied to {destination_folder}")



def extract_patches(input_folder, output_folder, patch_size):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all files in the input folder
    input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    for input_file in input_files:
        input_path = os.path.join(input_folder, input_file)

        # Open the TIFF image
        img = Image.open(input_path)

        # Get the dimensions of the image
        img_width, img_height = img.size

        # Define the size of the patches
        patch_width, patch_height = patch_size

        # Calculate the number of patches in both dimensions
        num_patches_x = img_width // patch_width
        num_patches_y = img_height // patch_height

        # Extract patches and save them
        for i in range(num_patches_x):
            for j in range(num_patches_y):
                left = i * patch_width
                upper = j * patch_height
                right = left + patch_width
                lower = upper + patch_height

                # Crop the patch
                patch = img.crop((left, upper, right, lower))

                # Save the patch
                output_path = os.path.join(output_folder, f"{os.path.splitext(input_file)[0]}_patch_{i}_{j}.png")
                
                patch.save(output_path)

create_folder("patches")

# Specify input and output folders
input_folder_path = "0p5"
output_folder_path = "patches"

# Specify the patch size (1024x1024)
patch_size = (1024, 1024)

# Extract patches and save to the output folder
extract_patches(input_folder_path, output_folder_path, patch_size)

ipsample_file = input_folder_path+'/'+os.listdir(input_folder_path)[0]
# Open the TIFF image
img = Image.open(ipsample_file)
# Get the dimensions of the image
img_width, img_height = img.size

x_dim = img_width//1024
y_dim = img_height//1024

source_folder_path = "patches"
destination_folder_path = "final"

for i in range(x_dim):
    for j in range(y_dim):
        # print(str(i)+'_'+str(j))
        # Example usage:
        folder_path = "final/patch_"+str(i)+'_'+str(j)
        create_folder(folder_path)

        # Example usage:
        destination_subfolder_path = destination_folder_path+"/patch_"+str(i)+'_'+str(j)
        search_keyword = str(i)+'_'+str(j)

        move_png_files_with_keyword(source_folder_path, destination_subfolder_path, search_keyword)
        


