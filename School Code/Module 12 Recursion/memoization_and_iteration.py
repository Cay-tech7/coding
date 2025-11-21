# this code demonstrates three different approaches to calculate the nth term of the UVUnacii sequence: recursive, memoized, and iterative.
# I did need to look up how to implement memoization and iteration for this sequence. And AI helped me out with that.
import time

# recursive function to calculate the nth term of the UVUnacii sequence
def uvunacci_recursive(n): #function to calculate the nth term of the UVUnacii sequence recursively
    if n == 0: #base case
        return 0
    elif n == 1: #base case
        return 1
    elif n == 2: #base case because the UVUancii sequence starts with 0, 1, 2
        return 2
    return uvunacci_recursive(n-1) + uvunacci_recursive(n-2) + uvunacci_recursive(n-3) #recursive case: sum of the three preceding terms

# memoized function to calculate the nth term of the UVUnacii sequence
def uvunacci_memoized(n, memo_dict):
    if n in memo_dict:  # check if value already computed
        return memo_dict[n]
    if n == 0:  # base case
        return 0
    elif n == 1:  # base case
        return 1
    elif n == 2:  # base case
        return 2
    # compute the value and store it in the dictionary
    memo_dict[n] = uvunacci_memoized(n-1, memo_dict) + uvunacci_memoized(n-2, memo_dict) + uvunacci_memoized(n-3, memo_dict) #uses memoization to store previously computed values
    return memo_dict[n]

# iterative function to calculate the nth term of the UVUnacii sequence
def uvunacci_iterative(n):
    if n == 0:  # base case
        return 0
    elif n == 1:  # base case
        return 1
    elif n == 2:  # base case
        return 2

    uvu_sequence = [0, 1, 2]  # initialize the sequence with the first three terms
    for i in range(3, n + 1): # build the sequence iteratively
        next_value = uvu_sequence[i-1] + uvu_sequence[i-2] + uvu_sequence[i-3]  # calculate the next term
        uvu_sequence.append(next_value)  # append the next value to the sequence
    return uvu_sequence[n]

if __name__ == "__main__":
    n = input("Enter the number of terms for the UVUnacci sequence: ")
    if not n.isdigit() or int(n) < 0: #input validation by checking if input is a non-negative integer
        print("Please enter a non-negative integer.\n")
        exit(1)
    n = int(n)
    print(f"First {n} term(s): \n")

    # Recursive timing
    start = time.time() 
    recursive = [uvunacci_recursive(i) for i in range(n)]
    end = time.time()
    print(f"Recursive: {recursive} → Time: {end - start:.10f} seconds\n")

    # Memoized timing
    memo_dict = {}
    start = time.time()
    memoized = [uvunacci_memoized(i, memo_dict) for i in range(n)]
    end = time.time()
    print(f"Memoized: {memoized} → Time: {end - start:.10f} seconds\n")

    # Iterative timing
    start = time.time()
    iterative = [uvunacci_iterative(i) for i in range(n)]
    end = time.time()
    print(f"Iterative: {iterative} → Time: {end - start:.10f} seconds\n")

    #summary
    print("Summary of differences:\n - The recursive approach is straightforward but inefficient for large n due to repeated calculations. \n"
    "It is like walking up stairs but you forgot each step you took so you backtrack and try every possible combination of steps to reach the nth step.\n\n "

    "- The memoized approach optimizes the recursive method by storing previously computed values, significantly improving performance.\n "
    "It is like walking up stairs but you stop to write the steps you took to reach each step so you don't have to backtrack and try every possible combination of steps again.\n\n "

    "- The iterative approach is the most efficient in terms of time and space complexity, as it builds the sequence in a single pass without recursion overhead.\n"
    "It is like walking up stairs and keeping track of the last three steps you took to reach the nth step"
)