#!/usr/bin/env python3

from PIL import Image
import os, glob, sys

size = 600, 400
path = "./supplier-data/images/"
# first obtain a list of .tiff images from the images directory
for infile in glob.glob(path + '/*.tiff'):
  # remove 'image/' and '.tiff' from infile variable and save file name
  lane, _ = os.path.splitext(infile)
  _, file = os.path.split(lane)
  # open the image file
  with Image.open(infile) as im:
    # change image mode to 'RGB', necessary to convert to JPEG
    if im.mode != 'RGB':
        im = im.convert('RGB')
    # change image size
    out = im.resize(size)
    # add the destination directory path '/opt/icon/' and save image
    out.save("./supplier-data/images/" + file + ".jpeg", "JPEG")
