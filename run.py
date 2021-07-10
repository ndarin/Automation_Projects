#!/usr/bin/env python3

import os
import requests

def create_dict(path):
    file_list = os.listdir(path)
    dirs = [path + x for x in file_list]

    dict_list = []
    keys = 'title', 'name', 'date', 'feedback'

    for file in dirs:
        dic = {}
        with open(file) as f:
            count = 0
            for line in f:
                line = line.strip()
                if count == 0:
                    dic[keys[count]] = line
                elif count == 1:
                    dic[keys[count]] = line
                elif count == 2:
                    dic[keys[count]] = line
                else:
                    dic[keys[count]] = line
                count += 1
        dict_list.append(dic)
    return(dict_list)

def api_call(url, dictionary):
    response = requests.post(url, json=dictionary)
    if response.status_code != 201:
        raise Exception("POST failed with status code {}".format(response.status_code))

def main():
    dictionary = create_dict('C:/Users/tawan/data/feedback/')
    api_call(sys.argv[1], dictionary)

if __name__ == "__main__":
    main()
