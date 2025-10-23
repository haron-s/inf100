from pathlib import Path

def get_stringsum(s):
    string_list = s.split()
    int_list = []
    for string in string_list:
        try:
            int_list.append(int(string))
        except ValueError:
            continue
    return sum(int_list)

def get_line_with_highest_stringsum(s):
    stringsums = (
        (i+1, get_stringsum(line), line)
        for i, line in enumerate(s.splitlines())
        )
    largest_stringsum = next(stringsums)
    for line in stringsums:
        if line[1] > largest_stringsum[1]:
            largest_stringsum = line
    return largest_stringsum

def main():
    return get_line_with_highest_stringsum(Path(input()).read_text(encoding="utf-8"))

def test_get_stringsum():
    print('Testing get_stringsum... ', end='')
    assert 6 == get_stringsum('4 2')
    assert 9 == get_stringsum('5 -1 3 +2')
    assert 11 == get_stringsum('5 - 1 3 + 2')
    assert 42 == get_stringsum('42')
    assert 42 == get_stringsum('forty-one 42 førtitre')
    assert 42 == get_stringsum('foo2 42 2qux 3x1')
    assert 0 == get_stringsum('')
    assert 0 == get_stringsum('foo bar qux')
    assert 0 == get_stringsum('-9- 3+2')
    print('OK')

def test_get_line_with_highest_stringsum():
    print('Testing get_line_with_highest_stringsum... ', end='')

    arg = '4 2\n3 3\n6 6 6 6 12 6\n'
    assert (3, 42, '6 6 6 6 12 6') == get_line_with_highest_stringsum(arg)

    arg = '4 99 -98\nfoo 42 qux\nfoo bar quz\n'
    assert (2, 42, 'foo 42 qux') == get_line_with_highest_stringsum(arg)

    arg = '4 2\n3 3\n'
    assert (1, 6, '4 2') == get_line_with_highest_stringsum(arg)

    print('OK')

test_get_stringsum()
test_get_line_with_highest_stringsum()

if __name__ == "__main__":
    print(main())