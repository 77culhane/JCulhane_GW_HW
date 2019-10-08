# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0
start_total = 867884

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    # YOUR CODE HERE

    for row in reader:
        total_months = total_months + 1
        # Track the total
        # YOUR CODE HERE
        if int(row[1]) > 0:
            total_net = total_net + int(row[1])
        # Track the net change
        # YOUR CODE HERE
        net_change = int(row[1])- int(start_total)
        net_change_list.append(net_change)
        start_total = row[1]
        # Calculate the greatest increase
        # YOUR CODE HERE
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        # Calculate the greatest decrease
        # YOUR CODE HERE
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
# Calculate the Average Net Change
# YOUR CODE HERE
net_monthly_avg = sum(net_change_list) / len(net_change_list)
# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
# YOUR CODE HERE
print(output)
# Export the results to text file
# YOUR CODE HERE
text_file = open("Financial_Analysis.txt", "w")
text_file.write(output)
text_file.close()