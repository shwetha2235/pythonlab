"""This task builds flexible modular functions using variable-length positional (*args) and keyword arguments
(**kwargs) to compute dynamic class performance scores. The program receives varying sets of assessment
grades, calculates min, max, average, and letter score distributions, and returns multiple structured metrics via
tuple unpacking."""
def calculate_statistics(*marks, **details):
    if not marks:
        raise ValueError("At least one mark is required.")

    if any(not isinstance(m, (int, float)) or isinstance(m, bool)
           or not 0 <= m <= 100 for m in marks):
        raise ValueError("Marks must be between 0 and 100.")

    minimum = min(marks)
    maximum = max(marks)
    average = sum(marks) / len(marks)

    distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for mark in marks:
        if mark >= 90:
            distribution["A"] += 1
        elif mark >= 80:
            distribution["B"] += 1
        elif mark >= 70:
            distribution["C"] += 1
        elif mark >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    return minimum, maximum, average, distribution, details
# Function call using *args and **kwargs
result = calculate_statistics(
    95, 82, 76, 65, 48, 90,
    name="Class A",
    subject="Python Programming",
    semester=3
)
# Tuple unpacking
minimum, maximum, average, distribution, details = result
print("STUDENT GRADE AND STATISTICS REPORT")
print("-----------------------------------")
print("Class Name:", details["name"])
print("Subject:", details["subject"])
print("Semester:", details["semester"])
print("Minimum Marks:", minimum)
print("Maximum Marks:", maximum)
print("Average Marks:", round(average, 2))
print("\nGrade Distribution:")
for grade, count in distribution.items():
    print(f"Grade {grade}: {count} student(s)")
