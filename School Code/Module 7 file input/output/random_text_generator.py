#Create a Python script that generates random text made of lowercase words and writes it into a file using modular functions.
import random
import string

# Function to generate a random word of given length
def make_word():
    length = random.randint(5, 10)  # Random word length between 5 and 10
    return ''.join(random.choices(string.ascii_lowercase, k=length))  # Generate random word


def make_line():
    num_words = random.randint(8, 10)  # Random number of words in a line
    words = [make_word() for _ in range(num_words)]  # Generate list of random words
    return ' '.join(words)  # Join words into a single line

def write_random_text():
    num_lines = int(100)  # 100 lines of random text
    with open('random_text.txt', 'w') as file:  # Open file for writing
        for _ in range(num_lines):
            line = make_line()  # Generate a random line
            file.write(line + '\n')  # Write line to file
    print("Random text written to 'random_text.txt'")  # Confirmation message

if __name__ == "__main__":
    write_random_text()  # Call the function to write random text to file
