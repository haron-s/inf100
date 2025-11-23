months_of_temps = [
    [-3.0, 2.1, -1.1, -4.5],
    [4.8, 2.9, -1.3, 5.0, 6.1],
    [10.0, 12.0]
]

def average_temp_verbose(months_of_temps):
    total_sum = 0
    total_len = 0
    for month in months_of_temps:
        total_sum += sum(day for day in month)
        total_len += len(month)

    return total_sum / total_len

def average_temp(months_of_temps):
    total_sum = sum(day for month in months_of_temps for day in month)
    total_len = sum(len(month) for month in months_of_temps)

    return total_sum / total_len

print(average_temp_verbose(months_of_temps))
print(average_temp(months_of_temps))
