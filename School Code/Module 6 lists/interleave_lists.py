# this code takes two lists of integers, one even and one odd,  and returns a new listthat interleaves the values in alternating order
def interleave(odds, evens):
    interLeaved = []  # Initialize an empty list to store the interleaved result
    min_length = min(len(odds), len(evens))  # Find the length of the shorter list
    for i in range(min_length):  # Iterate through the indices of the shorter list
        interLeaved.append(odds[i])  # Add an odd number
        interLeaved.append(evens[i])  # Add an even number
    interLeaved.extend(odds[min_length:])  # Add any remaining odd numbers
    interLeaved.extend(evens[min_length:])  # Add any remaining even numbers
    return interLeaved  # Return the final interleaved list

if __name__ == "__main__":  # code to run when executed directly
    odds = [11, 33, 55]
    evens = [22, 44, 66, 88]
    result = interleave(odds, evens)  # Call the interleave function
    print(f"Here is your Interleaved list: {result}")  # Print the resulting interleaved list clearly
