#!/usr/bin/env python3

import os
import requests

def create_dict(path):
    # Get a list of files in the directory and add the directory path
    file_list = os.listdir(path)
    dirs = [path + x for x in file_list]
    # Create an empty list to store the dictionaries
    dict_list = []
    for file in dirs:
        # Open each file, read contents, store in a dictionary
        # Dictionary keys correspond to data labels in the files
        dic = {}
        with open(file) as f:
            count = 0
            for line in f:
                line = line.strip()
                if count == 0:
                    dic['title'] = line
                elif count == 1:
                    dic['name'] = line
                elif count == 2:
                    dic['date'] = line
                else:
                    dic['feedback'] = line
                count += 1
        dict_list.append(dic)
    return(dict_list)

def api_call(url, dictionary):
    # Function takes web service url and list of dictionaries
    # Pass one dictionary at a time to avoid Error 415.
    # Web service expects a dictionary not a list. 
    for dict in dictionary:
      response = requests.post(url, data=dict)
      # Print alert if something goes wrong.
      if response.status_code != 201:
        raise Exception("POST failed with status code {}".format(response.status_code))

def main():
    # Run the functions. 'create_dict' takes directory containing text files
    dictionary = create_dict('/data/feedback/')
    # 'api_call' takes web service url as a command line argument
    api_call(sys.argv[1], dictionary)

if __name__ == "__main__":
    main()
