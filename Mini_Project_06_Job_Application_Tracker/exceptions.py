# Custom exception raised when a user's GPA is below the minimum
# GPA required for a job application.
class InsufficientGPAError(Exception):
    """Raised when the user's GPA does not meet the job requirement."""
    pass


# Custom exception raised when a user does not have the
# required skills for a job application.
class MissingSkillsError(Exception):
    """Raised when the user lacks one or more required skills."""
    pass