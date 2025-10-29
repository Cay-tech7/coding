#create an empty dictionary to store student names and their scores
scorebook = {}

#add some students and their scores to the dictionary
scorebook["Alice"] = 88
scorebook["Bob"] = 75
scorebook["Charlie"] = 93
scorebook["Dana"] = 80
print("-------------------------------------------")

#print the scorebook
for student, score in scorebook.items():
    print(f"{student}: {score}")

#updates dana's scores
scorebook["Dana"] = 85
print(f"Dana's updated score: {scorebook['Dana']}")

#delete bob from the scorebook
removed_score = scorebook.pop("Bob") #removes Bob and stores his score
print("Bob has been removed from the scorebook.")

#check if eve is in the scorebook and print a message if not
if scorebook.get("Eve") is None: #checks if Eve is not in the dictionary
    print("Eve is not in the scorebook.")
else: 
    print("Eve is in the scorebook.")

#print average score of all remaining students
total_score = sum(scorebook.values()) #sums up all the scores in the dictionary by using values() method
number_of_students = len(scorebook) #gets the number of students remaining in the dictionary and stores it in a variable
average_score = total_score / number_of_students #calculates average score from total score and number of students
print(f"Average score: {average_score:.2f}") #prints average score formatted to 2 decimal places

#double check new scorebook contents
print("------------------------------------------")
print("Final scorebook contents:")
for student, score in scorebook.items():
    print(f"{student}: {score}")
