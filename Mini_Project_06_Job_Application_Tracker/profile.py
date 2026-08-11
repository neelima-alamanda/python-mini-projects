from utils import read_json, write_json

class User:
    """
    Represents a user profile.
    """

    def __init__(self, name, skills, gpa):
        self.name = name
        self.skills = skills
        self.gpa = gpa
    def to_dict(self):
        """
        Convert the User object into a dictionary.
        """
        return {
            "name": self.name,
            "skills": self.skills,
            "gpa": self.gpa
        }
    def create_profile(self):
        """
        Save the user profile into users.json.
        Prevent duplicate profiles based on the user's name.
        """
        users = read_json("users.json")

        # Check if the user already exists
        for user in users:
            if user["name"].lower() == self.name.lower():
                print("User profile already exists.")
                return

        # Add the new user
        users.append(self.to_dict())

        # Save updated data
        write_json("users.json", users)

        print("Profile created successfully.")
    def view_profiles(self):
        """
        Display all user profiles stored in users.json.
        """
        users = read_json("users.json")

        if not users:
            print("No user profiles found.")
            return

        print("\n----- User Profiles -----")

        for user in users:
            print("-" * 30)
            print(f"Name   : {user['name']}")
            print(f"Skills : {', '.join(user['skills'])}")
            print(f"GPA    : {user['gpa']}")
    
    def update_profile(self):
        """
        Update an existing user's skills and GPA.
        """
        users = read_json("users.json")

        name = input("Enter the name of the profile to update: ")

        for user in users:
            if user["name"].lower() == name.lower():

                skills = input("Enter new skills (comma separated): ")
                user["skills"] = [skill.strip().title() for skill in skills.split(",")]

                while True:
                    try:
                        gpa = float(input("Enter new GPA: "))
                        if 0 <= gpa <= 4:
                            user["gpa"] = gpa
                            break
                        else:
                            print("GPA should be between 0 and 4.")
                    except ValueError:
                        print("Invalid GPA.")

                write_json("users.json", users)
                print("Profile updated successfully.")
                return

        print("User profile not found.")
    
    def delete_profile(self):
        """
        Delete a user profile from users.json.
        """
        users = read_json("users.json")

        name = input("Enter the name of the profile to delete: ")

        for user in users:
            if user["name"].lower() == name.lower():
                users.remove(user)
                write_json("users.json", users)
                print("Profile deleted successfully.")
                return

        print("User profile not found.")
    def get_profile(self, name):
        """
        Find and return a user profile by name.
        """
        users = read_json("users.json")

        for user in users:
            if user["name"].lower() == name.lower():
                return user

        return None