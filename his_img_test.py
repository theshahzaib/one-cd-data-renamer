import cv2
import numpy as np

def histogram_equalization_multiple_references(source_image, reference_images):
    equalized_channels = []

    # Calculate combined histogram from all reference images
    reference_hist = np.zeros((256,), dtype=float)
    for ref_image in reference_images:
        for channel in cv2.split(ref_image):
            channel_hist, _ = np.histogram(channel.flatten(), bins=256, range=[0, 256], density=True)
            reference_hist += channel_hist

    # Calculate cumulative distribution function (CDF) from the combined histogram
    reference_cdf = reference_hist.cumsum()

    for channel in cv2.split(source_image):
        # Calculate histogram for the source channel
        source_hist, _ = np.histogram(channel.flatten(), bins=256, range=[0, 256], density=True)

        # Calculate cumulative distribution function (CDF) for the source channel
        source_cdf = source_hist.cumsum()

        # Create mapping function using the combined reference CDF
        mapping_function = np.interp(source_cdf, reference_cdf, range(256))

        # Apply mapping function to equalize the channel
        equalized_channel = np.interp(channel.flatten(), range(256), mapping_function).reshape(channel.shape)
        equalized_channels.append(equalized_channel.astype(np.uint8))

    # Merge the equalized channels to get the final equalized image
    equalized_image = cv2.merge(equalized_channels)

    return equalized_image

# Read the source and multiple reference images
source_image = cv2.imread('4.jpg')
reference_image1 = cv2.imread('2.jpg')
reference_image2 = cv2.imread('3.jpg')

# Perform histogram equalization using multiple reference images
equalized_image = histogram_equalization_multiple_references(source_image, [reference_image1, reference_image2])

# Display the images
cv2.imshow('Source Image', source_image)
cv2.imshow('Reference Image 1', reference_image1)
cv2.imshow('Reference Image 2', reference_image2)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
