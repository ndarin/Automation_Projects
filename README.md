# Automating Real World Tasks with Python

This repo contains scripts for 4 Automation projects.  Part of the
Google IT Automation with Python Professional Certificate final assessment.

There are 3 mini-projects and a main project.

Project 1 - Image Processing

image_processing.py - This script will open, rotate, resize and convert image files to jpeg and save the files to a different directory.

Project 2 - API call

reviews.py - The script processes customer reviews stored in text files,
and makes API calls to a Django-based web service that displays the reviews on a website.

Project 3 - PDF Generation

cars.py - This script accepts and processes a json file on car sales,
summarises maximum values, generates a pdf report and emails it. Its
module dependencies are: reports.py and emails.py

car_sales.json - Contains data on car sales.

Project 4 - Automating Uploading Catalog Info
This project combines all automation tasks from projects 1-3 in a single task.

changeImage.py - This script will open, resize and convert image files to jpeg and save the files to a different directory.

supplier_image_upload.py - It uploads the jpeg images to a Django-based web Catalog.

run2.py - The script opens catalog descriptions stored in text files, converts text to json and uploads the descriptions to the web catalog.

report_email.py - This script opens up the catalog description text files, extracts product name and weight info, generates a pdf report and emails it to the store owner. Its module dependencies are: reports.py and emails.py.

health_check.py - The script checks the health of the computer and generates an email alert notifying the user of an issue that needs to be addressed. The script is meant to be executed every 60 seconds via a cron job.

Other files
auto_mailer.py - A template script for creating and sending emails.
