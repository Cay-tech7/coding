# this code is to define 3 equations using additon, subtraction, multiplicaiton, and division.
# I will show, for each equation, at lesat two varions by changing the placement of parentheses. 

#equation 1 and its variants
equation1 = 2 + 3 * 4
equation1_variant = (2 + 3) * 4
equation1_variant2 = 2 + (3 * 4)

#equation 2 and its variants
equation2 = (10 - 6 / 2)
equation2_variant = (10 - 6) / 2
equation2_variant2 = 10 - (6 / 2)

#equation 3 and its variants
equation3 = 5 * 4 + 8 / 2
equation3_variant = (5 * 4) + (8 / 2)
equation3_variant2 = 5 * (4 + 8) / 2

# Print results, I noticed that when the divisision is involved, the result is show in a float 
print(f"Equation 1: 2 + 3 * 4")
print(f"Equation 1 Variant 1: (2 + 3) * 4 = {equation1_variant}")
print(f"Equation 1 Variant 2: 2 + (3 * 4) = {equation1_variant2}")
print()
print(f"Equation 2: 10 - 6 / 2")
print(f"Equation 2 Variant 1: (10 - 6) / 2 = {equation2_variant}")
print(f"Equation 2 Variant 2: 10 - (6 / 2) = {equation2_variant2}")
print()
print(f"Equation 3: 5 * 4 + 8 / 2")
print(f"Equation 3 Variant 1: (5 * 4) + (8 / 2) = {equation3_variant}")
print(f"Equation 3 Variant 2: 5 * (4 + 8) / 2 = {equation3_variant2}")