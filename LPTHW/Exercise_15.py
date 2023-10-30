# Import the 'argv' (Argument Variable) module from the 'sys' (System) library
# This allows us to pass command-line arguments to the script.
from sys import argv

# Unpack the 'argv' variable into two variables: 'script' and 'filename'
# 'script' will contain the name of the script itself, and 'filename' will contain the name of the file to be read.
script, filename = argv

# Open the file whose name is stored in 'filename' and store the file object in the variable 'txt'
txt = open(filename)

# Print a message stating which file will be displayed, then read and display the file's contents
print(f"Here's your file {filename}:")
print(txt.read())

# Ask the user to type the filename again, for demonstration purposes
print("Type the filename again:")
file_again = input("> ")

# Open the file whose name was just inputted and store the file object in the variable 'txt_again'
txt_again = open(file_again)

# Read and display the contents of the file specified by 'file_again'
print(txt_again.read())
