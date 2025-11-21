def uvunacci_recursive(n): #function to calculate the nth term of the UVUnacii sequence recursively
    if n == 0: #base case
        return 0
    elif n == 1: #base case
        return 1
    elif n == 2: #base case because the UVUancii sequence starts with 0, 1, 2
        return 2
    return uvunacci_recursive(n-1) + uvunacci_recursive(n-2) + uvunacci_recursive(n-3) #recursive case: sum of the three preceding terms
    
if __name__ == "__main__":
    n = input("Enter the number of terms for the UVUancii sequence: ") #get user input for number of terms
    if not n.isdigit() or int(n) < 0: #input validation by checking if input is a non-negative integer
        print("Please enter a non-negative integer.\n")
        exit(1) #exit the program with an error code

    n = int(n) #convert input to integer
    print(f"First {n} term(s): ")
    result = [uvunacci_recursive(i) for i in range(n)] #generates the UVUancii sequence up to n terms using list comprehension
    print(result)
