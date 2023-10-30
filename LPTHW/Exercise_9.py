# This Python program demonstrates how to store and print multiple lines of text.
# It introduces the concept of multi-line strings and the usage of escape sequences.

# Defining a string containing the names of the days of the week
days = "Mon Tue Wed Thu Fri Sat Sun"

# Defining a multi-line string containing the names of the months
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")