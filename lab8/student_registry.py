import json
import csv


def convert_student_to_csv(input, output): 
    with open("students.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    data_list = [
        [student["id"], student["name"], student["area"], student["year"]]
        for student in data["students"]
    ]

