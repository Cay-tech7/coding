
# This program calculates the food ration allocation for colonists during a festival.
#It uses snake_case, f strings, makes 2 decimal places where asked.
# user inputs for number of colonists and total food units available
number_of_colonists = int(input("Enter the number of colonists: "))
food_units = int(input("Enter the total number of food units available: "))

# calculations for ration allocation and remaining stockpile
total_ration_needed = 4 * number_of_colonists
remaining_festival_stockpile = food_units - total_ration_needed

# output the results using f-strings for formatting and two decimal places
print(f"Original supply: {food_units:.2f} units")
print(f"Ration allocation (4 units per colonist): {total_ration_needed:.2f}")
print(f"Festival stockpile remaining: {remaining_festival_stockpile:.2f}")