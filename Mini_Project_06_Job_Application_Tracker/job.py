from utils import read_json, write_json

class Job:
    """
    Represents a job listing.

    This class provides methods to handle job-related operations, 
    including creating, viewing, updating, and deleting job listings.
    """

    def __init__(self, job_id, title, required_skills, min_gpa):
        """
        Initialize a Job object with the required details.

        Attributes:
        - job_id (int): Unique identifier for the job.
        - title (str): Title or name of the job.
        - required_skills (list): List of skills required for the job.
        - min_gpa (float): Minimum GPA required for the job.
        """
        self.job_id = job_id
        self.title = title
        self.required_skills = required_skills
        self.min_gpa = min_gpa

    def to_dict(self):
        """
        Convert the `Job` object into a dictionary format suitable for storage.

        Returns:
        - dict: A dictionary representation of the Job object.
        """
        return {
            "job_id": self.job_id,
            "title": self.title,
            "required_skills": self.required_skills,
            "min_gpa": self.min_gpa
        }
    
    def create_job(self):
        """
        Save the job details into jobs.json.
        Prevents duplicate job entries based on job ID.

        Steps:
        1. Read the existing jobs from `jobs.json`.
        2. Check if a job with the same `job_id` already exists.
        3. If no duplicate is found, add the new job to the list.
        4. Save the updated jobs back to the JSON file.
        5. Notify the user whether the operation was successful or not.
        """
        # Load existing jobs from jobs.json
        jobs = read_json("jobs.json")

        # Check for duplicate job ID
        for job in jobs:
            if job["job_id"] == self.job_id:
                print("Job already exists.")  # Notify if the job ID is already present
                return

        # Add the new job to the list
        jobs.append(self.to_dict())

        # Save back to the JSON file
        write_json("jobs.json", jobs)

        print("Job created successfully.")  # Notify user of successful creation

    def view_jobs(self):
        """
        Display all job listings stored in jobs.json.

        Steps:
        1. Read all jobs from the `jobs.json` file.
        2. If no jobs are available, notify the user.
        3. Otherwise, display each job's details in a formatted way.
        """
        # Load the list of jobs from jobs.json
        jobs = read_json("jobs.json")

        # Check if there are no jobs in the database
        if not jobs:
            print("No job listings found.")  # Notify if the database is empty
            return

        # Display each job's details in a formatted way
        print("\n----- Job Listings -----")
        for job in jobs:
            print("-" * 35)
            print(f"Job ID          : {job['job_id']}")  # Display job ID
            print(f"Title           : {job['title']}")  # Display job title
            print(f"Required Skills : {', '.join(job['required_skills'])}")  # Display skills as a comma-separated list
            print(f"Minimum GPA     : {job['min_gpa']}")  # Display minimum GPA required

    def recommend_jobs(self, user_skills, jobs=None, index=0, recommendations=None):
        """
        Recursively recommend jobs based on partial skill matching.
        """

        if recommendations is None:
            recommendations = []

        if jobs is None:
            jobs = read_json("jobs.json")

        # Base case: all jobs have been checked
        if index >= len(jobs):
            return recommendations

        job = jobs[index]

        # Find matching skills
        matching_skills = []

        for skill in job["required_skills"]:
            if skill.lower() in [s.lower() for s in user_skills]:
                matching_skills.append(skill)

        # Recommend job if at least one skill matches
        if matching_skills:
            recommendations.append({
                "job_id": job["job_id"],
                "title": job["title"],
                "matching_skills": matching_skills,
                "min_gpa": job["min_gpa"]
            })

        # Recursive call for the next job
        return self.recommend_jobs(
            user_skills,
            jobs,
            index + 1,
            recommendations
        )
    def update_job(self):
        """
        Update an existing job listing in jobs.json.

        Steps:
        1. Read the existing jobs from `jobs.json`.
        2. Prompt the user for the `job_id` of the job they want to update.
        3. Validate the input and check if the job exists.
        4. If found, allow the user to modify job attributes:
            - Title
            - Required skills
            - Minimum GPA
        5. Save the updated jobs back to `jobs.json`.
        6. Notify the user whether the operation was successful or not.
        """
        # Load existing jobs from jobs.json
        jobs = read_json("jobs.json")

        # Prompt the user to enter the Job ID to update
        while True:
            try:
                job_id = int(input("Enter the Job ID to update: "))  # Validate input as integer
                break
            except ValueError:
                print("Invalid Job ID. Please enter a number.")  # Handle invalid input

        # Search for the job and update its details
        for job in jobs:
            if job["job_id"] == job_id:
                # Update job attributes
                title = input("Enter new job title: ")
                job["title"] = title

                skills = input("Enter required skills (comma separated): ")
                job["required_skills"] = [skill.strip().title() for skill in skills.split(",")]  # Normalize skill names

                # Validate GPA input
                while True:
                    try:
                        min_gpa = float(input("Enter minimum GPA: "))
                        if 0 <= min_gpa <= 4:
                            job["min_gpa"] = min_gpa  # Update the minimum GPA
                            break
                        else:
                            print("GPA should be between 0 and 4.")  # Notify if GPA is out of range
                    except ValueError:
                        print("Invalid GPA.")  # Handle invalid input

                # Save updated jobs back to JSON file
                write_json("jobs.json", jobs)
                print("Job updated successfully.")  # Notify success
                return

        print("Job not found.")  # Notify if the given Job ID does not exist

    def delete_job(self):
        """
        Delete a job listing from jobs.json.

        Steps:
        1. Read the existing jobs from `jobs.json`.
        2. Prompt the user for the `job_id` of the job they want to delete.
        3. Validate the input and check if the job exists.
        4. If found, remove the job from the list.
        5. Save the updated jobs back to `jobs.json`.
        6. Notify the user whether the operation was successful or not.
        """
        # Load existing jobs from jobs.json
        jobs = read_json("jobs.json")

        # Prompt the user to enter the Job ID to delete
        while True:
            try:
                job_id = int(input("Enter the Job ID to delete: "))  # Validate input as integer
                break
            except ValueError:
                print("Invalid Job ID. Please enter a number.")  # Handle invalid input

        # Search for the job to delete
        for job in jobs:
            if job["job_id"] == job_id:
                # Remove the job from the list
                jobs.remove(job)
                write_json("jobs.json", jobs)  # Save updated jobs back to JSON file
                print("Job deleted successfully.")  # Notify success
                return

        print("Job not found.")  # Notify if the given Job ID does not exist