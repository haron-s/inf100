import json
import csv


def convert_students_to_csv(input, output): 
    with open(input, "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)

    # 
    headers = list(data["students"][0].keys())
    data = [
        [student["id"], student["name"], student["area"], student["year"]]
        for student in data["students"]
    ]

    with open(output, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(headers)
        writer.writerows(data)

if __name__ == "__main__":
    convert_students_to_csv("students.json", "students.csv")
    convert_students_to_csv("students2.json", "students2.csv")
