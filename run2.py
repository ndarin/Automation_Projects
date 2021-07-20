#!/usr/bin/env python3

import os
import requests
import json

def create_dict(path):
    # Get a list of files in the directory and add the directory path
    file_list = os.listdir(path)
    dirs = [path + x for x in file_list]
    # Create an empty list to store the dictionaries
    dict_list = []
    for file in dirs:
        # Open each file, read contents, store in a dictionary
        # Dictionary keys correspond to data labels in the files
        filename, _ = os.path.splitext(file)
        img_name = os.path.basename(filename)
        dic = {}
        with open(file) as f:
            count = 0
            for line in f:
                line = line.strip()
                if count == 0:
                    dic['name'] = line
                elif count == 1:
                    dic['weight'] = int(line.replace("lbs", ""))
                else:
                    dic['description'] = line
                dic["image_name"] = img_name + ".jpeg"
                count += 1
        dict_list.append(dic)
    return(dict_list)

def api_call(url, dictionary):
    # Function takes web service url and list of dictionaries
    # Pass one dictionary at a time to avoid Error 415.
    # Web service expects a dictionary not a list.
    headers={'Content-Type':'application/json', 'Vary':"Accept"}
    for dict in dictionary:
        data = json.dumps(dict)
        print(data)
        response = requests.post(url, data=data, headers=headers)
        # Print alert if something goes wrong.
        #if response.status_code != 201:
        #    raise Exception("POST failed with status code {}".format(response.status_code))

def main():
    # Run the functions. 'create_dict' takes directory containing text files
    dictionary = create_dict('./supplier-data/descriptions/')
    # 'api_call' takes web service url as a command line argument
    api_call("http://34.136.150.150/fruits/", dictionary)

if __name__ == "__main__":
    main()
