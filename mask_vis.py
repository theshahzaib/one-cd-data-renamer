import os
import numpy as np
from PIL import Image

# Define your color map
color_map = {
    0: [0, 0, 0],     # Class 0 - Background (Black)
    1: [0, 255, 0],   # Class 1 - flatSurface (Green)
    2: [255, 0, 0],   # Class 2 - excavation (Red)
    3: [255, 0, 255], # Class 3 - building (Purple)
    4: [255, 255, 0]  # Class 4 - foundation (Yellow)
}

'''
basic_colors = {
    'red': [255, 0, 0],
    'green': [0, 255, 0],
    'blue': [0, 0, 255],
    'yellow': [255, 255, 0],
    'cyan': [0, 255, 255],
    'magenta': [255, 0, 255],
    'black': [0, 0, 0]
}
'''

# Input and output directories
input_folder = 'labels'
output_folder = 'output_colored_masks'

# Create output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all PNG files in the input folder
mask_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

# Process each mask file
for mask_file in mask_files:
    # Load the PNG mask
    mask_path = os.path.join(input_folder, mask_file)
    mask = Image.open(mask_path)
    
    # Convert the mask to numpy array
    mask_array = np.array(mask)

    # Create a blank RGB image with the same shape as the mask
    colored_mask = np.zeros((mask_array.shape[0], mask_array.shape[1], 3), dtype=np.uint8)

    # Color code the mask based on the color map
    for class_index, color in color_map.items():
        # Find pixels in the mask belonging to the current class
        class_pixels = (mask_array == class_index)
        
        # Assign color to the pixels belonging to the current class
        colored_mask[class_pixels] = color

    # Convert the numpy array to an image
    colored_mask_image = Image.fromarray(colored_mask)

    # Save the color coded mask in the output folder with the same filename
    output_mask_path = os.path.join(output_folder, mask_file)
    colored_mask_image.save(output_mask_path)

print("Color coding of masks completed.")
