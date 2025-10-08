from pathlib import Path
import json

content = Path("standings.json").read_text(encoding="utf-8")
data = json.loads(content)

print(data["league"]["name"])
print(data["league"]["created"])
print(data["standings"]["results"][17]["entry_name"])

for i in data:
    if data["standings"]["results"][] == 
