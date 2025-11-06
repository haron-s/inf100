from matplotlib import pyplot as plt
import csv

with open("Akvakulturregisteret.csv", "r", encoding="latin1", newline="") as csvfile:
    data = list(csv.reader(csvfile, delimiter=";"))
    
x_values_land = [float(row[24]) for row in data[2:] if row[19] == "LAND"]
y_values_land = [float(row[23]) for row in data[2:] if row[19] == "LAND"]
    
x_values_sea = [float(row[24]) for row in data[2:] if row[19] != "LAND"]
y_values_sea = [float(row[23]) for row in data[2:] if row[19] != "LAND"]

plt.scatter(x_values_land, y_values_land, color="blue", alpha=.1, s=8)
plt.scatter(x_values_sea, y_values_sea, color="orange", alpha=.1, s=8)
plt.show()