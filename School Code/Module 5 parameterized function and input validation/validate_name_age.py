# this code collects a user's name and age with input validation
# this script will contineu to prompt the user until both inputs are valid, and then display a confimation message.

def validate_name(name):
    if not name.isalpha():  # Check if the name contains only alphabetic characters
        print("Invalid input: Name must contain only letters.")
        return False
    return True

def validate_age(age):
    try:
        age = int(age)  # Try to convert age to an integer
        if age <= 0:  # Check if the age is a positive integer
            print("Invalid input: Age must be a positive integer.")
            return False
        elif age > 130:  # Check if the age is within a reasonable range
            print("Invalid input: Age must be less than or equal to 130.")
            return False
    
    except ValueError: # Handle the case where conversion to int fails
        print("Invalid input: Age must be a positive integer.")
        return False
    return True

if __name__ == "__main__": # code to run when executed directly
    while True: # loop until valid name is entered
        name = input("Enter your name: ").strip().lower().capitalize() # get user input and strips whitespace, lowers all letter to lowercase and then capitalizes
        if validate_name(name): # calls validation function
            break  # Exit loop if name is valid

    print()  # print a blank line for better readability

    while True: # loop until valid age is entered
        age = input("Enter your age: ") # get user input
        if validate_age(age): # calls validation function
            break  # Exit loop if age is valid

    print()

print("-----------------------")
print(f"Very nice, {name}. You are {age} years old.") # display confirmation message
print("-----------------------")