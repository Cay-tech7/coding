# This program calculates the food ration allocation for colonists during a festival.
#It uses snake_case, f strings, makes 2 decimal places where asked.
# user inputs for number of colonists and total food units available
number_of_colonists = int(input("Enter the number of colonists: "))
food_units = int(input("Enter the total number of food units available: "))


# calculations for ration allocation and remaining stockpile
total_ration_needed = 4 * number_of_colonists
remaining_festival_stockpile = food_units - total_ration_needed

#Zerins share, they get 15% of the remaining stockpile after allocation, but before distribution
zerinshare = remaining_festival_stockpile * 0.15
remaining_festival_stockpile -= zerinshare

#Lyras share, they get 10% of the remaining stockpile after Zerin's share is taken out
lyrashare = remaining_festival_stockpile * 0.10
remaining_festival_stockpile -= lyrashare

# Remainig distribution, this is what each colonist gets after zerin and lyra take their shares, plus their base 4 food units
colonist_share = remaining_festival_stockpile / number_of_colonists
colonist_share = colonist_share + 4


#add in the portion to zyrin and lyra
zerinshare += colonist_share
lyrashare += colonist_share

# output the results using f-strings for formatting and two decimal places
print(f"Zerin's share: {zerinshare:.2f}")
print(f"Lyra's share: {lyrashare:.2f}")
print(f"Share per colonist: {colonist_share:.2f}")
