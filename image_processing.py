#!/usr/bin/env python3

from PIL import Image
import os, glob

size = 128, 128

for infile in glob.glob("*.tiff"):
  file, ext = os.path.splitext(infile)
  with Image.open(infile) as im:
    out = im.rotate(90)
    out = out.thumbnail(size)
    out.save(file, "JPEG")
