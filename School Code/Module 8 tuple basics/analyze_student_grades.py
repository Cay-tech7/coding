#this program stores student names and grades using tuples, then analyzes the data to print statistics.
#list of tuples containing student names and their grades
students = [("Bob", 87), ("Iceman", 92), ("Mav", 93), ("Hangman", 85)]

def analyze_grades(students):
    grades = [grade for name, grade in students] # loops through each tuple in students list, unpacks the tuple into name and grade, and collects the grades (ignores the name) into a new list
    average = sum(grades) / len(grades) #average grade calculation
    highest_grade = max(grades) #highest grade calculation
    lowest_grade = min(grades) #lowest grade calculation

    # Find the names of students with the highest and lowest grades
    highest_student = next(name for name, grade in students if grade == highest_grade) #this loops through eac tuple in students, and checks if the student's grade equal the hgighest grade, if yes, then it grabs the students name
    lowest_student = next(name for name, grade in students if grade == lowest_grade) #same as above, but for lowest grade

    # Return all statistics as a single tuple
    return (average, highest_grade, highest_student, lowest_grade, lowest_student)
    

if __name__ == "__main__":
    avg, high, high_name, low, low_name = analyze_grades(students) #calls the function and unpacks the returned tuple
    print(f"Average grade: {avg:.2f}")
    print(f"Highest grade: {high} {high_name}")
    print(f"Lowest grade: {low} {low_name}")
