from pathlib import Path
from collections import defaultdict

def symbol_count(path):
    file_content = Path(path).read_text(encoding="utf-8")
    
    char_count = {}
    for character in remove_whitespaces(file_content):
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1

    return char_count

#samme funksjon med bruk av defaultdict class fra collections library
def symbol_count_defaultdict(path):
    file_content = Path(path).read_text(encoding="utf-8")
    
    char_count = defaultdict(int)
    for character in remove_whitespaces(file_content):
        char_count[character] += 1

    return char_count

def remove_whitespaces(s):
    return "".join(s.split())

def test_count_letters():
    print('Tester count_letters... ', end='')
    expected = {
        'K': 2, 'j': 1, 'æ': 1, 'r': 10, 'e': 15, 'v': 3, 'n': 10, ',': 2,
        'S': 2, 'a': 3, 't': 2, 'y': 3, '.': 2, '"': 2, 'F': 2, 'i': 3,
        ':': 1, 'B': 1, 'o': 2, 'd': 2, 'J': 1, 'u': 1, "'": 1, 's': 4,
        'E': 1, 'p': 1, '!': 1, 'l': 2, 'm': 3,
    }
    actual = symbol_count('postcard.txt')
    assert 'æ' in actual, 'æ mangler, har du husket utf-8 encoding?'
    assert expected == actual
    print('OK')

test_count_letters()