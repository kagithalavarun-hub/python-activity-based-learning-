class Student:
    def __init__(self, student_id, name, aggregate_marks, subjects,
                 attendance, family_income):
        self.student_id = student_id
        self.name = name
        self.aggregate_marks = aggregate_marks
        self.subjects = subjects
        self.attendance = attendance
        self.family_income = family_income

    def is_eligible(self):
        # Eligibility Criteria
        MIN_AGGREGATE = 75
        MIN_SUBJECT_MARK = 50
        MIN_ATTENDANCE = 80
        MAX_INCOME = 300000

        # Check aggregate marks
        if self.aggregate_marks < MIN_AGGREGATE:
            return False

        # Check subject-wise minimum marks
        if any(mark < MIN_SUBJECT_MARK for mark in self.subjects.values()):
            return False

        # Check attendance
        if self.attendance < MIN_ATTENDANCE:
            return False

        # Check income
        if self.family_income > MAX_INCOME:
            return False

        return True


def allocate_scholarships(students, scholarship_slots):
    # Filter eligible students
    eligible_students = [s for s in students if s.is_eligible()]

    # Ranking and Tie Resolution
    eligible_students.sort(
        key=lambda s: (
            -s.aggregate_marks,   # Higher aggregate first
            -s.attendance,        # Higher attendance first
            s.family_income,      # Lower income first
            s.name                # Alphabetical order
        )
    )

    # Select top students
    selected_students = eligible_students[:scholarship_slots]

    return selected_students


# Sample Data
students = [
    Student(
        101,
        "Rahul",
        88,
        {"Math": 90, "Physics": 85, "Chemistry": 89},
        92,
        150000
    ),
    Student(
        102,
        "Anjali",
        91,
        {"Math": 92, "Physics": 90, "Chemistry": 91},
        95,
        250000
    ),
    Student(
        103,
        "Kiran",
        91,
        {"Math": 95, "Physics": 88, "Chemistry": 90},
        93,
        180000
    ),
    Student(
        104,
        "Sai",
        72,
        {"Math": 80, "Physics": 75, "Chemistry": 78},
        85,
        100000
    ),
    Student(
        105,
        "Priya",
        89,
        {"Math": 87, "Physics": 91, "Chemistry": 89},
        96,
        120000
    )
]

scholarship_slots = 3

selected = allocate_scholarships(students, scholarship_slots)

print("\nScholarship Recipients:")
print("-" * 50)

for rank, student in enumerate(selected, start=1):
    print(f"Rank: {rank}")
    print(f"ID: {student.student_id}")
    print(f"Name: {student.name}")
    print(f"Aggregate Marks: {student.aggregate_marks}")
    print(f"Attendance: {student.attendance}%")
    print(f"Family Income: ₹{student.family_income}")
    print("-" * 50)

