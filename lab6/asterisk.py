def add_asterisks(s):
    asterisk = "*;*".join(s.split(";"))
    return f"*{asterisk}*"

def test_add_asterisks():
    print('Testing add_asterisks...', end='')

    # Test 1
    arg = 'foo;bar;qux'
    actual = add_asterisks(arg)
    expected = '*foo*;*bar*;*qux*'
    assert expected == actual

    # Test 2
    arg = 'honey;mustard'
    actual = add_asterisks(arg)
    expected = '*honey*;*mustard*'
    assert expected == actual

    print('OK')

test_add_asterisks()