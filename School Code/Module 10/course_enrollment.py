#This code manages student course enrollments using a dictionary.
# Each student has a unique ID, name, major, and a list of enrolled courses.
# The program allows printing student info, enrolling in new courses, and dropping students.

#dictionary of students
students = {
"S001": {"name": "Maverick", "major": "CS", "courses": ["CS1400", "MATH1210"]},
"S002": {"name": "Goose", "major": "IS", "courses": ["INFO2410", "CS1400"]},
"S003": {"name": "Iceman", "major": "DS", "courses": ["STAT1040", "CS1400"]}
}

# prints student information based on student ID
def print_student_info(student_id):
    student = students.get(student_id) # retrieves student info or None if not found
    if student:
        print("Student ID: ", student_id)
        print("Name: ", student.get("name")) #.get() method to safely access dictionary values
        print("Major: ", student.get("major")) #
        print("courses: ", student.get("courses"))
    else: 
        print("Student not found.")

# adds a course to a student's course list (avoids duplicates)
def enroll_student(student_id, course_code):
    student = students.get(student_id) 
    if student:
        #Ensures the "courses" key exists, if not create it with an empty list
        courses = student.setdefault("courses", []) #returns the list of courses or creates an empty list
        if course_code not in courses: #checks for duplicates
            courses.append(course_code) #adds the course
            print(f"Enrolled {student['name']} in {course_code}.") 
        else:
            print(f"{student['name']} is already enrolled in {course_code}.")

#completely removes a course from a student's cfrom the dictionary
def drop_student(student_id):
    student = students.get(student_id)
    if student:
        students.pop(student_id) #removes the student from the dictionary using the pop() method
        print(f"Removed student {student_id} from records.")


if __name__ == "__main__":
    print(f"Student key ID's: ", students.keys()) #prints all the keys in the dictionary
    print()
    print_student_info("S001")
    print()
    enroll_student("S001", "DOGFIGHTING 101")
    print()
    drop_student("S002")
    print()
    print(f"Summary\n" , students.items()) #prints all key-value pairs in the dictionary, showing current state, now that student S002 has been removed