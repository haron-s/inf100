from pathlib import Path
import json

content = Path("joker.json").read_text(encoding="utf-8")
data = json.loads(content)

def joker_bot(grunntall):
    if grunntall <= 4:
        return 'opp'
    else:
        return 'ned'

print(joker_bot(data['grunntall'][0]))
print(joker_bot(data['grunntall'][1]))
print(joker_bot(data['grunntall'][2]))
print(joker_bot(data['grunntall'][3]))
print(joker_bot(data['grunntall'][4]))