#!/usr/bin/env python3

from PIL import Image
import os, glob, sys

size = 128, 128
path = sys.argv[1]
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
    # convert image to thumbnail
    im.thumbnail(size)
    # rotate image and save output
    out = im.rotate(-90)
    # add the destination directory path '/opt/icon/' and save image
    out.save(sys.argv[2] + file + "JPEG")
