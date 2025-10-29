# This program generates a series of numbers based on user input and saves them to a text file.
# It includes functions to generate the number series and save it to a file.

def generate_number_series(start, end, step):
    return list(range(start, end + 1, step))  # Generate number series using range

def save_to_file(number_series, filename='number_series.txt'):
    with open(filename, 'w') as file:  # Open file for writing
        for number in number_series:
            file.write(f"{number}\n")  # Write each number on a new line

if __name__ == "__main__":
    try:
            starting_number = int(input("Enter the starting number: "))  # Get starting number from user
            ending_number = int(input("Enter the ending number: "))      # Get ending number from user
            if starting_number >= ending_number:
                print("Invalid input: Starting number must be less than ending number.")
                exit(1)
            step = int(input("Enter the step value: "))                  # Get step value from user
            if step <= 0:
                print("Invalid input: Step value must be a positive integer.")
                exit(1)
            if starting_number + step > ending_number:
                print("Invalid input: Step value is too large for the given range.")
                exit(1)
    except ValueError:
            print("Invalid input: Please enter valid integers.")
            exit(1)
    
    number_series = generate_number_series(starting_number, ending_number, step)  # Generate the series
    save_to_file(number_series)  # Save the series to a file
    print("Generated number series has been added to 'number_series.txt'")  # Print the generated series

