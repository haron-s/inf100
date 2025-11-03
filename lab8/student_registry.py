import json
import csv


#def convert_student_to_csv(input, output): 
with open("students.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data_list = [
    [id, name, area, year]
    for person in data["students"]
    for id, name, area, year in person.get()
]

print(data_list)
