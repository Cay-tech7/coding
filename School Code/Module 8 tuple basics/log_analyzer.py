# this code will read data from a file, parsing components, and perform baic statistics
# it will read server_logs.txt
#it will count how many times each severity level appears by spliting each line into severity level and log message
#it will identify the longest message by character count

severity_count = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}  # initialize severity count dictionary
longest_message = ""  # variable to track the longest message

#read each line
try:
    with open('c:/Users/cayde/Documents/UVU Fall 2025/Fundamentals of Programming CS1400-x01/code_folder/School Code/Module 8 tuple basics/server_logs.txt', 'r') as file: #I had to use the exact location
        for line in file: #goes line by line
            parts = line.strip().split("|")  #strips and splits each line into parts based on the '|' delimiter
            if len(parts) == 2: #check if there are exactly 2 parts after splitting
                severity = parts[0].strip() #get the severity level
                message = parts[1].strip() #get the log message

            #count how many times each severity level appears
            if severity in severity_count: #check if severity is one of the keys in the dictionary
                severity_count[severity] += 1 #increment the count for that severity level

            #identify the longest message (by character count)
            if len(message) > len(longest_message): #compare the length of the current message with the longest message found so far
                longest_message = message #update the longest message if the current one is longer
except FileNotFoundError: #handle the case where the file does not exist
    print("The file server_logs.txt was not found.")
    exit(1) #exit the program with a non-zero status to indicate an error

#writes the output to a new file named log_summary.txt
with open('log_summary.txt', 'w')as file: #open the file in write mode
    file.write("Log Summary\n")
    for level, count in severity_count.items(): #loop through each severity level and its count
        file.write(f"{level} : {count}\n") #write the severity level and its count to the file
    file.write(f"Longest message:  {longest_message}") #write the longest message to the file