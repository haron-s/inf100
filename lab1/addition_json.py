from pathlib import Path
import json


with open('addisjon.json') as file:
    tall = json.load(file)

sum = tall['tall1'] + tall['tall2']
print(f'Summen av tallene er {sum}')