student_info = {
    "name" : "Linda F.",
    "age" : 21,
    "career" : "Bachelors in Modern Languages",
    "is_active" : True
}

for key, value in student_info.items():
    print(f"{key}: {value} | Type: {type(value)}")