from pathlib import Path
import json

farger = Path('farger.json').read_text(encoding='utf-8')
data = json.loads(farger)

red1 = data['colA'] // 1000000
green1 = data['colA'] // 1000 % 1000
blue1 = data['colA']  % 1000

red2 = data['colB'] // 1000000
green2 = data['colB'] // 1000 % 1000
blue2 = data['colB'] % 1000

ratioB = data['rationB']

new_red = round(red1 * (1 - ratioB) + red2 * ratioB)
new_green = round(green1 * (1 - ratioB) + green2 * ratioB)
new_blue = round(blue1 * (1 - ratioB) + blue2 * ratioB)

new_color = new_red * 1000000 + new_green * 1000 + new_blue

print(new_color)