from PIL import Image
import os

def resize_images(input_folder, output_folder, target_resolution):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all files in the input folder
    input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    for input_file in input_files:
        input_path = os.path.join(input_folder, input_file)
        output_path = os.path.join(output_folder, input_file)

        # Open the image
        img = Image.open(input_path)

        # Calculate the new size based on the target resolution
        new_width = int(img.width * (0.3 / target_resolution))
        new_height = int(img.height * (0.3 / target_resolution))

        # Resize the image
        resized_img = img.resize((new_width, new_height))

        # Save the resized image
        resized_img.save(output_path)

if __name__ == "__main__":
    # Specify input and output folders
    input_folder_path = "0p3"
    output_folder_path = "0p5"

    # Specify the target resolution (0.5 meters per pixel)
    target_resolution = 0.5

    # Resize images and save to the output folder
    resize_images(input_folder_path, output_folder_path, target_resolution)
