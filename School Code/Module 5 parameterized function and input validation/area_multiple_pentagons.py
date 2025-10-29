# this code is to have two functions that will calculate the are a of a single regualr pentagon and the total area of multiple pentagons using paramerterized functions. 
#import math
import math

#function of a regular pentagon and returns area as a floating point number
#validates the input to be a positive number
def areaRegularPentagon(side_length): # function that calculates the area of a regular pentagon
    try: # validate input
        side_length = float(side_length) # convert to float
        if side_length <= 0: # check if positive
            print("Invalid input: Side length must be a positive number.")
            return None # return None for invalid input
    except ValueError as e: # handle conversion error
        print(f"Invalid input: {e}") 
        return None
    area = (5 * side_length**2) / (4 * math.tan(math.pi / 5)) # formula for area of a regular pentagon
    return area

# function that calculates the total area of multiple regular pentagons
def areaMultiplePentagons(side_length, number_of_pentagons): # function that calculates the total area of multiple regular pentagons
    try: # validate input
        number_of_pentagons = int(number_of_pentagons) # convert to int
        if number_of_pentagons <= 0: # check if positive
            print("Invalid input: Number of pentagons must be a positive integer.")
            return None
    except ValueError as e: # handle conversion error
        print(f"Invalid input: {e}")
        return None
    single_area = areaRegularPentagon(side_length) # get area of a single pentagon from previous function
    if single_area is None: # check if single area calculation was successful
        return None
    total_area = single_area * number_of_pentagons # total area calculation
    return total_area

if __name__ == "__main__":
    # code to run when executed directly
    side_length = input("Enter the side length of the regular pentagon: ") #get user input
    print()
    number_of_pentagons = input("Enter the number of pentagons: ") #get user input
    print()
    print(f"Area of a single regular pentagon with side length {side_length}: {areaRegularPentagon(side_length)}") # display area of single pentagon
    print()
    print(f"Total area of {number_of_pentagons} regular pentagons with side length {side_length}: {areaMultiplePentagons(side_length, number_of_pentagons)}") # display total area of multiple pentagons
    print()