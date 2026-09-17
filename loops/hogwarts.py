# students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)


# DICTIONARIES
students = [
    {"name": "Hermione", "Sex": "F", "race": "W"},
    {"name": "Julia", "Sex": "F", "race": "A"},
    {"name": "Renan", "Sex": "M", "race": "W"},
    {"name": "Bruno", "Sex": "M", "race": "B"}
]
for student in students:
    print(student["name"], student["Sex"])