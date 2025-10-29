#This code accepts a list of integers as a parameter and returns two new lists of even and odd numbers

def split_even_odd(numbers): # function that splits a list of integers into even and odd numbers
    even_numbers = [] # list to store even numbers
    odd_numbers = [] # list to store odd numbers
    for number in numbers: # iterate through the input list
        if number % 2 == 0: # check if the number is even
            even_numbers.append(number) # add to even list
        else:
            odd_numbers.append(number) # add to odd list
    return even_numbers, odd_numbers   # return both lists  

if __name__ == "__main__":   # code to run when executed directly
    while True:
        input_numbers = input("Enter a list of integers separated by spaces: ") # get user input
        if not input_numbers.strip():  # check for empty input
            print("No numbers were entered.")
            continue  # prompt again for input
        if any(not num.lstrip('-').isdigit() for num in input_numbers.split()):  # validate input by removing - for negative numbers and checking if all parts are digits
            print("Invalid input: Please enter only integers separated by spaces.")
            continue  # prompt again for input
        break  # exit loop if input is valid

    number_list = [int(num) for num in input_numbers.split()] # convert input string to a list of integers
    evens, odds = split_even_odd(number_list) # call the function

    # Sort the lists before printing
    number_list.sort()
    evens.sort()
    odds.sort()

    # printed output
    print("----------------------------------")
    print(f"Original list(sorted): {number_list}")
    print("----------------------------------")
    print(f"Even numbers: {evens}") 
    print("----------------------------------")
    print(f"Odd numbers: {odds}")

