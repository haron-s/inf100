from pathlib import Path
text = Path("data.txt").read_text(encoding="utf-8")
Path("data.txt").write_text("tekst" ,encoding="utf-8")

def filter_wordlist(path, search_string):
    file_content = Path(path).read_text(encoding="utf-8")
    return [line.strip() for line in file_content.splitlines() if search_string in line]

def test_filter_wordlist():
    print('Tester filter_wordlist... ', end='')

    # Test 1
    expected = ['database', 'baser']
    actual = filter_wordlist('sample.txt', 'base')
    assert expected == actual

    # Test 2
    expected = [
      'småstad', 'småstaden', 'småstas', 'småstasen', 'småstat', 'småstaten',
      'småstatene', 'småstater',
    ]
    actual = filter_wordlist('nsf2022.txt', 'småsta')
    assert expected == actual

    # Test 3
    expected = [
      'stjerneskudd', 'stjerneskudda', 'stjerneskuddene', 'stjerneskuddet', 
    ]
    actual = filter_wordlist('nsf2022.txt', 'stjerneskudd')
    assert expected == actual

    print('OK')

test_filter_wordlist()