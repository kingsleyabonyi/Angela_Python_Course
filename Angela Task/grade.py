student_scores = {
    "harry": 81,
    "Ronny": 78,
    "Drogba": 99,
    "Nnamdi": 62
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70:
        student_grades[student] = "Accepted"
    else:
        student_grades[student] = "Try again"
print(student_grades)