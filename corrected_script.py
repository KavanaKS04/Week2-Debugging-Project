
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def main():
    student_name = input("Enter student name: ").strip()

    if not student_name:
        print("Error: Student name cannot be empty.")
        return

    try:
        marks_input = input(
            "Enter marks separated by spaces: "
        ).split()

        if not marks_input:
            print("Error: Please enter at least one mark.")
            return

        marks = [float(mark) for mark in marks_input]

        if any(mark < 0 or mark > 100 for mark in marks):
            print("Error: Marks must be between 0 and 100.")
            return

        average = calculate_average(marks)
        grade = get_grade(average)

        print("\nStudent Name:", student_name)
        print("Average Marks:", round(average, 2))
        print("Grade:", grade)

    except ValueError:
        print("Error: Please enter valid numeric marks.")


if __name__ == "__main__":
    main()
