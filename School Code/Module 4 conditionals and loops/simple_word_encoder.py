#This code is a ceasar cipher encoder
#This was a tough one for me to figure out, because of the ascii values, so I added comments to each line
def shift_word(word, shift):
    word = input("Enter a word to: ").lower() #conversion to lower case
    shift = int(input("Enter the number of positions to shift (1-25): ")) #user input
    encoded_word = "" #empty string to store encoded word
    for char in word: #loop through each character in the word
        shifted = ord(char) + shift #uses the ascii value of the character and adds the shift value
        if shifted > ord('z'): #wrap around if it goes past 'z'
            shifted -= 26 #26 for all the letters in the alphabet
        encoded_word += chr(shifted) #convert back to character and add to encoded word
    print(f"Encoded word: {encoded_word}")
shift_word(0,0) #calls the function with values that will get replaced by user input by the inputs


