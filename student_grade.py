"""student_grade.py - Student Grade Calculator (console based)."""

PASS_MARK = 40            # minimum marks needed in every subject


def average(marks):
    """Return the average of a list of marks."""
    if not marks:
        raise ValueError("Marks list cannot be empty")
    return sum(marks) / len(marks)


def grade(avg):
    """Convert an average mark (0-100) into a letter grade."""
    if avg < 0 or avg > 100:
        raise ValueError("Average must be between 0 and 100")
    if avg >= 90:
        return "A"
    if avg >= 75:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= PASS_MARK:
        return "D"
    return "F"


def is_pass(marks):
    """Return True if the student scored at least PASS_MARK in every subject."""
    return len(marks) > 0 and all(m >= PASS_MARK for m in marks)


def main():
    students = {
        "Asha": [92, 88, 95],
        "Ravi": [70, 65, 80],
        "Meena": [35, 40, 30],
    }
    print("=== Student Grade Calculator ===")
    for name, marks in students.items():
        avg = average(marks)
        result = "PASS" if is_pass(marks) else "FAIL"
        print(f"{name:<8} Average: {avg:6.2f}  Grade: {grade(avg)}  "
              f"Result: {result}")


if __name__ == "__main__":
    main()
