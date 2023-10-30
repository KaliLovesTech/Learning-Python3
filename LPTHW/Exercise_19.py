# Define a function called 'cheese_and_crackers' that takes two arguments: cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print the number of cheeses using string formatting
    print(f"You have {cheese_count} cheeses!")
    # Print the number of boxes of crackers using string formatting
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # Print a string indicating this is enough for a party
    print("Man that's enough for a party!")
    # Print a string suggesting to get a blanket, followed by a newline character
    print("Get a blanket.\n")

# Print a message indicating we can call the function with direct numbers
print("We can just give the function numbers directly:")
# Call the function with numbers as arguments
cheese_and_crackers(20, 30)

# Print a message indicating we can call the function using variables
print("OR, we can use variables from our script:")
# Declare variables for amount of cheese and crackers
amount_of_cheese = 10
amount_of_crackers = 50
# Call the function using the variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print a message indicating we can do math inside the function call
print("We can even do math inside too:")
# Call the function using mathematical expressions as arguments
cheese_and_crackers(10 + 20, 5 + 6)

# Print a message indicating we can combine variables and math
print("And we can combine the two, variables and math:")
# Call the function using a combination of variables and mathematical expressions
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
