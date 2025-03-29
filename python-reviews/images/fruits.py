# import libraries
from PIL import Image

# open image
img = Image.open("fruits/apple.jpg")

# basic image information
print(img.format)  # JPEG
print(img.size)    # (640, 480)
print(img.mode)    # RGB
print(img.info['dpi'])    # {'dpi': (72, 72), 'jfif': 1, 'jfif_version': (1, 1), 'jfif_density': (72, 72), 'jfif_unit': 1, 'exif': b'Exif\x00\x00II*\x00\x08

# show image
img.show()