# This Python program demonstrates more advanced uses of string formatting.
# The 'format' method can take multiple arguments to populate multiple placeholders in a string.

# Defining a string with placeholders
formatter = "{} {} {} {}"

# Using 'format' to replace placeholders with numbers
print(formatter.format(1, 2, 3, 4))

# Using 'format' to replace placeholders with strings
print(formatter.format("one", "two", "three", "four"))
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))