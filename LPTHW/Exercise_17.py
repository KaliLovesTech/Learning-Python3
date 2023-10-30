# Import the 'argv' (Argument Variable) module from the 'sys' (System) library
# and 'exists' from 'os.path' to check if a file exists.
from sys import argv
from os.path import exists

# Hardcoding the names of the source and destination files
from_file = "test.txt"
to_file = "new_test.txt"

# Print a message to indicate which file is being copied to which
print(f"Copying from {from_file} to {to_file}")

# Open the source file and read its content into a variable called 'indata'
# Note: This could be done in one line, but it's split for clarity.
in_file = open(from_file)
indata = in_file.read()

# Print the size of the source file in bytes
print(f"The input file is {len(indata)} bytes long")

# Check if the destination file already exists and print the result
print(f"Does the output file exist? {exists(to_file)}")

# Wait for user confirmation to proceed
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# Open the destination file in write mode ('w') and write the content from 'indata'
out_file = open(to_file, 'w')
out_file.write(indata)

# Print a completion message
print("Alright, all done.")

# Close both the destination and source files to free up resources
out_file.close()
in_file.close()
