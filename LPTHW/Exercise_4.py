# This Python program demonstrates basic arithmetic operations with variables.
# Variables are used to store information that can be referenced and manipulated in a program.

# The number of cars available
cars = 100

# The space available in each car
space_in_a_car = 4.0

# The number of drivers available
drivers = 30

# The number of passengers
passengers = 90

# Calculating the number of cars not driven
cars_not_driven = cars - drivers

# Calculating the number of cars driven
cars_driven = drivers

# Calculating the total carpool capacity
carpool_capacity = cars_driven * space_in_a_car

# Calculating the average passengers per car
average_passengers_per_car = passengers / cars_driven
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")