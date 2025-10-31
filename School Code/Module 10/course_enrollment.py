students = {
"S001": {"name": "Alice", "major": "CS", "courses": ["CS1400", "MATH1210"]},
"S002": {"name": "Bob", "major": "IS", "courses": ["INFO2410", "CS1400"]},
"S003": {"name": "Charlie", "major": "DS", "courses": ["STAT1040", "CS1400"]}
}

def print_student_info(student_id):
    student = students.get(student_id)
    if student:
        print("Name: ", student.get("name"))
        print("Major: ", student.get("major"))
        print("courses: ", student.get("courses"))
    else: 
        print("Student not found.")

# adds a course to a student's course list (avoids duplicates)
def enroll_student(student_id, course_code):
    student   = students.get(student_id)
    if student:
        if course_code not in student["courses"]:
            student["courses"].update(course_code)
            print(f"Enrolled {student['name']} in {course_code}.")
        else:
            print(f"{student['name']} is already enrolled in {course_code}.")

#completely removes a course from a student's cfrom the dictionary
def drop_student(student_id):
    student = students.get(student_id)
    if student:
        students.pop(student_id)
        print(f"Removed student {student_id} from records.")


if __name__ == "__main__":
    print(f"Student key ID's: ", students.keys())
    print_student_info("S001")
    print()
    enroll_student("S001", "MATH1210")
    print()
    drop_student("S002")
    print(f"Summary\n" , students.items())