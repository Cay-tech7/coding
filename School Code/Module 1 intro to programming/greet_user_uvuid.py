"""
This program prompts the user for their name and UVU ID number,
validates the ID number to ensure it is exactly 8 digits long.
"""

name = str(input("Enter your name: "))
while True:
    try:
        id = int(input("Enter your UVU ID number: "))
        length = len(str(id))
        if length != 8:
            print("Error: UVU ID number must be 8 digits long.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Hello, " + name + "! Your UVU ID is " + str(id)+".")