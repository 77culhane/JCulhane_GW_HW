# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

    # Show pie selection prompt
    print("---------------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")

    pie_choice = input("Which would you like? ")
    if pie_choice == "Pecan":
        pie_purchases[0] = pie_purchases[0] + 1
    elif pie_choice == "Apple Crisp":
        pie_purchases[1] = pie_purchases[1] + 1
    elif pie_choice == "Bean":
        pie_purchases[2] = pie_purchases[2] + 1
    elif pie_choice == "Banoffee":
        pie_purchases[3] = pie_purchases[3] + 1
    elif pie_choice == "Black Bun":
        pie_purchases[4] = pie_purchases[4] + 1
    elif pie_choice == "BlueBerry":
        pie_purchases[5] = pie_purchases[5] + 1
    elif pie_choice == "Buko":
        pie_purchases[6] = pie_purchases[6] + 1
    elif pie_choice == "Burek":
        pie_purchases[7] = pie_purchases[7] + 1
    elif pie_choice == "Tamale":
        pie_purchases[8] = pie_purchases[8] + 1
    elif pie_choice == "Steak":
        pie_purchases[9] = pie_purchases[9] + 1
    else:
        print("!invalid entry!")

        
    
    # Get index of the pie from the selected number
    # YOUR CODE HERE
    choice_index = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
    # Add pie to the pie list by finding the matching index and adding one to its value
    # YOUR CODE HERE
    
    print("------------------------------------------------------------------------")

    # Inform the customer of the pie purchase
    print("Great! We'll have that "  + str(pie_choice) + " Pie right out for you.")

    # Provide exit option
    # Prompt the user if they would like to make another purchase
    # YOUR CODE HERE
    shopping = input("Would you like to make another purchase? (y/n): ")
# Once the pie list is complete
print("------------------------------------------------------------------------")

# Count instances of each pie
print("You purchased: ")

# Loop through the full pie list
# YOUR FOR LOOP HERE
for i in range(len(pie_list)):
    print(f"{pie_purchases[i]} {pie_list[i]}")


#piecounter = 0
#for purchase in pie_purchases:
#    # Gather the count of each pie in the pie list and print them alongside the pies
#    # YOUR CODE HERE
#    print(purchase)
#    print(pie_list[piecounter])
#    piecounter = piecounter + 1