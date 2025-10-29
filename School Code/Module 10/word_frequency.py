#this code accepts a string of text and returns a dictionary with the frequency of each word in the text.
#it removes all punctuation and is case-insensitive.
#it also ignores words that were only used once

def word_count(text): #text is a list of strings
    instance_dict = {} #dictionary to hold word counts
    for line in text: #iterate through each line in the text
        line = line.split() #split the line into words
        for word in line: #iterate through each word in the line
            word = word.lower().strip('.,!?";:()[]{}<>') #convert to lowercase and remove punctuation
            if word in instance_dict: #if the word is already in the dictionary
                instance_dict[word] += 1 #increment the count
            else: #if the word is not in the dictionary
                instance_dict[word] = 1 #add the word to the dictionary with a count of 1
    return instance_dict #return the dictionary



if __name__ == "__main__":
    text = input("Enter text: ") #get input from the user
    result = word_count([text]) #call the word_count function with the input text


    # Print each word and its frequency using a for loop and .items()
    print("--------------------------------------------")
    print("All words and their frequencies:")
    for word, frequency in result.items(): #iterate through the dictionary items
        print(f"{word}: {frequency}") #print the word and its frequency

    # Remove words that were only used once
    filtered_dict = result.copy() #create a copy of the result dictionary
    for word in result: #iterate through the original dictionary
        if result[word] == 1: #if the word was only used once
            del filtered_dict[word] #remove it from the copied dictionary

    print("\n--------------------------------------------")
    print("Words used more than once:")
    for word, frequency in filtered_dict.items(): #iterate through the filtered dictionary items
        print(f"{word}: {frequency}") 


