# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

filepath = os.path.join("Resources", "employees.csv")

new_employee_data = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # YOUR CODE HERE
        f_name = row['first_name']
        l_name = row['last_name']
        email = f'{l_name}.{f_name}@companymail.com'
        datarow = [row['first_name'], row['last_name'], row['ssn'], email]
        new_employee_data.append(datarow)
# Grab the filename from the original path
filename = os.path.split(filepath)

new_header = ["first_name", "last_name", "ssn", "email"]

# Write updated data to csv file
csvpath = os.path.join("", "employees.csv")
with open(csvpath, "w") as csvfile:
    # YOUR CODE HERE
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(new_header)

    csvwriter.writerows(new_employee_data)