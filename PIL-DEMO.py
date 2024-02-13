'''
Python Image Library 
Demonstration
Professor Hosmer
September 2021
'''

# Python Standard Library
import os

# 3rd Party Modules
from PIL import Image

imageFile = input("Image to Process: ")
try:
    with Image.open(imageFile) as im:
        # if success, get the details
        imStatus = 'YES'
        imFormat = im.format
        imType   = im.mode            

        imWidth  = im.width
        imHeight = im.height
        
        print("Image Format: ", im.format)
        print("Image Type:   ", im.mode)
        print("Image Width:  ", im.width)
        print("Image Height: ", im.height)
        
except Exception as err:
    print("Exception: ", str(err))
            
