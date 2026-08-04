# Define a Course class to represent a course with a unique ID, name, and enrolled students
class Course:
    def __init__(self, course_id, course_name):
        """
        Initialize a Course object with a unique course ID and a course name.
        The course also maintains a list of students enrolled in it.

        Parameters:
        - course_id (str): The unique identifier for the course
        - course_name (str): The name of the course
        """
        self.course_id = course_id  # Unique identifier for this course
        self.course_name = course_name  # Name of the course
        self.enrolled_students = []  # List to store all students enrolled in this course

    def add_student(self, student):
        """
        Add a student to the course.
        If the student is already enrolled, notify the user and do not add the student again.

        Parameters:
        - student (Student): The student object to be added to the course
        """
        # Check if the student is already enrolled by comparing their ID
        for s in self.enrolled_students:
            if s.id == student.id:
                print("Student is already enrolled.")  # Notify if the student is a duplicate
                return

        # If student is not already enrolled, add them to the list
        self.enrolled_students.append(student)
        print("Student enrolled successfully.")  # Inform that the student was added

    def remove_student(self):
        """
        Remove a student from the course based on their ID.
        If the student ID is not found, notify the user.

        This method takes input from the user to identify the student ID.
        """
        # Prompt the user until a valid integer ID is entered
        while True:
            try:
                std_id = int(input("Enter student ID to remove: "))  # Ask for the student ID
                break
            except ValueError:
                # If a non-integer input is given, prompt again
                print("Please enter a valid integer for the student ID.")

        # Initialize a flag to track whether the student is found and removed
        found = False
        for s in self.enrolled_students:
            if s.id == std_id:
                # Remove the student from the list if the ID matches
                self.enrolled_students.remove(s)
                found = True
                print("Student removed successfully.")  # Notify the user of success
                break  # Exit the loop since the student is removed

        # If no matching student ID is found, notify the user
        if not found:
            print("Student not found.")  # Notify that the student ID does not exist in the course

    def list_students(self):
        """
        List all students currently enrolled in this course.
        If no students are enrolled, display an appropriate message.

        This method ensures that student details are displayed in a formatted manner.
        """
        # Check if there are no students enrolled and notify the user
        if not self.enrolled_students:
            print("No students enrolled.")
            return  # Exit the method early

        # Loop through each student in the enrolled list and display their information
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print("-" * 30)
        for s in self.enrolled_students:
            print("-" * 20)  # Separator for better formatting
            s.display_info()  # Call the student's display_info method to show their details