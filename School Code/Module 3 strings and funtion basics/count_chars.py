#This program finds out how many times a specific character appears in a given string.

#inputs
string = input("Enter a string: ")
string_char = input("Enter a character to count: ")

#handels case sensitivity by converting both to lower case
string = string.lower()
string_char = string_char.lower()

# A function that takes the parameters string and string_char and then counts the instance of each character
def count_char(string, string_char):
    count = 0
    for char in string:
        if char == string_char:
            count += 1
    return count

#ensures that the string_char is a single character
if len(string_char) != 1:
    print("Please enter a single character to count.")
    exit()
    
#output the result
print(f"The character '{string_char}' appears {count_char(string, string_char)} time(s) in the string.")
