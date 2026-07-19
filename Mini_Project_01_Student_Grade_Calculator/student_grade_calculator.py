def get_student_details():
    """
    Collects the student's name, ID, and number of subjects.
    Validates inputs to ensure name and ID are not empty and subjects are positive integers.
    """
    while True:
        name = input("Enter student name: ").strip()  # Remove surrounding spaces
        if name:
            break
        print("Student name cannot be empty. Please enter a valid name.")

    while True:
        ID = input("Enter student ID: ").strip()  # Remove surrounding spaces
        if ID:
            break
        print("Student ID cannot be empty. Please enter a valid ID.")

    while True:
        try:
            subjects_count = int(input("Enter number of subjects: "))  # Convert input to integer
            if subjects_count > 0:
                break
            else:
                print("Number of subjects must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    return name, ID, subjects_count  # Return student details


def collect_subjects_and_scores(count):
    """
    Collects the names of subjects and scores for each subject.
    Ensures subject names are not empty and scores are between 0 and 100.
    """
    subject_list = []  # Stores subject names
    score_list = []  # Stores subject scores

    for subject_num in range(count):  # Loop through each subject
        while True:
            subject_name = input(f"\nEnter name for subject {subject_num + 1}: ").strip()  # Subject name input
            if subject_name:
                subject_list.append(subject_name)  # Append valid subject name
                break
            print("Subject name cannot be empty.")

        while True:
            try:
                marks = int(input(f"Enter marks for {subject_name} (0-100): "))  # Subject marks input
                if 0 <= marks <= 100:
                    score_list.append(marks)  # Append valid marks
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    return subject_list, score_list  # Return subjects and scores


def categorize_score(marks):
    """
    Returns the grade based on the marks.
    Grades are categorized as A, B, C, D, and F based on predefined ranges.
    """
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def analyze_scores(scores):
    """
    Analyzes the scores by calculating:
    - Total marks
    - Average marks
    - Highest and lowest marks
    - Count of subjects passed
    - Overall grade based on average
    - Grade distribution across all subjects
    """
    total = sum(scores)  # Calculate total marks
    avg = total / len(scores)  # Calculate average marks
    highest = max(scores)  # Find highest marks
    lowest = min(scores)  # Find lowest marks
    passing_count = sum(1 for score in scores if score >= 40)  # Count number of passing subjects
    overall_grade = categorize_score(avg)  # Categorize overall grade based on average

    # Calculate grade distribution
    grade_distribution = {
        "A": sum(1 for score in scores if score >= 90),  # Count subjects with grade A
        "B": sum(1 for score in scores if 80 <= score < 90),  # Count subjects with grade B
        "C": sum(1 for score in scores if 70 <= score < 80),  # Count subjects with grade C
        "D": sum(1 for score in scores if 40 <= score < 70),  # Count subjects with grade D
        "F": sum(1 for score in scores if score < 40)  # Count subjects with grade F
    }

    return total, avg, highest, lowest, passing_count, overall_grade, grade_distribution  # Return analysis results


def display_student_report(
    name, ID, subjects_count, subjects, scores, total, avg, highest, lowest,
    passing_count, overall_grade, grade_distribution
):
    """
    Displays a well-formatted student grade report including:
    - Basic student details
    - Subject scores and grades
    - Statistics like total, average, highest, and lowest marks
    - Grade distribution and scholarship eligibility
    - Principal's appreciation note
    """
    for i in range(5):  # Decorative pattern using a nested loop
        for j in range(i+1):
            print("*", end="")
        print()

    # Header section
    print("╔════════════════════════════════════════════════════╗")
    print("║               STUDENT GRADE REPORT                 ║")
    print("╚════════════════════════════════════════════════════╝")
    print(f"\nStudent Name      : {name}")
    print(f"Student ID        : {ID}")
    print(f"Number of Subjects: {subjects_count}\n")
    print(f"{'Subject':<20}{'Marks':<10}{'Grade':<10}{'Status'}")
    print("─" * 55)

    # Subject-wise grades and status
    for i in range(subjects_count):
        grade = categorize_score(scores[i])  # Get grade for subject
        status = "Pass" if scores[i] >= 40 else "Fail"  # Determine pass/fail status
        print(f"{subjects[i]:<20}{scores[i]:<10}{grade:<10}{status}")

    print("─" * 55)

    # Statistical analysis and summaries
    print(f"\nTotal Marks       : {total}")
    print(f"Average           : {avg:.2f}")
    print(f"Highest Marks     : {highest} ({subjects[scores.index(highest)]})")
    print(f"Lowest Marks      : {lowest} ({subjects[scores.index(lowest)]})")
    print(f"Subjects Passed   : {passing_count}")
    print(f"Overall Grade     : {overall_grade}")

    # Scholarship eligibility based on average marks
    if avg >= 85:
        print("🎓 Scholarship Status : Eligible")
    else:
        print("🎓 Scholarship Status : Not Eligible")

    # Grade distribution display for all subjects
    print("\nGrade Distribution:")
    for grade, count in grade_distribution.items():
        print(f"{grade:<5} : {count}")

    # Principal's appreciation note based on overall grade
    print("\nAppreciation Note:")
    if overall_grade == "A":
        print("Principal's Note: Exceptional performance! Keep it up!")
    elif overall_grade == "B":
        print("Principal's Note: Great effort! You're doing well!")
    elif overall_grade == "C":
        print("Principal's Note: Good progress! Stay motivated!")
    elif overall_grade == "D":
        print("Principal's Note: You've passed! Keep improving!")
    else:
        print("Principal's Note: Don't give up! You can do better!")

    print("\nEnd of Report")
    print("═" * 55)


def main():
    """
    Main program flow:
    - Collect student details
    - Collect subject names and scores
    - Analyze scores
    - Display the formatted grade report
    - Optionally allow processing for another student
    """
    print("=" * 60)
    print(f"{'🎓 WELCOME TO STUDENT GRADE CALCULATOR 🎓':^60}")
    print("=" * 60)

    while True:
        print("\n💻 Collecting student details...")
        name, ID, subject_count = get_student_details()

        print("\n📘 Collecting subject names and scores...")
        subjects, scores = collect_subjects_and_scores(subject_count)

        total_marks, average_marks, highest_marks, lowest_marks, pass_count, grade, grade_distribution = analyze_scores(
            scores
        )
        display_student_report(
            name,
            ID,
            subject_count,
            subjects,
            scores,
            total_marks,
            average_marks,
            highest_marks,
            lowest_marks,
            pass_count,
            grade,
            grade_distribution
        )
        choice = input("\nWould you like to add another student? (yes/no): ").strip().lower()
        if choice != "yes":
            print("\nThank you for using the Student Grade Calculator!")
            break


if __name__ == "__main__":
    main()