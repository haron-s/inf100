from pathlib import Path
import json

content = Path("shortest_words.json").read_text(encoding="utf-8")
data = json.loads(content)

word1 = data['words'][0]
word2 = data['words'][1]
word3 = data['words'][2]

word_len1 = len(word1)
word_len2 = len(word2)
word_len3 = len(word3)

shortest_n = min(word_len1, word_len2, word_len3)

for i in data['words']:
    if len(i) == shortest_n:
        print(i)