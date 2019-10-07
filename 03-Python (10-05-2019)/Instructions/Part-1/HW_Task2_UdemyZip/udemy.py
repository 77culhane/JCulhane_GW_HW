import os
import csv

csvpath = os.path.join("web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title
        # YOUR CODE HERE
        title.append(row[1])
        # Add price
        # YOUR CODE HERE
        price.append(row[4])
        # Add number of subscribers
        # YOUR CODE HERE
        subscribers.append(row[5])
        # Add amount of reviews
        # YOUR CODE HERE
        reviews.append(row[6])
        # Determine percent of review left to 2 decimal places
        # YOUR CODE HERE
        percent = round(int(row[6]) / int(row[5]), 2)
        review_percent.append(percent)
        # Get length of the course to just a number
        # YOUR CODE HERE
        splitlength = row[9].split(" ")
        length.append(float(splitlength[0]))
# Zip lists together
# YOUR CODE HERE
zipped = zip(title, price, subscribers, reviews, review_percent, length)

#Set variable for output file
output_file = os.path.join("web_final.csv")

 # Open the output file
with open(output_file, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter =',')

    # Write the header row
    csvwriter.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    # YOUR CODE HERE
    csvwriter.writerows(zipped)