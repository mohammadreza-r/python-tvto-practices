# Sample data - list of dictionaries
students_data = [
    {"name": "Ali", "scores": [18, 19, 17, 20, 18]},
    {"name": "Maryam", "scores": [16, 15, 17, 18, 16]},
    {"name": "Reza", "scores": [20, 19, 20, 18, 19]},
    {"name": "Sara", "scores": [14, 15, 13, 16, 15]},
    {"name": "Mohammad", "scores": [17, 18, 16, 17, 19]}
]


def calculate_average(scores):
    """Calculate the average of a list of scores"""
    if not scores:
        return 0
    return sum(scores) / len(scores)


def analyze_students(students):
    """Analyze student score data"""

    print("=" * 50)
    print("📊 Student Score Analysis")
    print("=" * 50)

    # Part A: Display each student's average
    print("\nA) Each student's average score:")
    print("-" * 40)

    averages = {}
    for student in students:
        name = student["name"]
        avg = calculate_average(student["scores"])
        averages[name] = avg
        print(f"  {name}: {avg:.2f}")

    # Part B: Dictionary of name and average
    print("\nB) Dictionary of names and averages:")
    print("-" * 40)
    print(averages)

    # Part C: Student with highest average
    print("\nC) Student with the highest average:")
    print("-" * 40)

    if averages:
        top_student = max(averages, key=averages.get)
        top_average = averages[top_student]
        print(f"  🏆 {top_student} with average {top_average:.2f}")

    print("\n" + "=" * 50)

    return averages


# Run the program
averages_dict = analyze_students(students_data)

# Option to add a new student
print("\nWould you like to add a new student?")
add_new = input("Yes/No: ").strip().lower()

if add_new in ['yes', 'y']:
    name = input("Student name: ")
    scores_input = input("Enter scores separated by commas (e.g., 18, 19, 17): ")
    scores = [float(s.strip()) for s in scores_input.split(',') if s.strip()]

    new_student = {"name": name, "scores": scores}
    students_data.append(new_student)

    print("\nUpdated information:")
    analyze_students(students_data)