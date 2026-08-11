# Import the relevant modules for handling user profiles, job postings, and applications.
from profile import User
from utils import read_json
from job import Job
from application import Application

def display_menu():
    """
    Display the main menu of the Job Application Tracker.
    Provides users with a list of options to interact with the system.
    """
    print("\n========== Job Application Tracker ==========")
    print("1. Create User Profile")
    print("2. View User Profiles")
    print("3. Update User Profile")
    print("4. Delete User Profile")
    print("5. Add Job")
    print("6. View Jobs")
    print("7. Update Job")
    print("8. Delete Job")
    print("9. Apply for Job")
    print("10. View Applications")
    print("11. Recommend Jobs for User")
    print("12. Exit")

# Infinite loop to continuously display the menu and handle user input.
while True:
    # Call the function to display the main menu.
    display_menu()

    # Try to capture the user's choice and handle invalid inputs.
    try:
        choice = int(input("\nEnter your choice: "))  # Convert the input to an integer.
    except ValueError:
        # If conversion fails, notify the user and prompt again.
        print("Please enter a valid number.")
        continue

    # Handle each menu option based on the user's choice.
    if choice == 1:
        # Option 1: Create a new user profile.
        name = input("Enter name: ")  # Capture the user's name.

        # Capture the user's skills as a comma-separated string and process into a list.
        skills = input("Enter skills (comma separated): ")
        skills = [skill.strip() for skill in skills.split(",")]  # Strip extra spaces.

        # Prompt the user for their GPA, validate input within the range [0, 4].
        while True:
            try:
                gpa = float(input("Enter GPA: "))  # Convert GPA to a float.
                if 0 <= gpa <= 4:  # GPA should be in a valid range.
                    break
                print("GPA should be between 0 and 4.")  # Notify for invalid range.
            except ValueError:
                print("Invalid GPA.")  # Notify for non-numeric input.

        # Create a User object and call the `create_profile` method to save the data.
        user = User(name, skills, gpa)
        user.create_profile()

    elif choice == 2:
        # Option 2: View all user profiles.
        user = User("", [], 0)  # Create a temporary User object.
        user.view_profiles()  # Call the method to display all profiles.

    elif choice == 3:
        # Option 3: Update an existing user profile.
        user = User("", [], 0)  # Create a temporary User object.
        user.update_profile()  # Call the method to update a user's profile.

    elif choice == 4:
        # Option 4: Delete an existing user profile.
        user = User("", [], 0)  # Create a temporary User object.
        user.delete_profile()  # Call the method to delete a user's profile.

    elif choice == 5:
        # Option 5: Add a new job posting.
        while True:
            try:
                job_id = int(input("Enter Job ID: "))  # Capture a unique job ID as an integer.
                break
            except ValueError:
                print("Invalid Job ID.")  # Notify for non-numeric input.

        title = input("Enter Job Title: ")  # Capture the job's title.

        # Capture job's required skills as a comma-separated string and process into a list.
        skills = input("Enter Required Skills (comma separated): ")
        skills = [skill.strip() for skill in skills.split(",")]  # Strip extra spaces.

        # Prompt for the minimum GPA required for the job, validate input within range [0, 4].
        while True:
            try:
                min_gpa = float(input("Enter Minimum GPA: "))
                if 0 <= min_gpa <= 4:
                    break
                print("GPA should be between 0 and 4.")
            except ValueError:
                print("Invalid GPA.")

        # Create a Job object and call the `create_job` method to save the job.
        job = Job(job_id, title, skills, min_gpa)
        job.create_job()

    elif choice == 6:
        # Option 6: View all job postings.
        job = Job(0, "", [], 0)  # Create a temporary Job object.
        job.view_jobs()  # Call the method to display all job postings.

    elif choice == 7:
        # Option 7: Update an existing job posting.
        job = Job(0, "", [], 0)  # Create a temporary Job object.
        job.update_job()  # Call the method to update job details.

    elif choice == 8:
        # Option 8: Delete a job posting.
        job = Job(0, "", [], 0)  # Create a temporary Job object.
        job.delete_job()  # Call the method to delete a job posting.

    elif choice == 9:
        # Option 9: Apply for a job.
        name = input("Enter User Name: ")  # Capture the user's name.

        # Prompt for the job ID the user wants to apply for.
        while True:
            try:
                job_id = int(input("Enter Job ID: "))
                break
            except ValueError:
                print("Invalid Job ID.")  # Notify for non-numeric input.

        # Create an Application object and call the method to apply for the selected job.
        application = Application(name, job_id)
        application.apply_for_job()

    elif choice == 10:
        # Option 10: View all submitted applications.
        application = Application("", 0)  # Create a temporary Application object.
        application.view_applications()  # Call the method to display all applications.

    elif choice == 11:
        # Option 11: Recommend jobs based on the user's skills.
        name = input("Enter User Name: ")

        user_manager = User("", [], 0)
        user = user_manager.get_profile(name)

        if user is None:
            print("User profile not found.")
        else:
            job = Job(0, "", [], 0)

            recommendations = job.recommend_jobs(user["skills"])

            if not recommendations:
                print("No matching jobs found.")
            else:
                print("\n----- Recommended Jobs -----")

                for recommendation in recommendations:
                    print("-" * 35)
                    print(f"Job ID          : {recommendation['job_id']}")
                    print(f"Title           : {recommendation['title']}")
                    print(
                        f"Matching Skills : "
                        f"{', '.join(recommendation['matching_skills'])}"
                    )
                    print(f"Minimum GPA     : {recommendation['min_gpa']}")
    elif choice == 12:
        # Option 12: Exit the application.
        print("Thank you for using Job Application Tracker!")
        break
    else:
        # Handle invalid menu option selections.
        print("Invalid choice. Please try again.")