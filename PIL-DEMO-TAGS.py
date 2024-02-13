'''
PIL DEMO
JPEG
EXIF TAGS
'''


# import the Python Image Library 
# along with TAGS and GPS related TAGS
# Note you must install the PILLOW Module
# pip install PILLOW

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

fileName = input("Image to Process: ")

try:
    pilImage = Image.open(fileName)
    exifData = pilImage._getexif()

except Exception as err:
    print("Exception: ", str(err))

# Interate through the exifData
# Searching for GPS Tags

imageTimeStamp = "NA"
cameraModel    = "NA"
cameraMake     = "NA"

if exifData:

    for tag, theValue in exifData.items():

        # obtain the tag
        tagValue = TAGS.get(tag, tag)

        # Collect basic image data if available

        if tagValue == 'DateTimeOriginal':
            imageTimeStamp = exifData.get(tag).strip()

        if tagValue == "Make":
            cameraMake = exifData.get(tag).strip()

        if tagValue == 'Model':
            cameraModel = exifData.get(tag).strip()

print("Image Timestamp: ", imageTimeStamp)print("Camera Make:     ", cameraMake)
print("Camera Model:    ", cameraModel)