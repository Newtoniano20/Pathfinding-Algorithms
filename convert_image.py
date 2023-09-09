import sys

from PIL import Image

if len(sys.argv) != 2:
    sys.exit("Usage: python convert_image.py filename")

im = Image.open(sys.argv[1])

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

with open("map.txt", 'w') as f:
    for row in pixels:
        for column in row:
            f.write(" " if column == 1 else "#")
        f.write("\n")