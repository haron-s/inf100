from collections import Counter

def can_be_made_of_letters(word, letters):
    return  (Counter(word) <= Counter(letters))

def test_can_be_made_of_letters():
    print('Tester can_be_made_of_letters... ', end='')
    assert can_be_made_of_letters('emoji', 'abcdefghijklmno') is True
    assert can_be_made_of_letters('smilefjes', 'abcdefghijklmnopqrs') is False
    assert can_be_made_of_letters('smilefjes', 'abcdeeefhijlmnopsss') is True
    assert can_be_made_of_letters('lese', 'esel') is True
    print('OK')

def possible_words(wordlist, letters):
    possible_wordlist = [
        word for word in wordlist
        if can_be_made_of_letters(word, letters)
        ]
    return possible_wordlist

def test_possible_words():
    print('Tester possible_words... ', end='')
    hundsk =['tur', 'mat', 'kos', 'hent', 'sitt', 'dekk', 'voff']
    kattsk =['kos', 'mat', 'pus', 'mus', 'purr', 'mjau', 'hiss']
    assert(['kos', 'sitt'] == possible_words(hundsk, 'fikmopsttuv'))
    assert(['kos', 'pus', 'mus'] == possible_words(kattsk, 'fikmopsttuv'))
    print('OK')

test_can_be_made_of_letters()
test_possible_words()