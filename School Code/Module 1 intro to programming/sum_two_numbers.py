#This program adds two integers together
#It prompts the user for an input and assigns it that value
#I used a while loop to make sure that the input is an integer and not something else like a float or a string, negative numbers are okay. 
#It is reapeated for a second integer
#Finally, it adds the two integers and prints the result
print("This program adds two integers together")

import sys

try:
    x = int(input("Enter a number:"))
except ValueError:
     print("Invalid input. Please run the program again, and do an integer this time.")
     sys.exit()

try:
     y = int(input("Enter another number:"))
except ValueError:
     print("Invalid input. Please run the program again, and do an integer this time.")
     sys.exit()

print("The sum of ", x, "and ", y, "is", x+y)
