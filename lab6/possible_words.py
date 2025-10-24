from pathlib import Path
from collections import Counter

def contains(letters_count, string):
    string_count = {}
    for char in string:
        string_count[char] = string_count.get(char,0) + 1

    return all(string_count[char] <= letters_count.get(char, 0) for char in string_count)

def possible_words_from_file(path, letters): # doesn't use Counter() from collections
    word_list = Path(path).read_text(encoding="utf-8").splitlines()
    letters_count = {}
    for char in letters:
        letters_count[char] = letters_count.get(char,0) + 1
    
    return [word for word in word_list if contains(letters_count, word)]

def possible_words_from_file_collections(path, letters): # uses Counter() from collections
    word_list = Path(path).read_text(encoding="utf-8").splitlines()
    letters_count = Counter(letters)
    return [word for word in word_list if not Counter(word) - letters_count]

def test_possible_words_from_file():
    print('Tester possible_words_from_file... ', end='')
    assert(['du', 'dun', 'hu', 'hud', 'hun', 'hund', 'nu', 'uh']
            == possible_words_from_file('nsf2022.txt', 'hund'))

    # Ekstra test for varianten hvor det er wildcard i bokstavene
    # assert(['a', 'cd', 'cv', 'e', 'i', 'pc', 'wc', 'æ', 'å']
    #         == possible_words_from_file('nsf2022.txt', 'c*'))
    print('OK')

def test_possible_words_from_file_collections():
    print('Tester possible_words_from_file_collections... ', end='')
    assert(['du', 'dun', 'hu', 'hud', 'hun', 'hund', 'nu', 'uh']
            == possible_words_from_file_collections('nsf2022.txt', 'hund'))

    # Ekstra test for varianten hvor det er wildcard i bokstavene
    # assert(['a', 'cd', 'cv', 'e', 'i', 'pc', 'wc', 'æ', 'å']
    #         == possible_words_from_file('nsf2022.txt', 'c*'))
    print('OK')

if __name__ == '__main__':
    test_possible_words_from_file()
    test_possible_words_from_file_collections()