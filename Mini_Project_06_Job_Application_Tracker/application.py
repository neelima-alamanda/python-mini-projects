from utils import read_json, write_json
from exceptions import InsufficientGPAError, MissingSkillsError
from datetime import datetime

class Application:
    """
    Represents a job application.
    This class handles the logic related to submitting and viewing job applications.
    """

    def __init__(self, user_name, job_id):
        """
        Initialize an Application object with user name, job ID, and the current application date and time.

        Attributes:
        - user_name (str): The name of the user applying for the job.
        - job_id (int): The ID of the job the user is applying for.
        - application_date (str): The timestamp when the application is created.
        """
        self.user_name = user_name
        self.job_id = job_id
        self.application_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current timestamp in readable format

    def to_dict(self):
        """
        Convert the `Application` object into a dictionary format suitable for storage.

        Returns:
        - dict: A dictionary representation of the application, which includes the user name, job ID, and application date.
        """
        return {
            "user_name": self.user_name,
            "job_id": self.job_id,
            "application_date": self.application_date
        }

    def apply_for_job(self):
        """
        Apply for a job after verifying eligibility based on GPA and required skills.

        The method performs the following steps:
        - Reads user profiles, job postings, and existing applications from JSON files.
        - Finds the user and job based on the provided user name and job ID.
        - Validates the application by:
          - Checking if the user's GPA meets the job's minimum GPA.
          - Checking if the user has the required skills for the job.
        - If the application is valid, it appends the application to `applications.json`.
        - If not, raises custom exceptions (InsufficientGPAError, MissingSkillsError) and handles them.
        """
        # Load user profiles, job postings, and existing applications
        users = read_json("users.json")  # Read all user profiles from `users.json`
        jobs = read_json("jobs.json")  # Read all job listings from `jobs.json`
        applications = read_json("applications.json")  # Read existing applications from `applications.json`

        # Step 1: Find the user by the provided name
        user = None
        for u in users:
            if u["name"].lower() == self.user_name.lower():  # Case-insensitive match
                user = u
                break  # Exit loop once the user is found

        if user is None:
            # If the user is not found, print a message and exit
            print("User not found.")
            return

        # Step 2: Find the job by the provided job ID
        job = None
        for j in jobs:
            if j["job_id"] == self.job_id:
                job = j
                break  # Exit loop once the job is found

        if job is None:
            # If the job is not found, print a message and exit
            print("Job not found.")
            return

        try:
            # Step 3: Validate the user's GPA
            if user["gpa"] < job["min_gpa"]:
                # Raise an exception if the user's GPA does not meet the job's minimum requirement
                raise InsufficientGPAError(
                    "User does not meet the minimum GPA requirement."
                )

            # Step 4: Check if the user possesses all required skills for the job
            missing_skills = []  # List to track skills that the user is missing

            for skill in job["required_skills"]:
                # Check if each required skill is found in the user's skills
                if skill.lower() not in [s.lower() for s in user["skills"]]:
                    missing_skills.append(skill)

            if missing_skills:
                # Raise an exception if the user lacks any required skills
                raise MissingSkillsError(
                    f"Missing required skills: {', '.join(missing_skills)}"
                )

            # Step 5: If all validations pass, save the application
            applications.append(self.to_dict())  # Append the application as a dictionary
            write_json("applications.json", applications)  # Save updated applications to `applications.json`

            print("Application submitted successfully.")  # Success message

        except (InsufficientGPAError, MissingSkillsError) as e:
            # Handle custom exceptions and display the error message to the user
            print(e)

    def view_applications(self):
        """
        Display all submitted job applications.

        Reads the `applications.json` file and prints the details of all recorded applications.
        If no applications exist, prints a message indicating that no applications were found.
        """
        applications = read_json("applications.json")  # Load submitted applications from `applications.json`

        if not applications:
            # If no applications are found, print a message and return
            print("No applications found.")
            return

        # Loop through all applications and print their details in a formatted way
        print("\n----- Job Applications -----")
        for application in applications:
            print("-" * 40)  # Separator line for better formatting
            print(f"User Name        : {application['user_name']}")  # Display user name
            print(f"Job ID           : {application['job_id']}")  # Display job ID
            print(f"Application Date : {application['application_date']}")  # Display application submission date