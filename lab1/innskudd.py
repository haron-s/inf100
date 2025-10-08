from pathlib import Path
import json

content = Path('bankdata.json').read_text(encoding='utf-8')
data = json.loads(content)

name = data['personalia']['navn']
value = data['konti'][0]['saldo']

sparekonto_saldo = data['konti'][1]['saldo']
total = value + sparekonto_saldo

print(f"{name} har {total} kroner i innskudd")