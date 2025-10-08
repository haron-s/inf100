from pathlib import Path
import json

content = Path("longest_word.json").read_text(encoding="utf-8")
data = json.loads(content)

word1 = data['words'][0]
word2 = data['words'][1]
word3 = data['words'][2]

word_len1 = len(word1)
word_len2 = len(word2)
word_len3 = len(word3)

longest_n = max(word_len1, word_len2, word_len3)

for i in data['words']:
    if len(i) == longest_n:
        print(i)
        break