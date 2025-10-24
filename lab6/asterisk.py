from pathlib import Path

def add_asterisks(s):
    asterisk = "*;*".join(s.split(";"))
    return f"*{asterisk}*"

def add_asterisks_csv(org_file, new_file):
    file_content = Path(org_file).read_text(encoding="utf-8")
    
    modified_content = [add_asterisks(line) for line in file_content.splitlines()]
    Path(new_file).write_text("\n".join(modified_content),encoding="utf-8")

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

def test_add_asterisks_csv():
    print('Testing add_asterisks_csv...', end='')

    infile = '.tmp.add_asterisks_csv_test.in.csv'
    outfile = '.tmp.add_asterisks_csv_test.out.csv'

    Path(infile).write_text((
        'foo;bar;qux\n'
        'honey;mustard;sausage\n'
    ), encoding='utf-8')

    add_asterisks_csv(infile, outfile)
    actual = Path(outfile).read_text(encoding='utf-8')
    expected = (
        '*foo*;*bar*;*qux*\n'
        '*honey*;*mustard*;*sausage*\n'
    )
    assert expected.strip() == actual.strip()

    print('OK')

test_add_asterisks()
test_add_asterisks_csv()