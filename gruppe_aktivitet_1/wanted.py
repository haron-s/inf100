from pathlib import Path
import json

content = Path("wanted.json").read_text(encoding="utf-8")
data = json.loads(content)

print(f'Total number of entries: {data["total"]}')

print(data["items"][5]["title"])
print(data["items"][5]["subjects"])
print(data["items"][5]["race_raw"])
print(data["items"][5]["languages"])
print(data["items"][5]["reward_text"])