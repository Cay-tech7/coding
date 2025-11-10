def process_grades(grades):
    #uses a list comprehension to filter out invalid grades (less than 0 or greater than 100)
    valid_grades = [grade for grade in grades if 0 <= grade <= 100] #Iterate through grades and keep only valid ones
    print(f"Valid grades: {valid_grades}") 
    if not valid_grades: #if there is no valid grades
        print("No valid grades to process.")
        return

    # Inner ed function to calculate grade distribution
    def grade_distribution(valid_grades):
        counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0} #initialize counts with a dictionary
        for grade in valid_grades: #iterate through valid grades
            if 90 <= grade <= 100: #check for grade ranges
                counts["A"] += 1 #increment count for A
            elif 80 <= grade <= 89: #repeats for other grades
                counts["B"] += 1
            elif 70 <= grade <= 79:
                counts["C"] += 1
            elif 60 <= grade <= 69:
                counts["D"] += 1
            else:
                counts["F"] += 1
        return counts
    
     #call functions to process grades   
    calculate_average(grades) #calls on helper function to calculate average
    grade_distribution(valid_grades) #calls on inner function to get grade distribution
    
    average = calculate_average(valid_grades) #calculate average using helper function
    print(f"Average grade: {average:.2f}") #print average with 2 decimal places
    print(f"Grade distribution: {grade_distribution(valid_grades)}") #print grade distribution
    
# helper function to calculate average
def calculate_average(valid_grades):
    total = sum(valid_grades)
    count = len(valid_grades)
    return total / count if count > 0 else 0 #avoid division by zero
    
# Main execution
if __name__ == "__main__":
    grades = [
        95, 82, 76, 59, 89, 101, -10, 67, 73, 88, 92, 105, 45, 60, 78, 84, 99, 100, 102, 38,
        91, 85, 77, 66, 54, 49, 81, 93, 97, 103, 40, 35, 29, 62, 74, 80, 90, 98, 87, 83,
        70, 65, 58, 50, 47, 44, 30, 25, 20, 15, 10, 5, 0, -5, -20, 110, 120, 115, 108, 106,
        96, 94, 86, 79, 75, 72, 68, 64, 61, 57, 53, 48, 43, 39, 34, 28, 22, 18, 12, 8,
        3, 2, 1, -1, -3, -7, -15, 104, 107, 109, 111, 113, 114, 116, 117, 118, 119, 122, 125, 130
    ]
 # Example list of grades
    process_grades(grades) #process the grades