import csv

with open("records.csv", "r", newline="", encoding="utf-8") as input:
    reader = csv.reader(input, delimiter=",")
    table = list(reader)
        
data = table[1:]

headers = ["label", "total_duration"]
new_data = [
    [data[i][2], round(float(data[i][1]) - float(data[i][0]))]
    for i in range(len(data))
    ]

with open("durations.csv", "w", newline="", encoding="utf-8") as output:
    writer = csv.writer(output, delimiter=",", lineterminator="\n")
    
    writer.writerow(headers)
    writer.writerows(new_data)

for i in range(len()):
    data[i] - data[i]