# -*- coding: UTF-8 -*-
"""PyBoss Homework Solution."""

# Import required packages
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "employee_data.csv")
file_to_output = os.path.join("analysis", "employee_data_reformatted.csv")

# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Placeholders for re-formatted contents
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_ssns = []
emp_dobs = []
emp_states = []

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as emp_data:
    csvreader = csv.reader(emp_data)

    header = next(csvreader)

    # Loop through each row, re-grab each field and store in a new list
    for row in csvreader:

        # Grab emp_ids and store it into a list
        emp_ids = emp_ids + [row[0]]
        # Grab names, split them, and store them in a temporary variable
        namesplitter = row[1]
        namesplitter = namesplitter.split(" ")
        # Then save first and last name in separate lists
        # YOUR CODE HERE
        for first_names in namesplitter:
           first_names = namesplitter[0]
        for last_names in namesplitter:
           last_names = namesplitter[1]
        emp_first_names.append(first_names)
        emp_last_names.append(last_names)
        # Grab DOB and reformat it
        # YOUR CODE HERE
        dob = row[2]
        dobsplitter = dob.split("-")
        YYYY = dobsplitter[0]
        MM = dobsplitter[1]
        DD = dob[2]
        new_dob = f"{MM}/{DD}/{YYYY}"
        # Then store it into a list
        # YOUR CODE HERE
#        emp_dobs = new_dob
        emp_dobs.append(new_dob)

        # Grab SSN and reformat it
        # YOUR CODE HERE
        ssnsplitter = row[3].split("-")
#        ssnsplitter[0:3] = ("-", "-", "-")
        First = ssnsplitter[0]
        Second = ssnsplitter[1]
        Third = ssnsplitter[2]
        for i in First:
             First = "***"
        for i in Second:
             Second = "**"
        # Then store it into a list
        # YOUR CODE HERE
        new_ssns = f"{First}-{Second}-{Third}"
        emp_ssns.append(new_ssns)
#        joined_ssn = " ".join(ssnsplitter)
#        emp_ssns.append(joined_ssn)

        
        # Grab the states and use the dictionary to find the replacement
        # YOUR CODE HERE
        states = row[4]
        # Then store the abbreviation into a list
        # YOUR CODE HERE
        abbreviated = us_state_abbrev[states]        
        emp_states.append(abbreviated)

# Zip all of the new lists together
# YOUR CODE HERE
zipped_lists = zip(emp_ids, emp_first_names, emp_last_names, emp_dobs, emp_ssns, emp_states)
new_header = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
# Write all of the election data to csv
# YOUR CODE HERE
file_to_output = os.path.join("analysis", "employee_data_reformatted.csv")

with open(file_to_output, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(new_header)

    csvwriter.writerows(zipped_lists)

