import csv

def count_facilities_by_species(path):
    with open(path, "r", encoding="latin1", newline="") as csvfile:
        data = list(csv.reader(csvfile, delimiter=";"))
    
    species_sum = {}
    for row in data[2:]:
        species = row[12]
        try:
            species_sum[species] += 1
        except KeyError:
            species_sum[species] = 1

    for key in sorted(species_sum):
        print(f'{key}: {species_sum[key]}')
    
if __name__ == '__main__':
    count_facilities_by_species('Akvakulturregisteret.csv')
