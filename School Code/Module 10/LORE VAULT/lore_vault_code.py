#this code reconstructs a book from a scrambled archive file

#function to reconstruct a book from a scrambled archive file
def reconstruct_book(book_code):
    #read the contents of the scrambled archive file
    with open (book_code, "r") as input_file: #open the input file for reading
        lines = input_file.readlines() #read all lines into a list

    #reconstruct the correct order of the the lines by sorting based on their line numbers
    line_dict = {} #line number as key, line text as value
    for line in lines: #iterate through each line in the file
        line_number, line_text = line.split("|", 1) #split line into line number and text
        line_dict[int(line_number)] = line_text.rstrip("\n") #line number as int key, line text as value without newline
    ordered_lines = [line_dict[key] for key in sorted(line_dict.keys())] #list of lines ordered by line number

    #identify the longest line in the book (if multiple lines tie, choose the one with the higher line number)
    longest_line_length = 0 
    longest_line_number = 0
    for line_number, line_text in line_dict.items(): #iterate through line number and text pairs
        line_length = len(line_text) #get length of current line
        #check if this line is longer or ties with the current longest line
        if line_length > longest_line_length or (line_length == longest_line_length and line_number > longest_line_number): #update if longer or tie with higher line number
            longest_line_length = line_length #update longest line length
            longest_line_number = line_number #update longest line number
            longest_line_text = line_text #line text of the longest line

    #compute the average line length (rounded to the nearest integer)
    total_length = sum(len(line) for line in ordered_lines) #sum lengths of all lines
    average_length = round(total_length / len(ordered_lines)) #compute average length rounded to nearest integer

    #write all this information in o a new file named <BOOKCODE>_book.txt, structured as follows
    output_file_name = book_code.replace(".txt", "_book.txt") #create output file name
    with open(output_file_name, "w") as output_file: #open output file for writing
        output_file.write(f"{book_code.replace('.txt','')}\n\n") #write book code
        output_file.write(f"Longest line ({longest_line_number}): {longest_line_text}\n\n") #write longest line info
        output_file.write(f"Average length: {average_length}\n\n") #write average length info
        for line in ordered_lines: #write ordered book content lines
            output_file.write(f"{line}\n") #write each line followed by newline
        
        

if __name__ == "__main__":
    reconstruct_book("ALG.txt") 
