# This code processes a lore vault text file, sorts its lines based on numeric identifiers,
# finds the longest line, calculates the average line length, and writes the results to an output file.
# I got help from AI to teach me a solution the sort_lines function and to add the .endswith function in the main function.
# All comments are my understanding of the code functionality

import os
import sys

def read_archive(filename):
    parsed_lines = [] #placeholder for parsed lines
    with open(filename, 'r', encoding='utf-8') as file: #open the file with UTF-8 encoding
        for line in file: #read each line
            if "|" in line: #check for delimiter
                content, number = line.rsplit("|", 1) #split line at last delimiter
                parsed_lines.append((int(number.strip()), content.strip())) #store as tuple
    return parsed_lines 

def sort_lines(lines): #sort lines based on numeric identifier (AI helped me here for this function)
    for i in range(len(lines)): #loops through each line in the book
        for j in range(0, len(lines)-i-1): #this loop goes through each line except the sorted ones
            if lines[j][0] > lines[j+1][0]: #this loop compaires the first line to the next line
                lines[j], lines[j+1] = lines[j+1], lines[j] #swaps if out of order using tuples
    return lines

def longest_line(lines): #find the longest line
    max_length = -1 #initialize max length
    longest = (0, "") #placeholder for longest line info
    for line_number, content in lines: #iterate through lines
        if len(content) > max_length or (len(content) == max_length and line_number > longest[0]): #check for longest or tie with higher line number
            max_length = len(content) #update max length
            longest = (line_number, content) #update longest line info
    return longest

def average_line_length(lines):
    total_length = 0 #initialize total length
    for line in lines: #iterate through lines
        total_length += len(line[1]) #get length of current line
    average_length = total_length / len(lines) if lines else 0 #calculate average
    return average_length   

def write_output(book_code, sorted_lines, longest_line_info, average_length): #write output to file
    output_filename = book_code.replace(".txt", "") + "_book.txt" #output filename
    with open(output_filename, 'w', encoding='utf-8') as output_file: #open file for writing
        output_file.write(f"{book_code.replace('.txt', '')}\n\n") #write book code
        output_file.write(f"Longest line ({longest_line_info[0]}): {longest_line_info[1]}\n\n") #write longest line info
        output_file.write(f"Average length: {round(average_length)}\n\n") #write average length
        for line in sorted_lines: #write sorted lines
            output_file.write(f"{line[1]}\n") #write line content

def main():
    if len (sys.argv) != 2: #check for correct number of arguments
        print("Usage: python lore_vault.py <BOOK_CODE>") #
        return
    book_code = sys.argv[1] #get book code from command line
    
    # Add .txt extension if not already present
    if not book_code.endswith(".txt"): # check if book_code ends with .txt (AI helped me here with the .endswith function)
        book_code = book_code + ".txt"
    
    if not os.path.isfile(book_code): #check if file exists
        print(f"Error: File {book_code} does not exist.") #error message
        return
    
    lines = read_archive(book_code)
    sorted_lines = sort_lines(lines)
    longest_line_info = longest_line(sorted_lines)
    average_length = average_line_length(sorted_lines)
    write_output(book_code, sorted_lines, longest_line_info, average_length)

if __name__ == "__main__":
    main()