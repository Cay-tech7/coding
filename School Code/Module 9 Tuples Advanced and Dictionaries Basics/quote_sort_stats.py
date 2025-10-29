#this code reads quotes from a text file, processes them into tuples, and generates a report sorted by quote length, author, total quotes, average length, and the quote with the most words.

quotes_list = [] #list to store tuples of (quote, author_id)

#find and read the file
with open(r"c:\Users\cayde\Documents\UVU Fall 2025\Fundamentals of Programming CS1400-x01\code_folder\School Code\Module 9 Tuples Advanced and Dictionaries Basics\quotes_data.txt", "r") as file:
    for line in file: #goes line by line
        quote, author_id = line.strip().split("|") #split line into quote and author_id
        tuple_data = (quote, author_id) #create tuple
        quotes_list.append(tuple_data) #add tuple to list

def generate_quote_report(quotes_list):      
    #sort by length of quote
    length_tuple_pairs = [(len(quote), author, (quote, author)) for quote, author in quotes_list] #create list of (length, author, tuple) pairs
    length_tuple_pairs.sort()  # sorts by length first, then author
    new_list = [quote_tuple for length, author, quote_tuple in length_tuple_pairs] #extract sorted tuples

    ###compute and display###
    #total number of quotes
    total_quotes = len(quotes_list)

    #average length of quotes(rounded to nearest integer)
    total_length = sum(len(quote) for quote, author in quotes_list) #sum lengths
    average_length = round(total_length / total_quotes) #compute average length


    #quote with the most words
    for quote, author in new_list[::-1]:  #start from longest quote, by grabbing from the end of sorted list
        word_count = len(quote.split()) #count words
        print(f'Quote with the most words ({word_count} words): "{quote}" | Author: {author}')
        break

    #store sorted quotes to new file
    with open("sorted_quotes.txt", "w") as output_file: #open new file for writing
        output_file.write("Quotes sorted by length:\n") 
        output_file.write(f"Longest quote has {len(new_list[-1][0])} characters. {new_list[-1][0]}\n\n") #grabs the longest quote, which is the last in the sorted list, and shows what it is
        output_file.write(f"Average quote length: {average_length} characters.\n\n") #writes average length
        for quote, author in new_list: #writes each sorted quote
            output_file.write(f'"{quote}" | {author}\n') #writes each sorted quote

if __name__ == "__main__":
    generate_quote_report(quotes_list)