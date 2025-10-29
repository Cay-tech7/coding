# this code is a ceasar cipher cimulator with tow main fuctions, encoding and decoding.

def encode(text, shift):
    result = ""  # Initialize an empty string to store the encoded result
    for char in text:  # Iterate through each character in the input text
        if char.isalpha():  # Check if the character is an alphabet letter
            shift_base = ord('A') if char.isupper() else ord('a')  # Determine the base ASCII value based on case
            # Perform the shift and wrap around using modulo 26
            encoded_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += encoded_char  # Append the encoded character to the result
        else:
            result += char  # Non-alphabet characters are added unchanged
    return result  # Return the final encoded string

def decode(text, shift):
    return encode(text, -shift)  # Decoding is just encoding with a negative shift

if __name__ == "__main__":     # code to run when executed directly
    # Loop until a valid decision is entered
    while True:
        decision = input("Would you like to encode or decode a message? (e/d): ").strip().lower()
        if decision in ('e', 'd'):
            break
        else:
            print("Invalid choice: Please enter 'e' to encode or 'd' to decode.")
    print()
    message = input("Enter your message: ")  # Get the message to encode or decode
    print()
    while True:  # Loop until a valid positive shift value is entered
        try:
            shift = int(input("Enter the shift value (must be a positive integer): "))  # Get the shift value
            if shift > 0:
                break  # Exit loop if input is valid and positive
            else:
                print("Invalid input: Please enter a positive integer greater than zero.")
        except ValueError:
            print("Invalid input: Please enter a valid positive integer.")
    print()
    if decision == 'e':  # If the user chose to encode
        encoded_message = encode(message, shift)  # Call the encode function
        print(f"Encoded message: {encoded_message}")  # Display the encoded message
    else:  # decision == 'd'
        decoded_message = decode(message, shift)  # Call the decode function
        print(f"Decoded message: {decoded_message}")  # Display the decoded message

    

