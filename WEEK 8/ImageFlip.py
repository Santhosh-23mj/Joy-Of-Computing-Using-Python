#!/usr/bin/python3
"""
This program implements image processing
This program just flips an image
Flipping is called as transpose
"""

from PIL import Image

image = input("Enter path to image file : ")
print("1 - FLIP LEFT RIGHT")
print("2 - FLIP TOP BOTTOM")
ch = int(input("Your choice : "))
img   = Image.open(image)

if ( ch == 1 ):
    transposed_image = img.transpose(Image.FLIP_LEFT_RIGHT)

if ( ch == 2 ):
    transposed_image = img.transpose(Image.FLIP_TOP_BOTTOM)

transposed_image.save('Output.png')
print("DONE")