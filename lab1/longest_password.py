from pathlib import Path
import json

content = Path('passwords.json').read_text(encoding='utf-8')
data = json.loads(content)

password1 = data['people'][0]['password']
password2 = data['people'][1]['password']
password3 = data['people'][2]['password']

print(max(len(password1),len(password2),len(password3)))