#!/usr/bin/env python3

import os
import datetime
import reports
import emails

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
                    dic['name'] = line
                elif count == 1:
                    dic['weight'] = line
                count += 1
        dict_list.append(dic)
    return(dict_list)

def create_paragraph(dict_list):
    paragraph = []
    for dic in dict_list:
        values = list(dic.values())
        paragraph.append("name: {} \nweight: {}<br/>". format(values[0], values[1]))
    return "".join(paragraph)

def main():
    # Run the functions. 'create_dict' takes directory containing text files
    dictionary = create_dict('./supplier-data/descriptions/')
    paragraph = create_paragraph(dictionary)
    date_today = datetime.date.today().strftime("%B %d, %Y")
    title = "Processed Update on {}".format(date_today)
    # Generate the pdf
    reports.generate_report("/tmp/processed.pdf", title, paragraph)

    # Generate and send email
    sender = "automation@example.com"
    receiver = "something@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"

    message = emails.generate(sender, receiver, subject, body, attachment)
    emails.send(message)

if __name__ == "__main__":
    main()
