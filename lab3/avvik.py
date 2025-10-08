from pathlib import Path
import json

def load_emission_data(filename):
    content = filename
    data = Path(content).read_text(encoding='utf-8')
    emission_data = json.loads(data)
    return emission_data

def get_deviations(data):
    emissions = data
    deviations_list = []
    for i in emissions["data"]:
        actual = i["intensity"]["actual"]
        forecast =i["intensity"]["forecast"]
        
        if actual is not None and forecast is not None:
            deviation = actual - forecast
            deviations_list.append(abs(deviation))
    return deviations_list

def count_values_larger_than(values, threshold):
    count = 0
    for i in values:
        if i > threshold:
            count += 1
    return count

def main():
    filename = input()
    threshold = int(input())

    data = load_emission_data(filename)
    deviastions_list = get_deviations(data)
    count = count_values_larger_than(deviastions_list,threshold)

    print(f"Antall avvik større enn {threshold}: {count}")

if __name__ == "__main__":
    main()