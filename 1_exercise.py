import numpy as np

students = np.array([
    ("Franco", 20),
    ("Linda", 21),
    ("Yuliana", 21),
    ("Jhon", 20)
], dtype=[("name", "U10"), ("age", "i4")])

for student in students:
    print("Nombre: ", student["name"], "| Type:", type(student["name"]))
    print("Edad: ", student["age"], "| Type:", type(student["age"]))
    print("------")
