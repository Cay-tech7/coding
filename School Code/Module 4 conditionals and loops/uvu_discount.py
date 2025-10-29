# This code is a discount calculator
#It finds out if the person bying the item is a student or faculty

#inputs
#makes sure the price is a valid number and not negative
while True:
    try:
        item_price = float(input("Enter the price of the item: $"))
        if item_price < 0:
            print("Error: Price cannot be negative.")
            continue
        break
    except ValueError:
        print("Error: Price must be a number.")

#checks if the person is a student, faculty, or neither
is_student = False
is_faculty = False
non_uvu = False
while True:
    person = input("Enter buyer type ('s' for student, 'f' for faculty, 'n' for neither): ").lower()
    if person in ('s', 'f','n'):
        if person == "s":
            is_student = True
        elif person == "f":
            is_faculty = True
        elif person =="n":
            non_uvu = True
        break
    else:
        print()
        print("Error: Please enter 's' for student, 'f' for faculty, or 'n' for neither.")
        print()

# Determine discount rate
if person == "s":
    discount_rate = 0.05  # 5% discount for students
elif person == "f":
    discount_rate = 0.08  # 8% discount for faculty
else:
    discount_rate = 0.0 #no discounts for non UVU individuals

# Calculate final price
discount_amount = item_price * discount_rate
final_price = item_price - discount_amount

#cashregister printout and outputs
if not (is_student or is_faculty):
    print("------------------------------")
    print("No discount applied.")
    
elif is_student:
    print("------------------------------")
    print("Student discount applied.")

elif is_faculty:
    print("------------------------------")
    print("Faculty discount applied.")
    
print(f"Final price for {item_price:.2f} after {discount_rate} discount is: ${final_price:.2f}")
print()
print("Thank you for shopping with us!")
print("------------------------------")