# This program is a basic letter shifting utility that can shift any alphabetical character forward or backward by a fixed amount, similar to a Caesar Cipher.

def shift_character(char, shift, mode):

    # Ensure the character is a single alphabetical character
    if len(char) != 1:
        return "Error: Please enter a single character."
    
    #checks to see if the character is a integer, and if so, it returns the character unchanged
    if not char.isalpha():
        return char
    
    #This makes sure the shift is an integer
    try:
        shift = int(shift)
    except ValueError:
        return "Error: Shift value must be an integer."

    # this make sure the user only input forward or backward
    if mode == "backward":
        shift = -shift
    elif mode != "forward":
        return "Error: Mode must be 'forward' or 'backward'."
    
    #performs the shift by giving a library, assigning the character to an index, then shifts the index and returns the new character
    # Checks if the character is upper or lower case to maintain the case after shifting
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char.islower():
        alphabet = lower_alphabet
    else:
        alphabet = upper_alphabet

    #finds the index of the character, shifts it, and returns the new character from the given alphabet
    index = alphabet.index(char)
    # Use modulo 26 to wrap around the alphabet if the shift goes past 'z' or 'A'
    shifted_index = (index + shift) % 26
    return  alphabet[shifted_index]

#user inputs
char = input("Enter a character: ")
shift = input("Enter shift value: ")
mode = input("Enter direction (forward/backward): ").lower() 

#calls the function and prints the result, taking the user inputs as parameters
print("-----------------------------")
print (f"Shifted character: {shift_character(char, shift, mode)}")