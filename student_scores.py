
students = [
    {"name": "A", "marks": [50, 60, 70]},
    {"name": "B", "marks": [30, 40]},
    {"name": "C", "marks": [80, 90]}
]

total_updated_marks = 0

for student in students:
    marks = student["marks"]
    average = sum(marks) / len(marks)

    if average >= 60:
        for mark in marks:
            total_updated_marks += mark + 5  # Add 5 grace marks

print("Total Updated Marks:", total_updated_marks)