#This code calculates the areas of a circle, rectangle, and triangle.
#imports the math module to access the value of pi.
import math

#Creates a function for the circle area calculation.
def calculate_circle_area(radius):
    pi = math.pi
    return pi * radius ** 2

#Creates functions for rectangle area calculation.
def calculate_rectangle_area(height, width):
    return height * width

#Creates function for triangle area calculation.
def calculate_triangle_area(base, height):
    return 0.5 * base * height

#Main program starts here. It is a loop that gets user input and calls the functions to calculate areas.
while True:
    print("Area Calculation Program.")
    print("1. Circle Area")
    print("2. Rectangle Area")
    print("3. Triangle Area")
    print("4. Exit")

    #prompts the usser to choose an option. That option is stored in the variable choice to be used in the if statments below.
    choice = input("Choose an option (1-4): ")
    print()

    #User inputs for circle area calculation. Calls the def funtion of a circle area. 
    if choice == "1":
        radius = float(input("Enter the radius of the circle: "))
        circle_area = calculate_circle_area(radius)
        print(f"Area of the circle with a radius of {radius} is: {circle_area:.4f}")
        print()

    elif choice == "2":
        #User inputs for rectangle area calculation. Calls the def funtion of a rectangle area. 
        height = float(input("Enter the height of the rectangle: "))    
        width = float(input("Enter the width of the rectangle: "))
        rectangle_area = calculate_rectangle_area(height, width)
        print(f"Area of the rectangle with the height of {height} and width of {width} is: {rectangle_area:.4f}")
        print()

    elif choice == "3":
        #User inputs for triangle area calculation. Calls the def funtion of a triangle area. 
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        triangle_area = calculate_triangle_area(base, height)
        print(f"Area of the triangle with the base of {base} and height of {height} is: {triangle_area:.4f}")
        print()
    
    #exits the program using the break statement to break the while loop. 
    elif choice == "4":
        print("Exiting the program.")
        break

    #Handles invalid input.
    else:
        print("Invalid choice. Please select a valid input (1-4).")