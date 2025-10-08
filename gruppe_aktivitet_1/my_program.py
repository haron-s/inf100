from pathlib import Path
import json

content = Path("eksempel.json").read_text(encoding="utf-8")
data = json.loads(content)

print(data[0])
