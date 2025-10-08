from pathlib import Path
import json

def frame(text):
    if text.startswith('#'):
        text = '#' + text
    else:
        text = '# ' + text

    if text.endswith('#'):
        return text + ' #'
    return text + ' #'


print('Testing frame... ', end='')
content = Path("frame_word_test.json").read_text(encoding="utf-8")
data = json.loads(content)
test = data['test_data'][0]
s = test['word']
s = frame(s)
assert test['result'] == frame(s)
print('OK')