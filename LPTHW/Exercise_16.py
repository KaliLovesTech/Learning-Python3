# Step 1: Set the name of the file we're going to work with
filename = "Exercise_15_Sample.txt"

# Step 2: Print a message saying we're going to erase the file
print(f"We're going to erase {filename}.")
# Inform the user how to cancel the operation
print("If you don't want that, hit CTRL-C *(*^C*)*.")
# Inform the user how to proceed
print("If you do want that, hit RETURN.")

# Step 3: Wait for the user to make a choice
input("?")

# Step 4: Open the file in 'write' mode, which will erase the file
print("Opening the file...")
target = open(filename, 'w')

# Step 5: Truncate (clear) the file - not strictly needed when opened in 'w' mode
print("Truncating the file. Goodbye!")
target.truncate()

# Step 6: Ask the user for three lines of text
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Step 7: Inform the user that we're going to write these lines to the file
print("I'm going to write these to the file.")

# Step 8: Write each line followed by a newline character to separate them
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Step 9: Close the file, which is important to make sure everything gets saved
print("And finally, we close it.")
target.close()

