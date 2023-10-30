# Import 'argv' from the 'sys' library to read command-line arguments
from sys import argv

# Unpack the command-line arguments into 'script' and 'input_file'
script, input_file = argv

# Define a function 'print_all' that takes a file object 'f' and prints its content
def print_all(f):
    print(f.read())

# Define a function 'rewind' that takes a file object 'f' and sets its read/write position to the start
def rewind(f):
    f.seek(0)

# Define a function 'print_a_line' that takes a line number and a file object, and prints that line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open the file specified by 'input_file' and store it in 'current_file'
current_file = open(input_file)

# Print a message to indicate the whole file will be printed
print("First let's print the whole file:\n")

# Call 'print_all' to print the content of 'current_file'
print_all(current_file)

# Print a message to indicate that the file read/write position will be reset
print("Now let's rewind, kind of like a tape.")

# Call 'rewind' to set the read/write position to the start of 'current_file'
rewind(current_file)

# Print a message to indicate that three lines will be printed
print("Let's print three lines:")

# Set the current line number to 1
current_line = 1
# Print the first line of 'current_file'
print_a_line(current_line, current_file)

# Increment the current line number
current_line = current_line + 1
# Print the second line of 'current_file'
print_a_line(current_line, current_file)

# Increment the current line number again
current_line = current_line + 1
# Print the third line of 'current_file'
print_a_line(current_line, current_file)
