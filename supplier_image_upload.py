#!/usr/bin/env python3

import os
import glob
import requests

path = "./supplier-data/images/"
url = "http://localhost/upload/"

for infile in glob.glob(path + '/*.jpeg'):
    with open(infile, 'rb') as opened:
        response = requests.post(url, files={'file': opened})
        if response.status_code != 201:
            raise Exception("POST failed with status code {}".format(response.status_code))
