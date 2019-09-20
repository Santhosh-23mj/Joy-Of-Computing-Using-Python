#!/usr/bin/python3
"""
This program implements a Image Enchancing technique - CLAHE
CLAHE - Contrast Limited Adaptive Histogram Equalization
There are more to explore
These things are made simpler by the pre-built libraries
in python 
"""

import cv2

imagefile = input("Enter the path to the image file : ")

# opening the file
img = cv2.imread(imagefile)

# object initialization
clahe = cv2.createCLAHE()

# converting image to grrayscale
gray_img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )

# Applying CLAHE
enhanced = clahe.apply(gray_img)

# printing output
cv2.imwrite('output.png',enhanced)

print("Done")