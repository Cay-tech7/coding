# Write a Python program that reads the contents of a text file and counts the occurrences of each vowel (a, e, i, o, u, y), regardless of case.

def vowel_count(word): #function that counts the number of each vowel in a given word
    a_count = word.count('a')
    e_count = word.count('e')
    i_count = word.count('i')
    o_count = word.count('o')
    u_count = word.count('u')
    return a_count, e_count, i_count, o_count, u_count

def clean_text(text):
    return ''.join([char for char in text if char.isalpha()]) #removes non alphabetic characters by checking if each character is alphabetic

def read_document():
    try: #tries to read the file
        with open('random_text.txt', 'r') as file: #opens the file
            text = file.read().lower()  # Read the file and convert to lowercase
            cleaned_text = clean_text(text) # Read the file and convert to lowercase
            a_count, e_count, i_count, o_count, u_count = vowel_count(cleaned_text)  # Count vowels
            total_vowels = a_count + e_count + i_count + o_count + u_count  # Total vowel count
            print(f"Total vowels: {total_vowels}")  # Print total count
            print(f"Here is the vowel count - a: {a_count}, e: {e_count}, i: {i_count}, o: {o_count}, u: {u_count}")  # Print counts

    except FileNotFoundError: #handles if the file is not found
        print("The file 'random_text.txt' was not found.")

if __name__ == "__main__": # code to run when executed directly
    read_document()