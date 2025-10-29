# this is a guessing game wher ea tuple stores a random set o fnumbers and the user attempts to guess them. 
import random

def player_guess(player_input):
    try:
        return tuple(int(num) for num in player_input.strip().split())
    except ValueError:
        print("Invalid input. Please enter 5 integers separated by spaces.")
        print()
        return ()
    
def compare_tuples(numbers, tuple_data):
    correct_positions = 0
    for i in range(len(numbers)):
        try:
            if numbers[i] == tuple_data[i]:
                correct_positions += 1
        except (IndexError, ValueError):
            continue
    return correct_positions

def play_game():
        numbers = tuple(random.randint(1,20) for _ in range(5))
        guess_number = 1
        best_match = 0
        best_guess_tuple = ()

        print("Welcome to the Tuple Guessing Game!")
        print("I have selected 5 random numbers between 1 and 20.")
        print("You have 5 attempts to guess the correct numbers in the correct positions.")
        print("Separate your numbers with spaces.")
        print()
        while guess_number <= 5:
            player_input = input(f"You are on guess {guess_number}/5. Try and guess the numbers in the list.")

            tuple_data = player_guess(player_input)

            if len(tuple_data) != 5:
                print("Please enter exactly 5 numbers.")
                print()
                continue
            correct_positions = compare_tuples(numbers, tuple_data)
            print(f"You have {correct_positions} number(s) in the correct position.")
            print()

            if correct_positions > best_match:
                best_match = correct_positions
                best_guess_tuple = tuple_data

            if correct_positions == 5:
                print("Congratulations! Oh my gosh, you did it! You guessed the correct combination!")
                print()
                break

            guess_number += 1

        if guess_number > 5:
            print(f"This game is hard, even the guy who made it couldn't beat his own game!")
            print(f"The correct combination was: {numbers}")

            if best_guess_tuple:
                print(f"Your best guess was: {best_guess_tuple}")
                print(f"Your best attempt had {best_match} correct positions.")
                percentage_match = (best_match / 5) * 100
                print(f"That's a {percentage_match}% match.")
            else:
                print("You did not make any valid guesses.")
                print()

if __name__ == "__main__":
    while True:
        play_game()  # Play one complete game

        # Ask if they want to play again
        play_again = input("Would you like to play again? (y/n): ").lower().strip()
        
        if play_again in ['n', 'no']:
            print()
            print("Thanks for playing!")
            break
        elif play_again not in ['y', 'yes']:
            print()
            print("Please enter 'y' for yes or 'n' for no.")

        print()
        print("------------------------------------------------")
        print()
