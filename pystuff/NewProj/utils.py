students = [
    { "name": "Harry", "house": "Gryffindor" },
    { "name": "Cho", "house": "Ravenclaw"},
    { "name": "Draco", "house": "Slytherin"}
]

students.sort(key=lambda person: person["house"])

print(students)

