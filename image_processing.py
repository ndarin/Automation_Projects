#!/usr/bin/env python3

from PIL import Image
import os, glob

size = 128, 128

for infile in glob.glob("*.tiff"):
  file, ext = os.path.splitext(infile)
  with Image.open(infile) as im:
    im.thumbnail(size)
    out = im.rotate(90)
    out.save(file + ".jpg", "JPEG")
