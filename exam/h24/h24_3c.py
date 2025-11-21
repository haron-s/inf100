import csv

with open("candidate_numbers.csv", "r", newline="", encoding="utf-8") as input:
    reader = csv.reader(input, delimiter=";")
    candidate_numbers = dict(reader)

with open("student_overview.csv", "r", newline="", encoding="utf-8") as input:
    reader = csv.reader(input, delimiter=";")
    student_overview = list(reader)

    student_header = student_overview[0]
    student_data = student_overview[1:]

with open("exam_scores.csv", "r", newline="", encoding="utf-8") as input:
    reader = csv.reader(input, delimiter=";")
    exam_scores = dict(reader)

student_header.append("exam_score")
for candidate in candidate_numbers:
    name = candidate_numbers[candidate]
    score = exam_scores[candidate]

    for row in student_overview:
        if row[0] == name:
            row.append(score)

with open("student_overview_with_exam_scores.csv", "w", newline="", encoding="utf-8") as output:
    writer = csv.writer(output, delimiter=",", lineterminator="\n")
    
    writer.writerow(student_header)
    writer.writerows(student_data)