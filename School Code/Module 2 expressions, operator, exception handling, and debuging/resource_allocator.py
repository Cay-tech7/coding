# Author: Cayden Eastman
# Date: 8-5-2024
# This code calculates the distribution of food resources among colonists in a space colony. 
# The distribution is based on rules for the captain, second-in-command, and other crew members, who all get different amounts.


#welcome message
print("Resource Allocation for Space Colony")
print("----")

# user inputs
number_of_colonists = int(input("Enter the number of colonists: "))
food_units = int(input("Enter the total number of food units available: "))

# crew members, not including Mira and Tov, get 3 food units each
crew_members = number_of_colonists - 2
shore_leave = round(crew_members* 3, 2)
shore_leave_per_crew_member = round(shore_leave / crew_members, 2)
remaining_after_shore_leave = round(food_units - shore_leave, 2)

# captain's share: 13% of remaining stockpile
miras_share = round(remaining_after_shore_leave * 0.13, 2)
remaining_after_miras_share = round(remaining_after_shore_leave - miras_share, 2)

# second-in-command's share: 11% of remaining after captain's share
tovs_share = round(remaining_after_miras_share * 0.11, 2)
remaining_after_tovs_share = round(remaining_after_miras_share - tovs_share, 2)

# remaining food evenly split among all colonists (including Mira and Tov)
final_share_per_colonist = round(remaining_after_tovs_share / number_of_colonists, 2)

# add final share to Mira and Tov
miras_share = round(miras_share + final_share_per_colonist, 2)
tovs_share = round(tovs_share + final_share_per_colonist, 2)

#add shore leave to crew members, which excludes Mira and Tov
final_share_per_crew_member = round(final_share_per_colonist, 2) + (shore_leave_per_crew_member)

# display
print("----")
print("Displaying results:")
print()
print(f"How many colonists: {number_of_colonists}")
print(f"How many total food units: {food_units}")
print(f"Mira's share: {miras_share:.2f}")
print(f"Tov's share: {tovs_share:.2f}")
print(f"Each colonist's share: {final_share_per_crew_member:.2f}")
print("----")

# checks to see the total distributed food
# I don't think the calculation is off or that I'm not rounding correctly, but that it is a matter of floating point numbers?
total_distributed = round(miras_share + tovs_share + (final_share_per_crew_member * crew_members), 2)
print(f"Total food distributed: {total_distributed:.2f}")
print("----")