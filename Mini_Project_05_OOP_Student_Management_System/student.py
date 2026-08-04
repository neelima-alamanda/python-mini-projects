# Define a Student class to represent general student information
class Student:
    def __init__(self, id, name, gpa):
        """
        Initialize a Student object with a unique student ID, name, and GPA.

        Parameters:
        - id (int): A unique identifier for the student.
        - name (str): The name of the student.
        - gpa (float): The student's Grade Point Average (GPA), which should be in a valid range (0–4).
        """
        self.id = id  # Unique student identifier
        self.name = name  # Student's name
        self.gpa = gpa  # Student's GPA

    def display_info(self):
        """
        Display the basic information of the student: ID, name, and GPA.
        This method prints the student details in a formatted way.
        """
        print(f"Student ID: {self.id}")  # Print the student ID
        print(f"Student Name: {self.name}")  # Print the student's name
        print(f"GPA: {self.gpa:.2f}")  # Print the GPA, formatted to two decimal places

    def update_gpa(self):
        """
        Update the GPA of the student.
        Prompts the user to enter a new GPA, validates it, and updates the GPA if valid.
        """
        try:
            # Prompt the user to input a new GPA and convert it to a float
            new_gpa = float(input("Enter new GPA: "))

            # Validate the GPA (should be in the range 0–4)
            if 0 <= new_gpa <= 4:
                self.gpa = new_gpa  # Update the GPA
                print("Updated successfully")  # Inform the user of the success
            else:
                # Inform the user about invalid GPA range
                print("GPA should be between 0 and 4.")
        except ValueError:
            # Handle cases where the GPA input is invalid (e.g., non-numeric input)
            print("Invalid GPA.")

# Define a GraduateStudent class that inherits from Student
class GraduateStudent(Student):
    def __init__(self, id, name, gpa, research_topic):
        """
        Initialize a GraduateStudent object, which extends the base Student class
        with an additional research attribute.

        Parameters:
        - id (int): A unique identifier for the student.
        - name (str): The name of the student.
        - gpa (float): The student's GPA, within a valid range (0–4).
        - research_attribute (str): The research topic or field of the graduate student.
        """
        super().__init__(id, name, gpa)  # Call the parent class constructor to initialize ID, name, and GPA
        self.research_topic = research_topic  # Additional attribute for research topic

    def display_info(self):
        """
        Display the graduate student's information, including the research topic.
        Overrides the `display_info` method of the base Student class.
        """
        super().display_info()  # Call the parent class method to display basic student information
        print(f"Research Topic: {self.research_topic}")  # Display the research topic