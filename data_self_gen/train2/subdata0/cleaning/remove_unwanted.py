import cv2
import numpy as np
# import skimage.morphology
import glob

# read input
for fil in glob.glob('labels/*.png'):
    name_1 = fil.split('/')[-1]
    print(name_1)
    img = cv2.imread(fil)
    img[img>=1]=255

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # use thresholding
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
    output = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    output[output==255]=200
    cv2.imwrite(name_1, output)
    #cv2.imshow('image', output)
    #cv2.waitKey(0)




# # get distance transform
# distance = thresh.copy()
# distance = cv2.distanceTransform(distance, distanceType=cv2.DIST_L2, maskSize=5).astype(np.float32)
#
# # get skeleton (medial axis)
# binary = thresh.copy()
# binary = binary.astype(np.float32)/255
# skeleton = skimage.morphology.skeletonize(binary).astype(np.float32)
#
# # apply skeleton to select center line of distance
# thickness = cv2.multiply(distance, skeleton)
#
# # get average thickness for non-zero pixels
# #average = np.mean(thickness[skeleton!=0])
#
# # thickness = 2*average
# print(len(thickness))
# thick = min(thickness[skeleton!=0])
# print("thickness:", thick)
