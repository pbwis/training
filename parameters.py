# Example of import modules.
# Run script example: python3 parameters.py Toyota white 23411
from sys import argv

script, car, colour, mileage = argv

print("This script is called:", script)
print("The model of car is:", car)
print("Colour of body is:", colour)
print("Mileage:", mileage)