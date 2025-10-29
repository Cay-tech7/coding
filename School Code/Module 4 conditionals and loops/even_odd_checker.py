#This code checks to see if the number is even or odd, or quit the program

#has a loop to determin to check or quit
#determines if the number is even or odd

def even_odd_checker():
    while True:
        option = input("Enter option: 'c' to check, 'q' to quit: ").lower()
        if option == 'q':
            print("--------------------------------")
            print("Exiting the program.")
            print("--------------------------------")
            break
        elif option == 'c':
            try:
                number = int(input("Enter a number to see if it's even or odd: "))
                if number % 2 == 0:
                    print(f"Your entered number, {number}, which is even.")
                else:
                    print(f"Your entered number, {number}, which is odd.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        else:
            print("Invalid option. Please enter 'c' to check or 'q' to quit.")

even_odd_checker()