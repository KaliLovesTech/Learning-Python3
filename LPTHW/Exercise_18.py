# Define a function called 'print_two' that takes any number of arguments (*args)
# This is similar to using argv for command-line arguments.
def print_two(*args):
    # Unpack the arguments into variables 'arg1' and 'arg2'
    arg1, arg2 = args
    # Print the arguments
    print(f"arg1: {arg1}, arg2: {arg2}")

# Define a function 'print_two_again' that takes exactly two arguments
# This is a cleaner way of doing what 'print_two' does without using *args.
def print_two_again(arg1, arg2):
    # Print the arguments
    print(f"arg1: {arg1}, arg2: {arg2}")

# Define a function 'print_one' that takes just one argument
def print_one(arg1):
    # Print the argument
    print(f"arg1: {arg1}")

# Define a function 'print_none' that takes no arguments
def print_none():
    # Print a message indicating no arguments were passed
    print("I got nothin'.")

# Call the function 'print_two' with two string arguments
print_two("Zed", "Shaw")

# Call the function 'print_two_again' with two string arguments
print_two_again("Zed", "Shaw")

# Call the function 'print_one' with one string argument
print_one("First!")

# Call the function 'print_none' with no arguments
print_none()
