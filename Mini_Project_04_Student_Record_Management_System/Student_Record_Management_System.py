# Function to add a new student to the records file
def add_student():
    # Prompt the user to enter the student's name and validate the input
    while True:
        name = input("Enter the student's name:").strip()  # Removes unnecessary leading and trailing whitespace
        if name:  # Ensure the name is not empty
            break
        else:
            print("Name cannot be empty")  # Display an error if the name is left blank

    # Prompt the user to enter the student's age and ensure it is a positive integer
    while True:
        try:
            age = int(input("Enter student's age:"))
            if age > 0:  # Age must be a positive number
                break
            else:
                print("Age should be a positive number")
        except ValueError:  # Handle invalid input (e.g., non-integer values)
            print("It must be an integer")

    # Prompt the user to enter the student's GPA and ensure it is within the valid range [0, 4]
    while True:
        try:
            GPA = float(input("Enter a student GPA value:"))
            if 0 <= GPA <= 4:  # GPA must be between 0 and 4 (inclusive)
                break
            else:
                print("GPA must be between 0 and 4.")
        except ValueError:  # Handle invalid input (e.g., non-numerical values)
            print("Please enter a valid GPA.")

    # Write the student's data into the file
    try:
        with open("students.txt", "a") as file:
            file.write(f"{name},{age},{GPA}\n")  # Format: name,age,GPA
        print("Student details saved successfully!")  # Confirmation message for successful save
    except IOError:  # Handle errors that might occur while working with the file
        print("Error writing to file.")

# Function to display all student records stored in the file
def display_students():
    try:
        # Open the file for reading
        with open("students.txt", 'r') as file:
            contents = file.readlines()  # Read all lines into a list
            if contents == []:  # Check if the file is empty
                print("No Records found")  # Inform the user if the file has no data
                return  # Exit the function early
        
        # Print the header for student records
        print("\nStudent Records")
        print("-" * 30)  # Add a separator for visual clarity

        # Iterate through each line in the file and process the records
        for line in contents:
            line = line.strip()  # Remove extra whitespace/newline from the line
            valid = line.split(",")  # Split the line by commas to extract individual fields

            # Ensure the line contains exactly 3 fields: name, age, GPA
            if len(valid) != 3:
                print("Invalid data format")  # Notify if the record format is incorrect
                continue  # Skip this line and move to the next

            name, age, gpa = valid
            try:
                age = int(age)  # Convert age to an integer
                gpa = float(gpa)  # Convert GPA to a floating-point number
            except ValueError:  # Handle invalid numeric values
                print("Invalid data format")  # Notify if numeric conversion fails
                continue  # Skip this record and continue to the next

            # Display the record in a formatted manner
            print(f"{'Name':<10}: {name}")
            print(f"{'Age':<10}: {age}")
            print(f"{'GPA':<10}: {gpa:.2f}")  # GPA displayed with two decimal places
            print("-" * 30)  # Separator between records
    except FileNotFoundError:  # Handle case where the file doesn't exist
        print("File not found")  # Notify the user that the file is missing

# Main function to display the menu and handle user choices
def main():
    # Display program title and formatting
    print("=" * 50)
    print("STUDENT RECORD MANAGEMENT")
    print("=" * 50)
    
    # Use an infinite loop to keep showing the menu until the user exits
    while True:
        # Display menu options
        print("\n========== MENU ==========")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        print("=" * 25)

        # Prompt the user for a choice and validate the input
        while True:
            try:
                choice = int(input("Enter your choice: "))  # User input for menu choice
                if 1 <= choice <= 3:  # Ensure the choice is between 1 and 3
                    break  # Exit loop if valid choice
                else:
                    print("Please enter a number between 1 and 3.")  # Notify invalid range
            except ValueError:  # Handle non-integer input
                print("Please enter a valid number.")

        # Execute the corresponding function based on the choice
        if choice == 1:
            add_student()  # Call function to add a new student
        elif choice == 2:
            display_students()  # Call function to display all students
        elif choice == 3:
            print("\nExiting Student Record Management System...")  # Notify the user about exiting
            break  # Exit the menu loop to end the program
        else:
            # This block won't be reached due to the validation above; kept for completeness
            print("Invalid choice. Please try again.")

# Entry point of the program; ensures main() runs only when the script is executed directly
if __name__ == "__main__":
    main()