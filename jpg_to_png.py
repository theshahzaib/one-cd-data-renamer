import concurrent.futures
from PIL import Image
import os

def convert_image(file_name):
    if file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        # Open the JPG image
        image_path = os.path.join(folder_path, file_name)
        img = Image.open(image_path)
        
        # Convert and save as PNG
        new_file_name = os.path.splitext(file_name)[0] + ".png"
        png_path = os.path.join(folder_path, new_file_name)
        img.save(png_path, "PNG")
        
        # Close the image
        img.close()
        
        # Delete the original JPG file
        os.remove(image_path)
        
        return new_file_name

if __name__ == "__main__":
    # Path to the folder containing JPG images
    folder_path = "images"
    
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)
    
    # Number of threads to use
    num_threads = min(8, len(file_list))  # Adjust the number of threads as needed
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Submit conversion tasks to the thread pool
        future_to_file = {executor.submit(convert_image, file_name): file_name for file_name in file_list}
        for future in concurrent.futures.as_completed(future_to_file):
            file_name = future_to_file[future]
            try:
                converted_file = future.result()
            except Exception as e:
                print(f"Conversion of {file_name} failed with error: {e}")

    print("Conversion and deletion completed.")
