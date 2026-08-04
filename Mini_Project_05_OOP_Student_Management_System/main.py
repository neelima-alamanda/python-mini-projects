# Importing the necessary classes from their respective modules
from student import Student, GraduateStudent
from course import Course

# Create instances of Student
# `Student` objects are initialized with a unique ID, a name, and a GPA
student1 = Student(101, "Thomas", 3.8)
student2 = Student(102, "John", 4.0)

# Create an instance of GraduateStudent
# `GraduateStudent` inherits from `Student` and includes an additional attribute for research topic
graduate_student1 = GraduateStudent(103, "Bob", 3.4, "AI")

# Create an instance of Course
# A `Course` object is initialized with a unique course ID and course name.
course1 = Course("C101", "Python")

# Adding students to the course
# Each `add_student` call enrolls a student in the course.
# A student can be a regular student or a graduate student.
course1.add_student(student1)  # Adds Thomas (Student) to the course
course1.add_student(student2)  # Adds John (Student) to the course
course1.add_student(graduate_student1)  # Adds Bob (GraduateStudent) to the course

# List all students enrolled in the course
# This will display information about each student, including ID, name, GPA, and (for graduate students) their research topic.
print("\n--- Students Enrolled ---")
course1.list_students()

# Update the GPA of a specific student (student1 in this case)
# Prompts the user to enter a new GPA, validates it, and updates it for the student if valid.
print("\n--- Update GPA ---")
student1.update_gpa()

# Remove a student from the course
# This prompts the user to input the ID of the student to be removed.
# If the ID exists, the student is removed, otherwise an error is displayed.
print("\n--- Remove Student ---")
course1.remove_student()

# List the students again after one of them has possibly been removed
# This helps verify that the `remove_student` functionality worked as expected.
print("\n--- Updated Student List ---")
course1.list_students()