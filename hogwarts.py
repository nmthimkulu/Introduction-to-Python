"""
students = ["Hermione", "Harry", "Ron", "Draco"]
house = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
"""

"""
for student in students:
    print(student)
"""

"""
for i in range(len(students)):
    print(i + i, students[i])
"""  

students = [
    {"name": "Hermione","house": "Gryffindor", "patronus": "Otter"},
    {"name":"Harry", "house": "Gryffindor","patronus": "Stag" },
    {"name": "Ron", "house": "Gryfindor", "patronus": "Jack Rusell terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus": None }
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")